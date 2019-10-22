from tkinter import *
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn import model_selection
from statistics import mode
#Metric calculations
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_absolute_error, accuracy_score
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split

first = [ 'lacrimation', 'abnormal_salivation', 'nasal_discharge', 'lameness',
            'firm_nodules_on_the_skin','enlarged_lymph_nodes', 'swollen_sore_legs', 'loss_of_appetite', 'eyes_nose_discharge', 'drop_in_milk',
            'weight_loss', 'blisters_in_mouth_and_feet','blisters_on_teats', 'dullness', 'shivering','rough_coat',
            'enlarged_parotid_gland','reluctant_to_move', 'anaemia', 'jaundice', 'severe_diarrhoea', 'swelling_in_the_neck',
            'cloudiness_of_the_eyes', 'breathing_difficulty', 'cyanosis_of_the_tongue', 'swelling_of_tongue_and_face']
disease = ['lumpy skin', 'foot and mouth', 'theileriases', 'babesiosis', 'anaplasmosis', 'anthrax', 'blue tongue']
second = []
#set seed
rand_seed = 221
np.random.seed = rand_seed
#loading dataset
tr = pd.read_csv("CattleDiseases.csv") #training data
'''
tr.replace({'prognosis': {'lumpy skin': 0, 'foot and mouth': 1, 'theileriases': 2, 'babesiosis': 3, 'anaplasmosis': 4,
                          'anthrax': 5, 'blue tongue': 6}}, inplace=True)
'''
#Import single models
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR, SVC
from sklearn.neighbors import KNeighborsRegressor,KNeighborsClassifier

#Classification models
log_cf = LogisticRegression(solver='lbfgs', random_state=rand_seed)
svc_cf = SVC(gamma='scale', random_state=rand_seed)
knn_cf = KNeighborsClassifier()
dtree_cf = DecisionTreeClassifier()
randomforest_cf = RandomForestClassifier()
gnb_cf = GaussianNB()
classification_models = [log_cf, svc_cf, knn_cf, dtree_cf, randomforest_cf, gnb_cf]

'''
#Regression models
linear_reg = LinearRegression()
svr_reg = SVR(gamma='scale')
knn_reg = KNeighborsRegressor()
regression_models = [linear_reg, svr_reg, knn_reg]
'''

# Define a function to standardize the data set
def standardize_data(tr):
    scaler = RobustScaler()
    data = scaler.fit_transform(tr)
    return data


# Create a function to split our data into train and validation set for both task

def get_split_data(features, target_name=None):
    ## Get the target column
    target = features[target_name]
    ## Drop the target from the data
    temp_data = features.drop(target_name, axis=1)
    temp_data = standardize_data(temp_data)

    # split data
    X_train, X_val, y_train, y_val = train_test_split(temp_data, target, test_size=0.1)
    return (X_train, X_val, y_train, y_val)


def get_mae(pred, true_value):
    return mean_absolute_error(true_value, pred)


def get_acc(pred, true_value):
    return accuracy_score(true_value, pred) * 100


# A Function to train and cross validate a model
def model_train(model, features=None, target_name=None, nfolds=10, task='class'):
    ## Get the target column
    target = features[target_name]
    ## Drop the target from the data
    temp_data = features.drop(target_name, axis=1)
    temp_data = standardize_data(temp_data)

    if task == 'reg':
        score = -1 * (cross_val_score(model, temp_data, target, cv=nfolds, scoring='neg_mean_absolute_error'))
        print("Mean Absolute Error of {} is {}".format(model.__class__.__name__, round(score[0], 4)))
        print("-------------------------------------")

    else:
        score = cross_val_score(model, temp_data, target, cv=nfolds, scoring='accuracy')
        print("Accuracy of {} is {} %".format(model.__class__.__name__, round(score[0] * 100)))
        print("-------------------------------------")
# Classification
for model in classification_models:
    model_train(model, features=tr, target_name='prognosis')
#Max voting
#The Max Voting is similar to averaging except it is used for classification problems.
# In max voting as the name implies, we train multiple models, make predictions
# and then take the maximum/modal/most popular class as the predicted class.

# get the data sets
X_train, X_val, y_train, y_val = get_split_data(tr, target_name='prognosis')

# fit single models
log_cf.fit(X_train, y_train)
knn_cf.fit(X_train, y_train)
svc_cf.fit(X_train, y_train)
dtree_cf.fit(X_train, y_train)
randomforest_cf.fit(X_train, y_train)
gnb_cf.fit(X_train, y_train)

# make predictions with trained models
pred1 = log_cf.predict(X_val)
pred2 = knn_cf.predict(X_val)
pred3 = svc_cf.predict(X_val)
pred4 = dtree_cf.predict(X_val)
pred5 = randomforest_cf.predict(X_val)
pred6 = gnb_cf.predict(X_val)

# Take max voting as final prediction
maxpred = []

for i in range(0, len(X_val)):
    # calculate the mode and append to maxpred vector
    maxpred.append(mode([pred1[i], pred2[i], pred3[i], pred4[i], pred5[i], pred6[i]]))

