from flask import render_template, flash, request, redirect, url_for, jsonify
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm
from app.models import User, Question, QuestionAttempt
from werkzeug.urls import url_parse
from datetime import datetime
import numpy as np


@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    if data['username'] == 'YOUR-USERNAME-HERE':
        return jsonify('Please fill out your username in the Jupyter Notebook cell :)')
    user = User(username=data['username'])
    user.set_password(data['password'])
    try:
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify('This username already exists. Please try another one.')
    return jsonify('Team created successfully.')


@app.route('/api/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    q = [{
        'qnumber': question.qnumber,
        'title': question.title,
        'description': question.description,
        'format': question.format,
        'answer': question.answer,
        'base_score': question.base_score
    } for question in questions]
    return jsonify(q)


@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    u = [{
        'username': user.username,
        'score': user.score(),
        'last_submission': user.last_submission(),
        'attempts': user.attempts()
    } for user in users]
    u = sorted(u, key=lambda i: i['score'])[::-1]
    u = sorted(u, key=lambda i: i['attempts'])
    u = sorted(u, key=lambda i: i['last_submission'])
    print(u)
    for i, user in enumerate(u):
        u[i]['rank'] = i+1
    return jsonify(u)

@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    print(username)
    user = User.query.filter_by(username=username).first()
    score = user.score()
    return jsonify('ok')



def process_dtype(answer, dtype):
    if dtype == 'Integer':
        return int(answer)
    else:
        return answer


def process_response(response, base_answer, dtype):
    if dtype == 'Integer':
        return response == base_answer
    else:
        return response == base_answer


@app.route('/api/question_attempt', methods=['POST'])
def question_attempt():
    time_attempted = datetime.utcnow()
    # Expect a username, password, qnumber, and reponse
    data = request.get_json()

    # Validate user
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        q = Question.query.filter_by(qnumber=data['qnumber']).first()
        if not q:
            return jsonify('There are no questions with that index.')
        correctAlready = QuestionAttempt.query \
                                        .filter_by(user_id=user.id,
                                                   question_id=q.id,
                                                   is_correct=True).first()
        if correctAlready:
            return jsonify(f'Already answered question {data["qnumber"]} correctly.')
        base_answer = process_dtype(q.answer, q.answer_type)
        is_correct = process_response(data['response'],
                                      base_answer,
                                      q.answer_type)
        attempt = QuestionAttempt(
            user_id=user.id,
            question_id=q.id,
            time_attempted=time_attempted,
            is_correct=is_correct
        )
        db.session.add(attempt)
        db.session.commit()
        return jsonify({'is_correct': is_correct,
                        'time_attempted': time_attempted})
    else:
        return jsonify('authentication failed')
    return jsonify('ok')
