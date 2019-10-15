from flask import render_template, flash, request, redirect, url_for, jsonify
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm
from app.models import User, Question
from werkzeug.urls import url_parse
from datetime import datetime
import numpy as np

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    print(data)
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify('ok')
    

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
        'score': np.random.randint(100),
        'last_submission': '2019-10-18 00:00:00'
    } for user in users]
    u = sorted(u, key=lambda i: i['score'])
    
    return jsonify(u[::-1])