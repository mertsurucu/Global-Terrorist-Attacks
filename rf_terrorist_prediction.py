from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
import numpy as np

# loads the data from npy
data = np.load('train_data.npy')
data_label = np.load('train_data_label.npy')

# encode the string features into int type
# and reshape the data 1D to 2D with 8 features in each row
le = preprocessing.LabelEncoder()
data = le.fit_transform(data)
data = np.reshape(data, (-1, 8))

count = 0
classes = []
i = 0
while i < len(data_label):
    if data_label[i] not in classes:
        classes.append(data_label[i])
        count += 1
    i += 1
print(count, "Terrorist Groups(Classes)")
print("Terrorist Group(Class) Names: ", classes)
generalOverallAccuracy = 0

th_fold = 0
# K-fold splits into 10 and shuffles the indexes
split_size = 10
kf = KFold(n_splits=split_size, shuffle=True)
kf.get_n_splits(data)
for train_index, test_index in kf.split(data):
    th_fold += 1
    # print("TRAIN:", train_index, "TEST:", test_index)
    train_data, test_data = data[train_index], data[test_index]
    train_label, test_label = data_label[train_index], data_label[test_index]

    # Create a random forest Classifier. By convention, clf means 'Classifier'
    clf = RandomForestClassifier(n_estimators=2)
    # Train the Classifier to take the training features and learn how they relate to the training(the species)
    clf.fit(train_data, train_label)
    # makes a list to get each accuracy
    prediction = clf.predict(test_data)
    accuracy_counter = 0
    for each in range(len(prediction)):
        if prediction[each] == test_label[each]:
            accuracy_counter += 1
    generalOverallAccuracy += accuracy_counter
    print("Accuracy for", th_fold, ". fold", accuracy_counter / len(prediction))
print("Overall Accuracy", generalOverallAccuracy / len(data_label))
