from flask import Flask,render_template,session,redirect,url_for, jsonify, session
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, SelectField, TextAreaField)
from wtforms.validators import DataRequired

# Import functions from .py files
from reviews_engine_nb import get_review_prediction
from recsys_engine import uucf_recom_currentuser, uucf_recom_newuser, iicf_recom_currentuser, iicf_recom_newuser, svd_recom_currentuser, svd_recom_newuser, content_recom_currentuser, content_recom_newuser

app = Flask(__name__)

app.config['SECRET_KEY']='key'

class ReviewForm(FlaskForm):

	review = TextAreaField(' ', validators = [DataRequired()])
	submit = SubmitField('Submit')

class ExistingUser(FlaskForm):
	existing_user = SelectField('Select Existing User',
								choices=[('TdYKJgSgY2GF_YJnwsi5yQ','TdYKJgSgY2GF_YJnwsi5yQ'),
						               		('DUF9LYMMCCawUcnzzXDf4Q','DUF9LYMMCCawUcnzzXDf4Q'),('WG0kTEJJNfT1egnunxpsvQ','WG0kTEJJNfT1egnunxpsvQ'),
						                    ('gjhzKWsqCIrpEd9pevbKZw','gjhzKWsqCIrpEd9pevbKZw'),('oS2O8YQ31HTSTQgPQKc7Cg','oS2O8YQ31HTSTQgPQKc7Cg'),
						                    ('kS1MQHYwIfD0462PE61IBw','kS1MQHYwIfD0462PE61IBw'),('uT88e0NuTpxcqcv3cAyUKA','uT88e0NuTpxcqcv3cAyUKA'),
						                    ('zMLbjqeTqp83g0uIAk0SWg','zMLbjqeTqp83g0uIAk0SWg')])
	recsys_type = SelectField('Choose Recommender System Type',
									choices= [('(Collab filtering) User-User','(Collab filtering) User-User'),
									('(Collab Filtering) Item-Item','(Collab Filtering) Item-Item'), 
									('(Collab Filtering) Singular Value Decomposition - SVD','(Collab Filtering) Singular Value Decomposition - SVD'),
									('Content-Based Filtering','Content-Based Filtering')])

	num_of_recommendations = SelectField('Select Number of Recommendations',
									choices= [('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'),
									('8','8'), ('9','9'), ('10','10')])

	submit = SubmitField('Submit')

class NewUser(FlaskForm):
	new_restaurants_1 = SelectField('Select New Restaurant 1',
								choices=[('The Cuppa (Outlet 1 - 89135)','The Cuppa (Outlet 1 - 89135)'),
						               		('Sushi Loca (Outlet 1 - 89149)','Sushi Loca (Outlet 1 - 89149)'),
						               		('Bouchon Bakery at the Venetian Theater','Bouchon Bakery at the Venetian Theater'),
						                    ("Capo's Italian Cuisine","Capo's Italian Cuisine"),('Lotus of Siam (Outlet 1 - 89104)','Lotus of Siam (Outlet 1 - 89104)'),
						                    ('Yu-Yu','Yu-Yu'),('The Capital Grille','The Capital Grille'),
						                    ('Pei Wei Asian Diner','Pei Wei Asian Diner')])
	new_restaurants_2 = SelectField('Select New Restaurant 2',
								choices=[('Metro Pizza (Outlet 1 - 89119)','Metro Pizza (Outlet 1 - 89119)'),
						               		('Bouchon','Bouchon'),
						               		('SkinnyFATS (Outlet 1 - 89148)','SkinnyFATS (Outlet 1 - 89148)'),
						                    ("Battista's Hole In the Wall","Battista's Hole In the Wall"),('Hiromaru Fusion Ramen','Hiromaru Fusion Ramen'),
						                    ('SUSHISAMBA - Las Vegas','SUSHISAMBA - Las Vegas'),('Viet Noodle Bar','Viet Noodle Bar'),
						                    ('Tonkatsu Kiyoshi','Tonkatsu Kiyoshi')])

	new_restaurants_3 = SelectField('Select New Restaurant 3',
								choices=[('Mon Ami Gabi','Mon Ami Gabi'),
						               		('Buldogis Gourmet Hot Dogs','Buldogis Gourmet Hot Dogs'),
						               		('Wolfgang Puck Bar & Grill Summerlin','Wolfgang Puck Bar & Grill Summerlin'),
						                    ("Maggiano's Little Italy","Maggiano's Little Italy"),('Morels French Steakhouse & Bistro','Morels French Steakhouse & Bistro'),
						                    ("Lola's A Louisana Kitchen","Lola's A Louisana Kitchen"),('Wo Fat','Wo Fat'),
						                    ('Eggslut','Eggslut')])

	num_of_recommendations = SelectField('Select Number of Recommendations',
									choices= [('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'),
									('8','8'), ('9','9'), ('10','10')])	

	recsys_type = SelectField('Choose Recommender System Type',
									choices= [('(Collab filtering) User-User','(Collab filtering) User-User'),
									('(Collab Filtering) Item-Item','(Collab Filtering) Item-Item'), 
									('(Collab Filtering) Singular Value Decomposition - SVD','(Collab Filtering) Singular Value Decomposition - SVD'),
									('Content-Based Filtering','Content-Based Filtering')])

	submit = SubmitField('Submit')




