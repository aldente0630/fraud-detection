# IEEE Fraud Detection with Unsupervised Learning
## Requirement
* The dataset can be downloaded from [this Kaggle competition](https://www.kaggle.com/c/ieee-fraud-detection/).
* `Altair`, `vega-datasets`, `PyOD` and `scikit-learn` version 0.24 libraries are required. 
* For some experiments, `Amazon SageMaker` and related SDKs are needed. This installation can be skipped.
  
## EDA
To preprocess data for modeling, I quickly explored proportions of missing values, cardinalities of categorical variables, distributions of numeric variables, and a correlation coefficient matrix. For the efficiency of the calculation, I selected 100 features by random sampling and looked at the proportions of their missing values. I have found that most of the features have a fairly high percentage of missing values.
  
[!Proportions of Missing Values](https://github.com/aldente0630/fraud-detection-with-unsupervised-learning/blob/b959ce754282ed28d2d43ed079d7d06c214d735e/prop_of_missing_values.png)
