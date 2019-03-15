import pickle
from textblob import TextBlob

def get_review_prediction(text):
	# Load TfidfVectorizer fit pickle file from train data in the fake reviews file
	with open('../Part 1 - Fake reviews/tvec_fit.pkl', "rb") as f:
	    tvec_fit = pickle.load(f)

	# Load Naive Bayes trained model pickle file from train data in the fake reviews file
	with open('../Part 1 - Fake reviews/mnb_model.pkl', "rb") as f:
	    mnb_model = pickle.load(f)

	# Transform text into list so that it can be processed
	temp_list = []
	temp_list.append(text)
	print(temp_list)

	# Fit and transform text data using TfidfVectorizer
	X = tvec_fit.transform(temp_list)
	nb_prediction = mnb_model.predict(X)
	# option to predict_proba
	nb_predict_proba = mnb_model.predict_proba(X)

	if nb_prediction.all() == 1:
		nb_prediction = 'Real Review'
	else:
		nb_prediction = 'Fake Review'

	if (nb_predict_proba[0][1] >= 0.65) or (nb_predict_proba[0][1] <= 0.35):
		nb_prediction = nb_prediction + ' (High Confidence)'

	sentiment_polarity = TextBlob(text).sentiment[0]
	subjectivity = TextBlob(text).sentiment[1]

	if sentiment_polarity > 0.5:
		sentiment_polarity = 'Very Positive'
	elif sentiment_polarity > 0.2:
		sentiment_polarity = 'Positive'
	elif sentiment_polarity < -0.5:
		sentiment_polarity = 'Very Negative'
	elif sentiment_polarity < -0.1:
		sentiment_polarity = 'Negative'
	else:
		sentiment_polarity = 'Neutral'

	if (subjectivity >= 0.7) or (subjectivity <= -0.7):
		subjectivity = 'Very Subjective'
	elif (subjectivity >= 0.2) or (subjectivity <= -0.2):
		subjectivity = 'Mildly Subjective'
	else:
		subjectivity = 'Neutral'

	return nb_prediction, sentiment_polarity, subjectivity