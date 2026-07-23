# DecodeLabs AI Internship - Project 2
# Data Classification Using K-Nearest Neighbors (KNN)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Step 2: Understand the dataset
print("First 5 Rows of Dataset:")
df = pd.DataFrame(X, columns=iris.feature_names)
print(df.head())

print("\nFlower Classes:")
print(iris.target_names)

print("\nDataset Shape:")
print(X.shape)

# Step 3: Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Step 4: Apply the KNN classification algorithm and train the model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Step 5: Predict the test data
predictions = model.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, predictions)

print("\nPredicted Values:")
print(predictions)

print("\nActual Values:")
print(y_test)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
