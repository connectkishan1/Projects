# Project- House Prices Prediction: Advanced Regression Techniques
##### [Kaggle](https://www.kaggle.com/connectkishan1/house-prices-prediction)
* Project for the course Machine Learning
* Participation of the kaggle competition [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/)
* We were graded on leaderboard scores and I scored 11th of the class with position 526th of the leaderboard
* I used a weighted average of XGBoost, Lasso, ElasticNet, and Gradient Boosting Regressor
* The focus of this project was mostly on feature engineering


<img src="https://github.com/connectkishan1/Projects/blob/master/Personal%20Project/Docs/pic/kaggle.JPG" width="70%"/>

---
### Dataset Overview
The dataset contains 79 explanatory variables that describe alsmost every aspect of residential homes in Ames, Iowa. It's up to me to predict the pricing of houses based on the given dataset. The data is split into a train and test data set for me to train and test on.
This dataset is part of a kaggle competition in which the principles of stacking, blending and ensembling techniques can be learned.

### Goal
to predict the sales price for each house. For each Id in the test set, you must predict the value of the SalePrice variable. 

### Metric
Submissions are evaluated on Root-Mean-Squared-Error (RMSE) between the logarithm of the predicted value and the logarithm of the observed sales price.
(Taking logs means that errors in predicting expensive houses and cheap houses will affect the result equally.)

### Visuallization,EDA & Data processing Method that helps to use for other regression Project.
* Heatmap: Features most correlated with target
* Pairplot: Features most correlated with target
* Distribution plot:for all numerical data
* Distribution plot: for column such as target
* Countplot: for all Categorical features
* Boxplot: for all Categorical features vs target
* To create a list of the names of the columns that have Total missing values/% of missing value
* filling missing value
* log transform the column 1d such as target 
* Top 20 display features with largest positive skew
* scaling of numerical feature
* getdummies for catgorical feature
* grid search to find the best parameters for each model
* cross_val_score with RMSE & r2 score technique


