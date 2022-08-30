### Cleaning(or Cleansing) vs. Data Wrangling
* Data cleaning, also referred to as data cleansing, is the process of finding and correcting <span style='color:red'>inaccurate data</span> from a particular data set or data source. example)  identifying duplicate records, filling empty fields and fixing structural errors
* Data cleaning focuses on removing inaccurate data from your data set whereas data wrangling focuses on transforming the data’s format, typically by converting “raw” data into another format more suitable for use. 
* Data wrangling, also referred to as data munging, is the process of converting and mapping data from one raw format into another.
* Data cleaning enhances the data’s accuracy and integrity while wrangling prepares the data structurally for modeling. 
* Traditionally, data cleaning would be performed before any practices of data wrangling being applied.
* 
     <img src="https://miro.medium.com/max/1400/1*32j2A1EFgqDHUcNTQackwA.png" width="700"/>
* [read article1](https://www.inzata.com/data-wrangling-vs-data-cleaning-whats-the-difference/)
* [read article2](https://blog.devgenius.io/data-cleaning-vs-data-wrangling-3577827e28a7)

### Master efficient workflows for cleaning real-world, messy data.
* [kaggle Data Cleaning](https://www.kaggle.com/learn/data-cleaning)

### Data Wrangling 
* 처음부터 끝까지 데이터 처리 과정을 포함한다고 설명함. 세세한 정의는 각각 해석이 틀린다는 것을 알 수 있음.
* includes all (cleaning, enriching, validating)....
* [Harvard Business School](https://online.hbs.edu/blog/post/data-wrangling)

### Feature Reduction (Feature Selection + Feature Extraction)
* Feature Selection
  * feature selection, also known as variable selection, attribute selection or variable subset selection, is the process of selecting a subset of relevant features (variables, predictors) for use in model construction. <br> 
  * 현재 데이터 세트에서 데이터를 가공하지 않고 필요없는 데이터를 제외시키는 것. 필요한 데이터만 남기는 것. <br.
  * 관련없거나 중복되는 feature들을 filtering하여 간결한 subset를 생성하는 과정. 

    <img src="https://miro.medium.com/max/1388/0*D_jQ5yBsvCZjEYIW" width="500"/>
    
* Feature Extraction
  * 기존 feature들을 조합하여 새로운 feature를 생성하는 것.
  * 차원 축소 이용. 고차원 feture를 저차원 feature로 변환

    <img src="https://github.com/fasthill/My-gist/blob/main/data/picture/feature_extraction.JPG" width="500"/>

### Feature Transformation, Feature Engineering
* Feature Transformation:  which modifies the data, to make it more understandable for the machine. (예: 문자를 숫자로 변환, cleaning + wrangling)
     * Note that we don’t create new columns from the current ones; This is where Transformation differs from Feature Engineering.
* Feature Engineering: uses already modified features to create new ones, which will make it easier for any Machine Learning algorithm to understand and learn any pattern.
* Feature Engineering은 머신러닝 알고리즘을 작동하기 위해 데이터에 대한 도메인 지식을 활용하여 특징(Feature)를 만들어내는 과정. 머신러닝 모델을 위한 데이터 테이블의 컬럼(특징)을 생성하거나 선택하는 작업을 의미. Feature Engineering은 모델 성능에 미치는 영향이 크기 때문에 머신러닝 응용에 있어서 굉장히 중요한 단계이며, 전문성과 시간과 비용이 많이 드는 작업


### Outlier Treatement
* [Detecting And Treating Outliers In Python — Part 1](https://towardsdatascience.com/detecting-and-treating-outliers-in-python-part-1-4ece5098b755)
* [Detecting And Treating Outliers In Python — Part 2](https://towardsdatascience.com/detecting-and-treating-outliers-in-python-part-2-3a3319ec2c33)
* [Detecting and Treating Outliers In Python — Part 3](https://towardsdatascience.com/detecting-and-treating-outliers-in-python-part-3-dcb54abaf7b0)
* [5 Outlier Detection Techniques that every “Data Enthusiast” Must Know](https://towardsdatascience.com/5-outlier-detection-methods-that-every-data-enthusiast-must-know-f917bf439210)
* [Cleaning up Data from Outliers](https://www.pluralsight.com/guides/cleaning-up-data-from-outliers)
* [How to Scale Data With Outliers for Machine Learning](https://machinelearningmastery.com/robust-scaler-transforms-for-machine-learning/)


### Missing Value Treatement
* [A Better Way to Handle Missing Values in your Dataset: Using IterativeImputer (PART I)](https://towardsdatascience.com/a-better-way-to-handle-missing-values-in-your-dataset-using-iterativeimputer-9e6e84857d98)
* [A Better Way to Handle Missing Values in your Dataset: Using IterativeImputer on the Stock Market Data (PART II)](https://levelup.gitconnected.com/a-better-way-to-handle-missing-values-in-your-dataset-using-iterativeimputer-on-the-stock-market-dbbb5d4ef458)

### Normal Distribution
* [How to Transform Data to Better Fit The Normal Distribution](https://machinelearningmastery.com/how-to-transform-data-to-fit-the-normal-distribution/)
* [How do I know if my data have a normal distribution?](https://www.graphpad.com/support/faq/testing-data-for-normal-distrbution/)
* [6 ways to test for a Normal Distribution — which one to use?](https://towardsdatascience.com/6-ways-to-test-for-a-normal-distribution-which-one-to-use-9dcf47d8fa93)
