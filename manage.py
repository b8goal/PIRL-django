#!/usr/bin/env python
import os
import sys
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

def random_data(data):
    # 데이터 분할(train, test 데이터 7:3으로 - numpy->random)
    np.random.seed(seed=1234)

    # 0.7보다 작으면 True -> train 데이터, 아니면 False -> test 데이터
    msk = np.random.rand(data.shape[0]) < 0.7
    data_train = data[msk]
    data_test = data[~msk]

    # train/test 데이터의 목표변수/설명변수 지정
    data_train_y = data_train["당뇨병 의사 판정"]
    data_train_x = data_train.drop("당뇨병 의사 판정", axis=1, inplace=False)
    data_test_y = data_test["당뇨병 의사 판정"]
    data_test_x = data_test.drop("당뇨병 의사 판정", axis=1, inplace=False)

    # train데이터와 test데이터 크기
    print("train data X size: {}".format(data_train_x.shape))
    print("train data Y size: {}".format(data_train_y.shape))
    print("test data X size: {}".format(data_test_x.shape))
    print("test data Y size: {}".format(data_test_y.shape))
    # train data: 385, test data: 184
    return data_train_x,data_train_y,data_test_x,data_test_y

def Decision_Tree(data_train_x, data_train_y, data_test_x, data_test_y):
    tree_uncustomized = DecisionTreeClassifier(random_state=1234)
    tree_uncustomized.fit(data_train_x, data_train_y)
    return tree_uncustomized
    # 훈련 데이터 정확도

if __name__ == "__main__":
    '''
    
    data1 = pd.read_csv('./data/dataset_01.csv')
        
        data2 = pd.read_csv('./data/dataset_02.csv')
        data3 = pd.read_csv('./data/dataset_03.csv')
        data4 = pd.read_csv('./data/dataset_04.csv')
        data = data1.append(data2).append(data3).append(data4)
        print(data)
        
    data = data1
    data_train_x, data_train_y, data_test_x, data_test_y = random_data(data)
    Decision_Tree(data_train_x, data_train_y, data_test_x, data_test_y)

    depths = np.arange(1, 2)
    num_leafs = [1, 2]
    para_criterion = ["gini", "entropy"]
    param_grid = [{'criterion': para_criterion, 'max_depth': depths, 'min_samples_leaf': num_leafs}]

    gs = DecisionTreeClassifier(criterion="gini", max_depth=2, min_samples_leaf=2, random_state=1234)
    gs.fit(data_train_x, data_train_y)

    print("Accuracy on Training set:{:.3f}".format(gs.score(data_train_x,data_train_y)))
    print("Accuracy on Test set:{:3f}".format(gs.score(data_test_x,data_test_y)))
    '''

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
