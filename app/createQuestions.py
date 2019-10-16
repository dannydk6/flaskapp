from app import db
from app.models import Question


def main():
    Question.query.delete()
    q1 = Question(qnumber=1, title='Question 1',
                  description='How many unique cities have games been played in?',
                  answer=1965,
                  answer_type='Integer',
                  base_score=10)

    db.session.add(q1)
    db.session.commit()

    q2 = Question(qnumber=2, title='Question 2',
                  description='How many games were played in Glasgow, Scotland?',
                  answer=317,
                  base_score=10)

    db.session.add(q2)
    db.session.commit()
