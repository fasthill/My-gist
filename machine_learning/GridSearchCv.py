'''
GridSearchCV 하이퍼 파라미터 학습과 최적화 # (https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)
-estimator : classifier, regressor, pipeline 등 
-param_grid : 튜닝을 위한 파라미터, 사용될 파라미터를 dictionary 형태 작성
-scoring : 예측 성능 평가 방법
-cv : 교차 검증 분할 개수
'''

pipe = Pipeline([('scaler', StandardScaler()),
                ('model', SVR(kernel='linear'))])

param_grid = [{'model__gamma': ['scale', 'auto'],
               'model__C': [1.0, 0.1, 0.01],
               'model__epsilon': [1.0, 0.1, 0.01]}]

gs = GridSearchCV(estimator=pipe,
                 param_grid=param_grid,
                 n_jobs=multiprocessing.cpu_count(),
                 scoring=None,  #  Classification:  'accuracy','f1', 'recall', 'precision', 'roc_auc' 등
                                #  Regression: 'neg_mean_squared_error','r2', 'max_error' 등
                                # https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
                 cv=5, verbose=1)

gs.fit(X, y)

print("Best Estimator: {}".format(gs.best_estimator_)) 
print("Best Parameters: {}".format(gs.best_params_))  # 최적 파라미터.
print('Best Score: {}, Best Index: {}'.format(gs.best_score_ , gs.best_index_))  # 교차검증된 점수를 보여줌.

model = gs.best_estimator_  # 최적의 파라미터로 모델 생성
predicted = model.predict(X_test)  # gs.predict()
