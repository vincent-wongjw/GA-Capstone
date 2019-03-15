import numpy as np
import pandas as pd
from surprise import Reader, Dataset, SVD, KNNWithMeans
from sklearn.metrics.pairwise import cosine_similarity

import pickle


# UUCF for existing users
def uucf_recom_currentuser(current_user_id, n):
	'''
	Function that takes in a list of current user id and returns recommendations.
	
	Arguments:
	- current_user_id from database
	- n number of recommendations
	'''
	# load rest_reviews_nv_real pickle file
	with open("../Part 2 - Recommender system/user_rating_by_rest_exdate.pkl", "rb") as f:
		user_rating_by_rest_exdate = pickle.load(f)

	# load rec_uucf_surprise pickle file
	with open("../Part 2 - Recommender system/rec_uucf_surprise.pkl", "rb") as f:
		algo_uucf = pickle.load(f)

	# Initiate recommended scores for every item in the catalog
	recommendations = {'items': [], 'rating': []}
	
	for item in user_rating_by_rest_exdate['unique_store_id'].unique():
#         if item not in list(user_rating_by_rest_exdate[user_rating_by_rest_exdate['user_id'] == current_user_id]\
#                             ['unique_store_id']):
			rating = algo_uucf.predict(current_user_id, item, verbose = False)[3]
			recommendations['items'].append(item)
			recommendations['rating'].append(rating)
#         else:
#             pass
	
	# Take top n items and recommend to user
	recs_df = pd.DataFrame(recommendations).rename(columns={"items": "Recommended Restaurants in Las Vegas"}).sort_values(by = 'rating', ascending = False)[:int(n)].iloc[:, 0]
	recs_df.index = np.arange(1, len(recs_df) + 1)
	recs_df = pd.DataFrame(recs_df)
	
	return recs_df    



# UUCF for new users
def uucf_recom_newuser(new_restaurants, n):
	'''
	Function that takes in a list of new restaurants and returns recommendations.
	
	Arguments:
	- new_restaurants : List of restaurants chosen by new user.
	- n number of recommendations
	'''
	
	# load rest_reviews_nv_real pickle file
	with open("../Part 2 - Recommender system/user_rating_by_rest_exdate.pkl", "rb") as f:
		user_rating_by_rest_exdate = pickle.load(f)

	# load rec_uucf_surprise pickle file
	with open("../Part 2 - Recommender system/rec_uucf_surprise.pkl", "rb") as f:
		algo_uucf = pickle.load(f)

	# Append new customer to a new dataframe, and assign a unique customer id
	new_data = pd.DataFrame({'user_id': ['newuser123']*len(new_restaurants),
							 'unique_store_id': new_restaurants,
							 'user_stars': [4]*len(new_restaurants)})
	combined_data = pd.concat([new_data, user_rating_by_rest_exdate]).reset_index(drop=True)
	
	# Initatialise dataset with surprise and do train-test split
	reader = Reader(rating_scale = (1,5))
	data = Dataset.load_from_df(combined_data[['user_id', 'unique_store_id', 'user_stars']], reader)
	trainset = data.build_full_trainset()
	
#     # This algo must be trained before this function is executed. 
	algo_uucf.fit(trainset)
	
	# Initiate recommended scores for every item in the catalog
	recommendations = {'items': [], 'rating': []}
	
	for item in user_rating_by_rest_exdate['unique_store_id'].unique():
#         if item not in list(user_rating_by_rest_exdate[user_rating_by_rest_exdate['user_id'] == 'newuser123']['unique_store_id']):
			rating = algo_uucf.predict('newuser123', item, verbose = False)[3]
			recommendations['items'].append(item)
			recommendations['rating'].append(rating)
#         else:
#             pass
	
	# Take top n items and recommend to user
	recs_df = pd.DataFrame(recommendations).rename(columns={"items": "Recommended Restaurants in Las Vegas"}).sort_values(by = 'rating', ascending = False)[:int(n)].iloc[:, 0]
	recs_df.index = np.arange(1, len(recs_df) + 1)
	recs_df = pd.DataFrame(recs_df)
	
	return recs_df    



