from app import db
from app.models import Question, User


def main():
    User.query.delete()
    Question.query.delete()
    q0 = Question(qnumber=0, title='Question 0',
                  description='What is the name of first country in first row of olypmics df?',
                  answer='Afghanistan',
                  answer_type='String',
                  base_score=5)

    db.session.add(q0)
    db.session.commit()

    q0 = Question(qnumber=1, title='Question 1',
                  description='Which country has won the most gold medals in summer games?',
                  answer='United States',
                  answer_type='String',
                  base_score=10)

    db.session.add(q0)
    db.session.commit()
    
    q0 = Question(qnumber=2, title='Question 2',
                  description='Which country had the biggest difference between their summer and winter gold medal counts?',
                  answer='United States',
                  answer_type='String',
                  base_score=10)

    db.session.add(q0)
    db.session.commit()   
     
    q0 = Question(qnumber=3, title='Question 3',
                  description='Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count? Only include countries that have won at least 1 gold in both summer and winter.',
                  answer='Bulgaria',
                  answer_type='String',
                  base_score=10)

    db.session.add(q0)
    db.session.commit()  

    s = 'Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.'
    q0 = Question(qnumber=4, title='Question 4',
                  description=s,
                  answer='[2, 27, 130, 16, 22, 923, 569, 43, 24, 1, 1, 154, 276, 1, 5, 2, 184, 2, 411, 3, 12, 846, 24, 1120, 29, 7, 2, 67, 420, 2, 134, 327, 335, 1, 14, 5, 49, 1, 77, 94, 895, 1500, 2, 42, 1546, 269, 1068, 459, 5, 1574, 213, 3, 2, 1, 3, 6, 962, 6, 50, 49, 110, 1, 55, 10, 1333, 131, 866, 113, 168, 90, 609, 2, 4, 47, 6, 15, 38, 9, 1, 9, 1, 109, 9, 37, 2, 39, 4, 8, 727, 2, 203, 1, 37, 985, 19, 5, 2, 9, 11, 520, 39, 10, 4, 572, 1042, 14, 2526, 287, 4, 2, 11, 17, 6, 58, 56, 148, 268, 4, 2, 4, 1217, 630, 6, 32, 4, 4, 44, 1, 2, 27, 19, 191, 14, 220, 3, 5684, 16, 38, 18, 4, 2, 171, 4, 3, 18, 38]',
                  answer_type='Series[int]',
                  base_score=10)

    db.session.add(q0)
    db.session.commit()  

    q0 = Question(qnumber=5, title='Question 5',
                  description="Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)",
                  answer='Alabama',
                  answer_type='String',
                  base_score=10)

    db.session.add(q0)
    db.session.commit()  

    q0 = Question(qnumber=6, title='Question 6',
                  description="Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.",
                  answer='Alabama',
                  answer_type='List[str]',
                  base_score=10)

    db.session.add(q0)
    db.session.commit()  
    
    q0 = Question(qnumber=7, title='Question 7',
                  description="Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns. For example, if County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.",
                  answer='Alabama',
                  answer_type='String',
                  base_score=10)

    db.session.add(q0)
    db.session.commit()  

    q0 = Question(qnumber=8, title='Question 8',
                  description='In the census datafile, the United States is broken up into four regions using the "REGION" column. Create a query that finds the counties that belong to regions 1 or 2, whose name starts with "Washington", and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014. This function should return a 5x2 DataFrame with the columns = ["STNAME", "CTYNAME"] and the same index ID as the census_df (sorted ascending by index).',
                  answer='Bulgaria',
                  answer_type='DataFrame',
                  base_score=10)

    db.session.add(q0)
    db.session.commit()  

    q1 = Question(qnumber=9, title='Question 9',
                  description='How many unique cities have games been played in?',
                  answer=1965,
                  answer_type='Integer',
                  base_score=10)

    db.session.add(q1)
    db.session.commit()

    q2 = Question(qnumber=10, title='Question 10',
                  description='How many games were played in Glasgow, Scotland?',
                  answer=317,
                  answer_type='Integer',
                  base_score=10)

    db.session.add(q2)
    db.session.commit()