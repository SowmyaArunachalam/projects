import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the dataset
file_path = 'clean_social.csv'
data = pd.read_csv(file_path)

# Preprocess the data
le = LabelEncoder()

data['gender'] = le.fit_transform(data['gender'])
data['education'] = le.fit_transform(data['education'])
data['profession'] = le.fit_transform(data['profession'])
data['workDuration'] = data['workDuration'].str.extract('(\d+)').astype(int)
data['typeSocial'] = le.fit_transform(data['typeSocial'])
data['useSocial'] = le.fit_transform(data['useSocial'])
data['productivity'] = le.fit_transform(data['productivity'])  # Target variable

# Define features and target
X = data.drop(columns=['id', 'productivity'])
y = data['productivity']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)

