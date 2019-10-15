from app import app, db
from app.models import User, Question


def main():
    q1 = Question(qnumber=1, title='Question 1',
                  description='How many unique cities have games been played in?',
                  answer=1965,
                  base_score=10)

    db.session.add(q1)
    db.session.commit()


def q2():
    q1 = Question(qnumber=2, title='Question 2',
                  description='How many games were played in Glasgow, Scotland?',
                  answer=317,
                  base_score=10)

    db.session.add(q1)
    db.session.commit()