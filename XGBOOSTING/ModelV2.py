import numpy as np
import xgboost as xgb
import pickle
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split

def find_best_params(X_train, y_train, n_splits=10):
    params = {
        'objective': 'reg:squarederror',
        'n_estimators': 500,
        'max_depth': 6,
        'learning_rate': 0.1,
        'min_child_weight': 1,
        'subsample': 0.8,
        'colsample_bytree': 0.8
    }

    grid_search_params = {
        'max_depth': [4, 5, 6, 7, 8],
        'learning_rate': [0.05, 0.1, 0.2],
        'min_child_weight': [1, 3, 5],
        'subsample': [0.6, 0.7, 0.8, 0.9],
        'colsample_bytree': [0.6, 0.7, 0.8, 0.9]
    }

    model = xgb.XGBRegressor(**params)
    grid_search = GridSearchCV(estimator=model,
                               param_grid=grid_search_params,
                               scoring='neg_mean_squared_error',
                               cv=n_splits,
                               verbose=1)

    grid_search.fit(X_train, y_train)
    return grid_search.best_params_

def xgboostingmodel(datamodel,test_size=0.1, n_splits=10):

    vardep            = 'valor'
    datamodel[vardep] = np.log(datamodel[vardep])
    X = datamodel.drop(vardep, axis=1)
    y = datamodel[vardep]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    best_params = find_best_params(X_train, y_train, n_splits=n_splits)
    model = xgb.XGBRegressor(**best_params)
    model.fit(X_train, y_train)

    scores = cross_val_score(model, X_train, y_train, cv=n_splits, scoring='neg_mean_squared_error')
    rmse = np.sqrt(-scores)
    print("RMSE: ", rmse.mean())
    
    return model