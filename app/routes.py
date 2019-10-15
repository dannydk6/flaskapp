from flask import render_template, flash, request, redirect, url_for, jsonify
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm
from app.models import User, Question
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime

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
def get_questions(token):
    questions = Question.query.all()
    return jsonify(questions)