# IICF for existing users
def iicf_recom_currentuser(current_user_id, n):
	'''
	Function that takes in a list of current user id and returns recommendations.
	
	Arguments:
	- current_user_id from database
	- n number of recommendations
	'''
	# load rest_reviews_nv_real pickle file
	with open("../Part 2 - Recommender system/user_rating_by_rest_exdate.pkl", "rb") as f:
		user_rating_by_rest_exdate = pickle.load(f)

	# load rec_uucf_surprise pickle file
	with open("../Part 2 - Recommender system/rec_iicf_surprise.pkl", "rb") as f:
		algo_iicf = pickle.load(f)

	# Initiate recommended scores for every item in the catalog
	recommendations = {'items': [], 'rating': []}
	
	for item in user_rating_by_rest_exdate['unique_store_id'].unique():
#         if item not in list(user_rating_by_rest_exdate[user_rating_by_rest_exdate['user_id'] == current_user_id]\
#                             ['unique_store_id']):
			rating = algo_iicf.predict(current_user_id, item, verbose = False)[3]
			recommendations['items'].append(item)
			recommendations['rating'].append(rating)
#         else:
#             pass
	
	# Take top n items and recommend to user
	recs_df = pd.DataFrame(recommendations).rename(columns={"items": "Recommended Restaurants in Las Vegas"}).sort_values(by = 'rating', ascending = False)[:int(n)].iloc[:, 0]
	recs_df.index = np.arange(1, len(recs_df) + 1)
	recs_df = pd.DataFrame(recs_df)
	
	return recs_df    


# IICF for new users
def iicf_recom_newuser(new_restaurants, n):
	'''
	Function that takes in a list of new restaurants and returns recommendations.
	
	Arguments:
	- new_restaurants : List of restaurants chosen by new user.
	- n number of recommendations
	'''
	
	# load rest_reviews_nv_real pickle file
	with open("../Part 2 - Recommender system/user_rating_by_rest_exdate.pkl", "rb") as f:
		user_rating_by_rest_exdate = pickle.load(f)

	# load rec_uucf_surprise pickle file
	with open("../Part 2 - Recommender system/rec_iicf_surprise.pkl", "rb") as f:
		algo_iicf = pickle.load(f)

	# Append new customer to a new dataframe, and assign a unique customer id
	new_data = pd.DataFrame({'user_id': ['newuser123']*len(new_restaurants),
							 'unique_store_id': new_restaurants,
							 'user_stars': [4]*len(new_restaurants)})
	combined_data = pd.concat([new_data, user_rating_by_rest_exdate]).reset_index(drop=True)
	
	# Initatialise dataset with surprise and do train-test split
	reader = Reader(rating_scale = (1,5))
	data = Dataset.load_from_df(combined_data[['user_id', 'unique_store_id', 'user_stars']], reader)
	trainset = data.build_full_trainset()
	
#     # This algo must be trained before this function is executed. 
	algo_iicf.fit(trainset)
	
	# Initiate recommended scores for every item in the catalog
	recommendations = {'items': [], 'rating': []}
	
	for item in user_rating_by_rest_exdate['unique_store_id'].unique():
#         if item not in list(user_rating_by_rest_exdate[user_rating_by_rest_exdate['user_id'] == 'newuser123']['unique_store_id']):
			rating = algo_iicf.predict('newuser123', item, verbose = False)[3]
			recommendations['items'].append(item)
			recommendations['rating'].append(rating)
#         else:
#             pass
	
	# Take top n items and recommend to user
	recs_df = pd.DataFrame(recommendations).rename(columns={"items": "Recommended Restaurants in Las Vegas"}).sort_values(by = 'rating', ascending = False)[:int(n)].iloc[:, 0]
	recs_df.index = np.arange(1, len(recs_df) + 1)
	recs_df = pd.DataFrame(recs_df)
	
	return recs_df




