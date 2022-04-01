### Data Wrangling vs. Cleaning(or Cleansing)
* Data wrangling, also referred to as data munging, is the process of converting and mapping data from one raw format into another.
* Data cleaning, also referred to as data cleansing, is the process of finding and correcting <span style='color:red'>inaccurate data</span> from a particular data set or data source. example)  identifying duplicate records, filling empty fields and fixing structural errors
* Data cleaning focuses on removing inaccurate data from your data set whereas data wrangling focuses on transforming the data’s format, typically by converting “raw” data into another format more suitable for use. 
* Data cleaning enhances the data’s accuracy and integrity while wrangling prepares the data structurally for modeling. 
* Traditionally, data cleaning would be performed before any practices of data wrangling being applied.
* [read](https://www.inzata.com/data-wrangling-vs-data-cleaning-whats-the-difference/)

### Master efficient workflows for cleaning real-world, messy data.
* [kaggle Data Cleaning](https://www.kaggle.com/learn/data-cleaning)

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
