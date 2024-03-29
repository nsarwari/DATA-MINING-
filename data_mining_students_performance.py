# -*- coding: utf-8 -*-
"""data mining - students performance

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TT97bfTmq4jpmNE5ifWjsDqMBtezjwpE
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import mean_squared_error, accuracy_score

dataset_path = 'study_performance.csv'

data = pd.read_csv(dataset_path)

for column in categorical_columns:  data[column] = LabelEncoder().fit_transform(data[column])

categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

data['math_performance'] = pd.cut(data['math_score'], bins=[0, 60, 75, 100], labels=['Low', 'Medium', 'High'], right=False)

X_knn = data.drop(['math_score', 'reading_score', 'writing_score', 'math_performance'], axis=1)

y_knn = data['math_score']

X_train_knn, X_test_knn, y_train_knn, y_test_knn = train_test_split(X_knn, y_knn, test_size=0.2, random_state=42)

X_nb = X_knn

y_nb = data['math_performance']

X_train_nb, X_test_nb, y_train_nb, y_test_nb = train_test_split(X_nb, y_nb, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_knn_scaled = scaler.fit_transform(X_train_knn)
X_test_knn_scaled = scaler.transform(X_test_knn)

knn_regressor = KNeighborsRegressor(n_neighbors=5)

knn_regressor.fit(X_train_knn_scaled, y_train_knn)

y_pred_knn = knn_regressor.predict(X_test_knn_scaled)

mse_knn = mean_squared_error(y_test_knn, y_pred_knn)

print(f'KNN MSE: {mse_knn}')

"""NB model"""

missing_values = data.isnull().sum()



print(missing_values)

from sklearn.preprocessing import StandardScaler



nb_classifier = CategoricalNB()

print(data.isnull().sum())

print(data[data.isnull().any(axis=1)])

data_clean = data.dropna()

data_filled = data.fillna('missing')

data['math_performance'] = data['math_performance'].astype('object')



categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

data_selected = data_study_performance[categorical_columns]

for col in categorical_columns:
    data_study_performance[col] = data_study_performance[col].astype('category')

import pandas as pd

data_study_performance = pd.read_csv('study_performance.csv')

import pandas as pd

data_study_performance = pd.read_csv('study_performance.csv')

print(data_study_performance.head())

data_selected = data_study_performance[categorical_columns]

if  y_train_nb.dtype.name == 'category':
    y_train_nb = y_train_nb.cat.add_categories(['Missing'])
if y_test_nb.dtype.name == 'category':
    y_test_nb = y_test_nb.cat.add_categories(['Missing'])

y_train_nb = y_train_nb.fillna('Missing')
y_test_nb = y_test_nb.fillna('Missing')

nb_classifier = CategoricalNB()
nb_classifier.fit(X_train_nb, y_train_nb)

y_pred_nb = nb_classifier.predict(X_test_nb)
accuracy_nb = accuracy_score(y_test_nb, y_pred_nb)
print(f'NB Accuracy: {accuracy_nb}')