# SVD for existing users
def svd_recom_currentuser(current_user_id, n):
	'''
	Function that takes in a list of current user id and returns recommendations.
	
	Arguments:
	- current_user_id from database
	- n number of recommendations
	'''

	# load rest_reviews_nv_real pickle file
	with open("../Part 2 - Recommender system/user_rating_by_rest_exdate.pkl", "rb") as f:
		user_rating_by_rest_exdate = pickle.load(f)

	# load rec_uucf_surprise pickle file
	with open("../Part 2 - Recommender system/rec_svd_surprise.pkl", "rb") as f:
		algo_svd = pickle.load(f)

	# Initiate recommended scores for every item in the catalog
	recommendations = {'items': [], 'rating': []}
	
	for item in user_rating_by_rest_exdate['unique_store_id'].unique():
#         if item not in list(user_rating_by_rest_exdate[user_rating_by_rest_exdate['user_id'] == current_user_id]\
#                             ['unique_store_id']):
			rating = algo_svd.predict(current_user_id, item, verbose = False)[3]
			recommendations['items'].append(item)
			recommendations['rating'].append(rating)
#         else:
#             pass
	
	# Take top n items and recommend to user
	recs_df = pd.DataFrame(recommendations).rename(columns={"items": "Recommended Restaurants in Las Vegas"}).sort_values(by = 'rating', ascending = False)[:int(n)].iloc[:, 0]
	recs_df.index = np.arange(1, len(recs_df) + 1)
	recs_df = pd.DataFrame(recs_df)
	
	return recs_df    



# SVD for new users
def svd_recom_newuser(new_restaurants, n):
	'''
	Function that takes in a list of new restaurants and returns recommendations.
	
	Arguments:
	- new_restaurants : List of restaurants chosen by new user.
	- n number of recommendations
	'''
	
	# load rest_reviews_nv_real pickle file
	with open("../Part 2 - Recommender system/user_rating_by_rest_exdate.pkl", "rb") as f:
		user_rating_by_rest_exdate = pickle.load(f)

	# load rec_uucf_surprise pickle file
	with open("../Part 2 - Recommender system/rec_svd_surprise.pkl", "rb") as f:
		algo_svd = pickle.load(f)

	# Append new customer to a new dataframe, and assign a unique customer id
	new_data = pd.DataFrame({'user_id': ['newuser123']*len(new_restaurants),
							 'unique_store_id': new_restaurants,
							 'user_stars': [4]*len(new_restaurants)})
	combined_data = pd.concat([new_data, user_rating_by_rest_exdate]).reset_index(drop=True)
	
	# Initatialise dataset with surprise and do train-test split
	reader = Reader(rating_scale = (1,5))
	data = Dataset.load_from_df(combined_data[['user_id', 'unique_store_id', 'user_stars']], reader)
	trainset = data.build_full_trainset()
	
#     # This algo must be trained before this function is executed. 
	algo_svd.fit(trainset)
	
	# Initiate recommended scores for every item in the catalog
	recommendations = {'items': [], 'rating': []}
	
	for item in user_rating_by_rest_exdate['unique_store_id'].unique():
#         if item not in list(user_rating_by_rest_exdate[user_rating_by_rest_exdate['user_id'] == 'newuser123']['unique_store_id']):
			rating = algo_svd.predict('newuser123', item, verbose = False)[3]
			recommendations['items'].append(item)
			recommendations['rating'].append(rating)
#         else:
#             pass
	
	# Take top n items and recommend to user
	recs_df = pd.DataFrame(recommendations).rename(columns={"items": "Recommended Restaurants in Las Vegas"}).sort_values(by = 'rating', ascending = False)[:int(n)].iloc[:, 0]
	recs_df.index = np.arange(1, len(recs_df) + 1)
	recs_df = pd.DataFrame(recs_df)
	
	return recs_df