@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/fakerevsys', methods = ['GET', 'POST'])
def fakerevsys():
	form = ReviewForm()
	if form.validate_on_submit():
		session['review'] = form.review.data
		nb_prediction, sentiment_polarity, subjectivity = get_review_prediction(session['review'])

		return render_template('fakerevsys.html', nb_prediction = nb_prediction, 
							sentiment_polarity = sentiment_polarity, subjectivity = subjectivity, form = form, display_result = True, fakerevsys = True)

	return render_template('fakerevsys.html', form = form, display_result = False,  fakerevsys = True)


@app.route('/resrecsys_existinguser', methods = ['GET', 'POST'])
def resrecsys_existinguser():
	form = ExistingUser()

	if form.validate_on_submit():
		session['existing_user'] = form.existing_user.data
		session['recsys_type'] = form.recsys_type.data
		session['num_of_recommendations'] = form.num_of_recommendations.data

		if session['recsys_type'] == '(Collab filtering) User-User':
			recs_df_exist = uucf_recom_currentuser(session['existing_user'], session['num_of_recommendations'])
			return render_template('resrecsys_existinguser.html', tables_exist = [recs_df_exist.to_html()], form = form, display_result = True, resrecsys_existinguser = True)

		if session['recsys_type'] == '(Collab Filtering) Item-Item':
			recs_df_exist = iicf_recom_currentuser(session['existing_user'], session['num_of_recommendations'])
			return render_template('resrecsys_existinguser.html', tables_exist = [recs_df_exist.to_html()], form = form, display_result = True, resrecsys_existinguser = True)

		if session['recsys_type'] == '(Collab Filtering) Singular Value Decomposition - SVD':
			recs_df_exist = svd_recom_currentuser(session['existing_user'], session['num_of_recommendations'])
			return render_template('resrecsys_existinguser.html', tables_exist = [recs_df_exist.to_html()], form = form, display_result = True, resrecsys_existinguser = True)

		if session['recsys_type'] == 'Content-Based Filtering':
			recs_df_exist = content_recom_currentuser(session['existing_user'], session['num_of_recommendations'])
			return render_template('resrecsys_existinguser.html', tables_exist = [recs_df_exist.to_html()], form = form, display_result = True, resrecsys_existinguser = True)

	return render_template('resrecsys_existinguser.html', form = form, resrecsys_existinguser = True)


@app.route('/resrecsys_newuser', methods = ['GET', 'POST'])
def resrecsys_newuser():
	form = NewUser()

	if form.validate_on_submit():
		session['new_restaurants_1'] = form.new_restaurants_1.data
		session['new_restaurants_2'] = form.new_restaurants_2.data
		session['new_restaurants_3'] = form.new_restaurants_3.data
		session['recsys_type'] = form.recsys_type.data
		session['num_of_recommendations'] = form.num_of_recommendations.data

		temp_list = []
		temp_list.append(session['new_restaurants_1'])
		temp_list.append(session['new_restaurants_2'])
		temp_list.append(session['new_restaurants_3'])

		if session['recsys_type'] == '(Collab filtering) User-User':
			recs_df_new = uucf_recom_newuser(temp_list, session['num_of_recommendations'])
			return render_template('resrecsys_newuser.html', tables_new = [recs_df_new.to_html()], form = form, display_result = True, resrecsys_newuser = True)

		if session['recsys_type'] == '(Collab Filtering) Item-Item':
			recs_df_new = iicf_recom_newuser(temp_list, session['num_of_recommendations'])
			return render_template('resrecsys_newuser.html', tables_new = [recs_df_new.to_html()], form = form, display_result = True, resrecsys_newuser = True)

		if session['recsys_type'] == '(Collab Filtering) Singular Value Decomposition - SVD':
			recs_df_new = svd_recom_newuser(temp_list, session['num_of_recommendations'])
			return render_template('resrecsys_newuser.html', tables_new = [recs_df_new.to_html()], form = form, display_result = True, resrecsys_newuser = True)

		if session['recsys_type'] == 'Content-Based Filtering':
			recs_df_new = content_recom_newuser(temp_list, session['num_of_recommendations'])
			return render_template('resrecsys_newuser.html', tables_new = [recs_df_new.to_html()], form = form, resrecsys_newuser = True)

	return render_template('resrecsys_newuser.html', form = form, resrecsys_newuser = True)

# @app.route('/resrecsys_existinguser', methods = ['GET', 'POST'])
# def resrecsys_existinguser():
# 	form1 = ExistingUser()
# 	return render_template('resrecsys_existinguser.html')


# @app.route('/resrecsys_newuser', methods = ['GET', 'POST'])
# def resrecsys_newuser():
# 	form2 = NewUser()
# 	return render_template('resrecsys_newuser.html')


if __name__ == '__main__':
    app.run(debug=True)