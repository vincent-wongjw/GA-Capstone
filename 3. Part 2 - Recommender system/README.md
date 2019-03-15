Due to large file size and limited space, the data files are not uploaded in this folder. 

Kindly follow and run through the steps in the README files in the following folders sequentially in the order below (so that all the pre-requisite files can be generated) before running through the 'Restaurant Recommender.ipynb' workbook in this folder. 
0. Datasets
1. Processing of Yelp dataset
2. Part 1 - Fake reviews


FYI, the files that will be generated after the code is run from the 'Restaurant Recommender.ipynb' file are as follows:

1) Backup files
- businesses_reviewed.csv
- rest_reviews_nv_real.pkl
- user_rating_by_rest.csv
- user_rating_by_rest_exdate.pkl
- cust_ratings_businesses.csv

2) Pickled files of recommender models (to be used for production models)
- cbf_res_matrix.pkl (for content based filtering)
- userbiz_group.pkl (for content based filtering)
- rec_iicf_surprise.pkl
- rec_uucf_surprise.pkl
- rec_svd_surprise.pkl