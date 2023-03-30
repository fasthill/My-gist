
lgbm = None
lgbmgs = None

lgbm = lightgbm.LGBMClassifier(random_state=42)
    
search_space = {
        'learning_rate': (0.01, 1.0, 'log-uniform'),
        'num_leaves': (1, 100),      
        'max_depth': (0, 50),
        'min_child_samples': (0, 50),
        'max_bin': (100, 1000),
        'subsample': (0.01, 1.0, 'uniform'),
        'subsample_freq': (0, 10),
        'colsample_bytree': (0.01, 1.0, 'uniform'),
        'min_child_weight': (0, 10),
        'subsample_for_bin': (100000, 500000),
        'reg_lambda': (1e-9, 1000, 'log-uniform'),
        'reg_alpha': (1e-9, 1.0, 'log-uniform'),
        'scale_pos_weight': (1e-6, 500, 'log-uniform'),
        'n_estimators': (50, 100),
    }

bayes_cv_tuner = BayesSearchCV(
    estimator = lgbm,
    estimator = lgb.LGBMRegressor(
        objective='binary',
        metric='auc',
        n_jobs=1,
        verbose=0
    ),
    search_spaces = search_space,
    scoring = 'roc_auc',
    cv = StratifiedKFold(
        n_splits=3,
        shuffle=True,
        random_state=42
    ),
    n_jobs = 3,
    n_iter = ITERATIONS,   
    # n_iter = 200, means the model will be fit 200 times for different combination of parameter distributions specified * value specified of cv parameter 
    verbose = 0,
    refit = True,
    random_state = 42
)

# Fit the model
lgbm_result = bayes_cv_tuner.fit(X.values, y.values, callback=status_print)
