### Scikit learn에서 fit하기전에 model을 reset해야 하나?
No! reset 필요 없음. 처음부터 다시 시작함. <br> 
기존 데이터 결과를 사용하려면, partial_fit()사용 <br>
[stack overflow 설명](https://stackoverflow.com/questions/49841324/what-does-calling-fit-multiple-times-on-the-same-model-do)

### cross_val_score vs. cross_validate
The cross_validate function differs from cross_val_score in two ways -
* It allows specifying multiple metrics for evaluation.
* It returns a dict containing training scores, fit-times and score-times in addition to the test score. <br>
[stack overflow설명](https://datascience.stackexchange.com/questions/28441/what-is-the-difference-between-cross-validate-and-cross-val-score)

### 표준화를 해야 하는 ML 모델
[읽어 볼 것 1 Good](https://www.listendata.com/2017/04/how-to-standardize-variable-in-regression.html)
[읽어 볼 것 2](https://builtin.com/data-science/when-and-why-standardize-your-data)
