from datetime import datetime
from app import db, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from time import time
import jwt


followers = db.Table('followers',
                     db.Column('follower_id', db.Integer,
                               db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer,
                               db.ForeignKey('user.id'))
                     )

class QuestionAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    time_attempted = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    is_correct = db.Column(db.Boolean, index=True, default=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=False)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic'
    )

    def attempts(self):
        attempts = QuestionAttempt.query\
            .filter_by(user_id=self.id,
                       is_correct=True)\
            .join(Question)\
            .add_columns(Question.base_score).all()
        return len(attempts)

    def score(self):
        attempts = QuestionAttempt.query\
            .filter_by(user_id=self.id,
                       is_correct=True)\
            .join(Question)\
            .add_columns(Question.base_score).all()
        scores = [a.base_score for a in attempts]
        if scores:
            return sum(scores)
        return 0

    def last_submission(self):
        attempts = QuestionAttempt.query\
            .filter_by(user_id=self.id,
                       is_correct=True).all()
        submissions = [a.time_attempted for a in attempts]
        if submissions:
            return max(submissions)
        return datetime.strptime('2020-10-11','%Y-%m-%d')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qnumber = db.Column(db.Integer, default=None)
    title = db.Column(db.String(), default="")
    description = db.Column(db.String(), default="")
    format = db.Column(db.String(), default="JSON")
    answer = db.Column(db.String(), default=None)
    answer_type = db.Column(db.String(), default='String')
    base_score = db.Column(db.Integer, default=10)

    
class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    num_completed = db.Column(db.Integer, default=0)
    num_attempted = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=0)