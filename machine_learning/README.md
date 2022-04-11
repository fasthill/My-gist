### ■ Scikit learn에서 fit하기전에 model을 reset해야 하나?
No! reset 필요 없음. 처음부터 다시 시작함. <br> 
기존 데이터 결과를 사용하려면, partial_fit()사용 <br>
[stack overflow 설명](https://stackoverflow.com/questions/49841324/what-does-calling-fit-multiple-times-on-the-same-model-do)

### ■ cross_val_score vs. cross_validate
The cross_validate function differs from cross_val_score in two ways -
* It allows specifying multiple metrics for evaluation.
* It returns a dict containing training scores, fit-times and score-times in addition to the test score. <br>
[stack overflow설명](https://datascience.stackexchange.com/questions/28441/what-is-the-difference-between-cross-validate-and-cross-val-score)

### ■ 표준화를 해야 하는 ML 모델
[읽어 볼 것 1 Good](https://www.listendata.com/2017/04/how-to-standardize-variable-in-regression.html) <br>
[읽어 볼 것 2](https://builtin.com/data-science/when-and-why-standardize-your-data)

### ■ sparse_categorical_crossentropy vs. categorical_crossentropy
* sparse_categorical_crossentropy : 정수로 되어 있는 target 값을 그대로 사용할 경우 사용
* categorical_crossentropy : target값이 one hot encoding으로 되어 있는 경우 사용

### ■ SimpleRNN, RNN, LSTM 등을 중복하여 사용할 경우
* 마지막 SimpleRNN을 제외하고 이전에 나오는 SimpleRNN의 parameter "return_sequences=True"를 반드시 지정해야 함.

### ■ How to use a cross-validated model for prediction?
* https://stats.stackexchange.com/questions/411290/how-to-use-a-cross-validated-model-for-prediction

### ■ stratify argument in train_test_split vs. StratifiedShuffleSplit
* [see this answer in stackoverflow](https://stackoverflow.com/questions/61299828/stratify-argument-in-train-test-split-vs-stratifiedshufflesplit)
* train_test_split에서 stratify argument사용은 1회에 한하여 사용됨. one time split 반면에
* StratifiedShuffleSplit class 사용은 cross validation에서 사용되면서 반복적인 batch_size로 나눌때마다 사용됨

### ■ [Codetutorial-Tensorflow](https://codetorial.net/tensorflow/index.html)
