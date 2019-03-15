# Restaurant Analytics System 
* Fake Reviews Detection System
* Restaurant Recommender System

#### Project Status: [Completed]

## Project Intro/Objective

As an avid foodie, I often rely on review apps like Tripadvisor and Yelp for reliable restaurant recommendations when I am abroad. Under the hood of these sleek apps is data-driven innovation powering models that are constantly being fine tuned to facilitate an optimal user experience. 

Inspired by the technology that powers these apps, i built a a fake reviews detection system using NLP and classification techniques, and restaurant recommendation system using recommender filtering techniques to recommend products based on user similarity. 

### Methods Used

* Data Processing
* Data Visualization
* NLP - Word Processing, Sentiment Analysis, Word Embeddings
* Machine Learning - Classification Algorithms (Naive Bayes, Logistic Regression, Random Forest Classifier)
* Deep Learning - Convolutional Neural Networks with LSTM
* Recommender Systems
* Deployment of model


### Technologies
* Python - Pandas, Numpy, Scikit-learn
* Datalab using Google Cloud Platform's VM
* SQlite3
* NLP - NLTK (Word Processing, Sentiment Analysis, BOW), Word2Vec
* Deep Learning - Keras
* Recommender Systems - Manual coding of collab/content based filtering, Surprise library
* Deployment - Flask, HTML, CSS

## Project Description

### Objectives
1) Understand and build a model to differentiate fake restaurant reviews from legitimate ones
2) Build restaurant recommender systems, based on review ratings and restaurant attributes 

Using the fake reviews model optimized from the first section, we will use that to filter reviews data from the Yelp dataset in the second section to power the content-based recommender system. 

### Datasets
* Fake Yelp reviews labelled data from Stony Brook University. Since the traning set is too large, it is saved on google drive. Please download it from the link below. The 'YelpZip' and 'YelpNYC' datasets were used for this project
https://drive.google.com/open?id=0B8JIKvhJUvRdfjBaaFB3TWQ1MEstQVpnb1ZDTUZkampJTUpQaEVZYVJmSUVZZS1xSkNJXzA
* Yelp Challenge 2019 dataset: https://www.yelp.com/dataset/challenge. Only the restaurant and reviews dataset were utilised for this project

#### <Do take note that data files generated from each of the workbooks are not uploaded due to large size. Kindly follow the README files in each of the folders, starting from the '0. Datasets' folder to generate the necessary files for subsequent folders>

### 1) Understand and build a model to differentiate fake restaurant reviews from legitimate ones
*<Code found in '2. Part 1 - Fake reviews' folder under 'Fake reviews' Notebook>*

* In this part of the project, I work with a labelled restaurant 600k reviews dataset mined across 5 US states (NJ, VT, CT, PA and NY). The labels are based on Yelp's proprietary algorithm/filtering engine (explained here: https://www.yelpblog.com/2010/03/yelp-review-filter-explained), and are taken as a ground truth. I seek to understand and replicate this filtering engine. 

* Due to the class imbalance of 20% fake reviews, I started off by undersampling the majority class (due to limitations in my local server) and performing some feature engineering like deriving sentiment scores and text length. This resulted in a more manageable ~120k fake reviews and the same number of real reviews. 

* Upon performing EDA on the reviews, there were some interesting observations:
  * i) Fake reviews tend to be shorter in length on average as compared to real reviews, especially for more positively rated reviews
  * ii) Fake reviews tend to be polarised, with significantly higher frequency at ratings 1.0 (worst) and 5.0 (best) as compared to real reviews. 
  * iii) Fake reviews tend to contain words with a stronger tone as compared to real reviews which are more neutral. 
  * iv) Fake reviews tend to use generic and repetitive words that do not directly describe their experience at the food establishment (i.e. I had a good time with my family and friends) whereas real reviews tend to use more descriptive words that describe the experience at the restaurant, with reference to the food and ambience
 
* I subsequently ran classification models, separately using both review text data only and non-review text data only, to predict real and fake review labels. A train-test split and cross-validation testing on train set was applied. 
  * Classification models ran - Naive Bayes, Logistic Regression, RandomForestClassifier, CNN Deep Learning
  * Review text was processed using Bag of Words (CountVectorizer, TfidfVectorizer) and Word Embeddings. 
  * Evaluation metrics - Accuracy score, Recall score, ROC/AUC
  * Results: 
    * Using Naive Bayes had the best recall score of 0.72 using BoW (CountVectorizer) Bigrams
    * Logistic Regression had the best accuracy score of 0.74 using BoW (TfidfVectorizer) Bigrams with stopwords

### 2) Build restaurant recommender systems, based on review ratings and restaurant attributes 
*<Code found in '3. Part 2 - Recommender system' folder under 'Restaurant Recommender' Notebook>*

* Only the Yelp business and reviews datasets (~150k restaurants and ~2.5m reviews) will be used for this section. 
* To facilitate more efficient processing of the datasets, I reduced the scope of the datasets to a more manageable (~1.7k restaurants and ~120k reviews) by:
  * Looking at only Las Vegas restaurants (city with highest density of restaurants) and reviews associated with those restaurants
  * Filter out reviews flagged out as fake (from most optimal model in previous section)
  * Filter out reviews of users with less than 5 reviews
  * Remove restaurants with less than 10 reviews
* Utilised collaborative filtering methods (user-based, item-based and SVD) to make restaurant recommendations to users based on historical review ratings
  * A manual, user-based collab filtering approach was built from scratch to help me understanding how a recommender system works. Subsequently, the Surprise library was used for testing of user-based, item-based and SVD collab-filtering recommender systems 
  * Similarity measures tested - Cosine Similarity and Pearson Correlation
  * Evaluation - using RMSE and Precision score (Recommendation threshold - above 3.5 stars). Training set based on reviews before 2017, and testing set based on reviews from 2017 onwards
  * Results: SVD achieved the best RMSE score of 0.917 while the manual user-based collaborative filtering method achieved the best precision score of 0.798. 
* For the content-based filtering method, I used restaurant attributes to compare similarity across different restaurants to enable users to discover restaurants based on their previously visited restaurants
  * Some feature engineering was carried out - such as whether a restaurant is a chain? Do they serve breakfast/lunch/dinner?
  * Manually coded a content based filtering approach that recommended restaurants ordered by historical average ratings. 
 


### Key learnings
* Test out a minimal viable solution using a small, manageable dataset before scaling it up to larger datasets. Also, be resourceful in seeking out alternative and creative solutions of managing big datasets - so that it doesn't blow up your RAM! For example, using teamviewer on a CPU at home, or using Virtual Machines on the cloud that can be scaled with higher GPUs
* Do not dive too deep into any particular concept and spend too much time understanding - apply and let the concepts on the go
* How to tune and optimize classification models - Start with the data, then the type of model, then the parameters in the model. 
* How to deploy a model using Flask, HTML and CSS


### Next Steps
* Utilise other non-text features like user data and other business metadata like checkins to power the content-based recommender system
* Expand analysis beyond restaurants in the Las Vegas restaurants


## Contact
* Feel free to contact me through the following for further information and opportunities
- Email: wongjw90@gmail.com
- LinkedIn: https://www.linkedin.com/in/vincentwongjw/


## Acknowledgements
- Many thanks to my instructor Edoardo Venturini and TAs - Neil, Samantha and Hafsa from General Assembly for their support on this project
- Credits to Professor Rayana at Stony Brook University for the fake review labeled dataset