print("Logistic Regression Model")
print(get_acc(pred1, y_val))
print("KNN Classifier Model")
print(get_acc(pred2, y_val))
print("SVR Classifier Model")
print(get_acc(pred3, y_val))
print("DecisionTreeClassifier Model")
print(get_acc(pred4, y_val))
print("RandomForestClassifier Model")
print(get_acc(pred5, y_val))
print("NaiveBayes Using Gaussian Model")
print(get_acc(pred6, y_val))

print("Max Voting Model")
print(get_acc(np.array(maxpred), y_val))

#Advanced Ensemble Techniques
#Bagging

#Bagging and Boosting models for both classification and regression problems
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, BaggingRegressor
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor

#bagging algorithms for classification
rand_forest_cf = RandomForestClassifier(n_estimators=100, random_state=rand_seed)
extra_tree_cf = ExtraTreesClassifier(n_estimators=100, random_state=rand_seed)
#We use svc as our base model for bagging
bagging_meta_cf = BaggingClassifier(svc_cf, n_estimators=10, random_state=rand_seed)

#get data for classification task
X_train, X_val, y_train, y_val = get_split_data(tr, target_name='prognosis')

#Train and fit these models
rand_forest_cf.fit(X_train, y_train)
extra_tree_cf.fit(X_train, y_train)
bagging_meta_cf.fit(X_train, y_train)

#check their performance
print("ACC of Random Forest is : ", get_acc(rand_forest_cf.predict(X_val), y_val))
print("ACC of Extra Trees is : ", get_acc(extra_tree_cf.predict(X_val), y_val))
print("ACC of Bagging estimator is : ", get_acc(bagging_meta_cf.predict(X_val), y_val))

for x in range(0, len(first)):
    second.append(0)
#psymptoms = []
psymptoms = ['symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5', 'symptom6']
for k in range(0, len(first)):
    for z in psymptoms:
        if (z == first[k]):
            second[k] = 1
inputtest = [second]
predict = rand_forest_cf.predict(inputtest)
predicted = predict[0]

h = 'no'
for a in range(0, len(disease)):
    if (predicted == a):
        h = 'yes'
        break
'''
if (h == 'yes'):
    t1.delete("1.0", END)
    t1.insert(END, disease[a])
else:
    t1.delete("1.0", END)
    t1.insert(END, "Not Found")
'''

import joblib

joblib.dump(model, 'model.pkl')

user_input = {'lacrimation': 1, 'abnormal_salivation': 0, 'nasal_discharge': 0, 'lameness': 1,'firm_nodules_on_the_skin': 1,
              'enlarged_lymph_nodes': 0, 'swollen_sore_legs': 1, 'loss_of_appetite': 0, 'eyes_nose_discharge': 1, 'drop_in_milk': 0,
              'weight_loss': 0, 'blisters_in_mouth_and_feet': 0,'blisters_on_teats': 0, 'dullness': 1, 'shivering': 0,'rough_coat': 0,
              'enlarged_parotid_gland': 1,'reluctant_to_move': 0, 'anaemia': 0, 'jaundice':0, 'severe_diarrhoea': 1, 'swelling_in_the_neck': 0,
              'cloudiness_of_the_eyes': 0, 'breathing_difficulty': 0, 'cyanosis_of_the_tongue': 0, 'swelling_of_tongue_and_face': 0}

def input_to_one_hot(data):
    # initialize the target vector with zero values
    enc_input = np.zeros(26)
    # set the numerical input as they are
    enc_input[0] = data['lacrimation']
    enc_input[1] = data['abnormal_salivation']
    enc_input[2] = data['nasal_discharge']
    enc_input[3] = data['lameness']
    enc_input[4] = data['firm_nodules_on_the_skin']
    enc_input[5] = data['enlarged_lymph_nodes']
    enc_input[6] = data['swollen_sore_legs']
    enc_input[7] = data['loss_of_appetite']
    enc_input[8] = data['eyes_nose_discharge']
    enc_input[9] = data['drop_in_milk']
    enc_input[10] = data['weight_loss']
    enc_input[11] = data['blisters_in_mouth_and_feet']
    enc_input[12] = data['blisters_on_teats']
    enc_input[13] = data['dullness']
    enc_input[14] = data['shivering']
    enc_input[15] = data['rough_coat']
    enc_input[16] = data['enlarged_parotid_gland']
    enc_input[17] = data['reluctant_to_move']
    enc_input[18] = data['anaemia']
    enc_input[19] = data['jaundice']
    enc_input[20] = data['severe_diarrhoea']
    enc_input[21] = data['swelling_in_the_neck']
    enc_input[22] = data['cloudiness_of_the_eyes']
    enc_input[23] = data['breathing_difficulty']
    enc_input[24] = data['cyanosis_of_the_tongue']
    enc_input[25] = data['swelling_of_tongue_and_face']

    return enc_input
print(input_to_one_hot(user_input))
a = input_to_one_hot(user_input)
pred = model.predict([a])
predicted = pred[0]
print(predicted)


