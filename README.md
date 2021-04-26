# IEEE Fraud Detection with Unsupervised Learning
## Goals
* The prediction performances and computation times of various **unsupervised learning anomaly detection** algorithms such as **Isolation Forest**, **COPOD**, and **Random Cut Forest**, are compared.
* (Optional) `Altair` is applied for the purpose of drawing interactive plots during EDA.
  
## Requirement
* The dataset can be downloaded from [this Kaggle competition](https://www.kaggle.com/c/ieee-fraud-detection/).
* `Altair`, `vega-datasets`, `PyOD` and `scikit-learn` version 0.24 libraries are required. 
* For some experiments, `Amazon SageMaker` and related SDKs are needed. This installation can be skipped.
  
## EDA
To preprocess data for modeling, I quickly explored proportions of missing values, cardinalities of categorical features, distributions of numerical features, and a correlation coefficient matrix. For the efficiency of the calculation, I selected 100 features by random sampling and looked at the proportions of their missing values. I have found that most of the features have a fairly high percentage of missing values.
  
![Proportions of Missing Values](https://github.com/aldente0630/fraud-detection-with-unsupervised-learning/blob/b959ce754282ed28d2d43ed079d7d06c214d735e/prop_of_missing_values.png)
  
A list and description of categorical features can be found on [this Kaggle page](https://www.kaggle.com/c/ieee-fraud-detection/data). Some categorical features have more than a few hundred categories, or even more than 10,000.

![Cardinalities of Categorical Features](https://github.com/aldente0630/fraud-detection-with-unsupervised-learning/blob/5eadffe29734da70371e84b06eb73706a1c7731d/card_of_cat_features.png)
  
In order to examine the distribution of numerical features, some of the features with few missing values and adequately distributed were randomly selected. From the histograms, it can be seen that most of the features have a long tail.

![Histograms of Numeric Features](https://github.com/aldente0630/fraud-detection-with-unsupervised-learning/blob/f3336064503ab632af395f9cf75208437963ab76/hist_of_num_features.png)  
  
Finally I calculated the correlation coefficient matrix. While most of the features are not correlated, some have very high positive correlations.

![Correlation Matrix](https://github.com/aldente0630/fraud-detection-with-unsupervised-learning/blob/8d2e8f22179512119765ca5bd9cbdedefc2d990a/corr_matrix.png)

## Data Splitting & Preprocessing
In the general case of unsupervised learning, it is not possible to evaluate the predictive performance, but since there are labels in this example, 20% of the total was splitted into the validation dataset. Ordinal Encoding and imputation were applied to categorical features, and imputation was applied after normalization to numeric features. To view the transformed validation dataset, the dimensions of the dataset was reduced using **t-SNE**. The manifold looks like a twisted band, and the fraudulent labels appear to exist outside the clusters. Therefore, it seems that pretty good accuracy can be achieved even with unsupervised learning.
  
![Scatter Plot of Manifold with t-SNE](https://github.com/aldente0630/fraud-detection-with-unsupervised-learning/blob/84b3aa0258e6820a762707b50ca21d405ab77980/images/scatter_of_manifold.png)

## Moding with Isolation Forest, Random Cut Forest and COPOD
I used popular tree ensemble models, namely **Isolation Forest** and **Random Cut Forest**, and the latest algorithm **Copula-based Outlier Detection**(COPOD). For a detailed description of the algorithms, refer to the following links.
* [Liu, Fei Tony, Ting, Kai Ming and Zhou, Zhi-Hua. “Isolation forest.” Data Mining, 2008. ICDM’08. Eighth IEEE International Conference on.](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf?q=isolation-forest)
* [Liu, Fei Tony, Ting, Kai Ming and Zhou, Zhi-Hua. “Isolation-based anomaly detection.” ACM Transactions on Knowledge Discovery from Data (TKDD) 6.1 (2012): 3.](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/tkdd11.pdf)
* [Sudipto Guha, Nina Mishra, Gourav Roy, and Okke Schrijvers. "Robust random cut forest based anomaly detection on streams." In International Conference on Machine Learning, pp. 2712-2721. 2016. ](http://proceedings.mlr.press/v48/guha16.pdf)
* [Li, Z., Zhao, Y., Botta, N., Ionescu, C. and Hu, X. COPOD: Copula-Based Outlier Detection. IEEE International Conference on Data Mining (ICDM), 2020.](https://arxiv.org/pdf/2009.09463.pdf)

## Model Evaluation
Anomaly scores output by the models have lognormal distributions with long tails as expected.
![Histograms of Models](https://github.com/aldente0630/fraud-detection-with-unsupervised-learning/blob/03d4bf187332dec8baef687e1fdf4fcafd24466c/images/hist_of_models.png)
  
![ROC Curves](https://github.com/aldente0630/fraud-detection-with-unsupervised-learning/blob/08f4d46f7bfe34df957027e9527441cd92fb96f6/images/roc_curves2.png)
  
![PR Curves](https://github.com/aldente0630/fraud-detection-with-unsupervised-learning/blob/03d4bf187332dec8baef687e1fdf4fcafd24466c/images/pr_curves.png)