# Content based recommendation for existing users
def content_recom_currentuser(username, num_recommended_res, start_col = 'rest_avg_stars', end_col = 'noiselvl_very_loud', 
						num_similar_res = 20):
	
	# load restaurant matrix pickle file
	with open("../Part 2 - Recommender system/cbf_res_matrix.pkl", "rb") as f:
		res_matrix = pickle.load(f)

	# load pickle file of businesses visited by every individual
	with open("../Part 2 - Recommender system/userbiz_group.pkl", "rb") as f:
		userbiz_group = pickle.load(f)

	# Get restaurants visited by username
	res_list = userbiz_group.loc[username][0].split(', ')
	
	unique_res_list = []
	for res in res_list:
		# Get index of restaurant list 
		unique_res_list.extend(res_matrix[res_matrix['unique_store_id'] == res].index)
	# Get similar customers' restaurants index preferences    
	unique_res_list = np.unique(unique_res_list)

	# Generate average scores of the restarant list
	df_ref = pd.DataFrame(columns = res_matrix.loc[:, start_col:].columns)
	# provide list of indices from the list of restaurants and all cols
	df_ref.loc[0, :] = res_matrix.loc[unique_res_list, start_col:].mean()
	
	# Generate restaurant similarity between res_list and the rest of the other restaurants
	res_similarity = cosine_similarity(df_ref, res_matrix.loc[:, start_col:])
	
	# Find top n most similar res to avg of restaurant list by cosine similarity score
	unique_res_list_id = np.argsort(res_similarity)[0][-(num_similar_res + 1):-1]
	
	# Sort by number of stars
	top_n_recommended_res = res_matrix.loc[unique_res_list_id, 'rest_avg_stars'].sort_values(ascending = False)[: int(num_recommended_res)].index.tolist()
		
	top_n_res_name = []
	for ind in top_n_recommended_res:
		  top_n_res_name.append(res_matrix.loc[ind, 'unique_store_id'])
	
	# Take top n items and recommend to user
	recs_df = pd.DataFrame(top_n_res_name, columns = ['Recommended Restaurants in Las Vegas'])
	recs_df.index = np.arange(1, len(recs_df) + 1)
	recs_df = pd.DataFrame(recs_df)
	
	
	return recs_df


# Content based recommendation for new users
def content_recom_newuser(res_list, num_recommended_res, start_col = 'rest_avg_stars', end_col = 'noiselvl_very_loud', 
						num_similar_res = 20):
	
	# load restaurant matrix pickle file
	with open("../Part 2 - Recommender system/cbf_res_matrix.pkl", "rb") as f:
		res_matrix = pickle.load(f)

	unique_res_list = []
	for res in res_list:
		# Get index of restaurant list 
		unique_res_list.extend(res_matrix[res_matrix['unique_store_id'] == res].index)
	# Get similar customers' restaurants index preferences    
	unique_res_list = np.unique(unique_res_list)

	# Generate average scores of the restarant list
	df_ref = pd.DataFrame(columns = res_matrix.loc[:, start_col:].columns)
	# provide list of indices from the list of restaurants and all cols
	df_ref.loc[0, :] = res_matrix.loc[unique_res_list, start_col:].mean()
	
	# Generate restaurant similarity between res_list and the rest of the other restaurants
	res_similarity = cosine_similarity(df_ref, res_matrix.loc[:, start_col:])
	
	# Find top n most similar res to avg of restaurant list by cosine similarity score
	unique_res_list_id = np.argsort(res_similarity)[0][-(num_similar_res + 1):-1]
	
	# Sort by number of stars
	top_n_recommended_res = res_matrix.loc[unique_res_list_id, 'rest_avg_stars'].sort_values(ascending = False)[: int(num_recommended_res)].index.tolist()
		
	top_n_res_name = []
	for ind in top_n_recommended_res:
		  top_n_res_name.append(res_matrix.loc[ind, 'unique_store_id'])
	
	# Take top n items and recommend to user
	recs_df = pd.DataFrame(top_n_res_name, columns = ['Recommended Restaurants in Las Vegas'])
	recs_df.index = np.arange(1, len(recs_df) + 1)
	recs_df = pd.DataFrame(recs_df)
	
	
	return recs_df