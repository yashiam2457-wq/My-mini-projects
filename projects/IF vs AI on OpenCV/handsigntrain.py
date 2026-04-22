import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

FILE = "C:\\Users\\Loq\\Documents\\programs\\myprojects\\image_dataset.csv"
data = pd.read_csv(FILE, header=None).dropna()

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

print("Feature size:", X.shape[1])
counts = y.value_counts()
valid = counts[counts >= 2].index

X = X[y.isin(valid)]
y = y[y.isin(valid)]
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)
model = RandomForestClassifier(
    n_estimators=500,
    max_depth=25,
    min_samples_split=5,
    min_samples_leaf=2,
    n_jobs=-1,
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", model.score(X_test, y_test))
print("\nReport:\n", classification_report(y_test, y_pred))

print("Model expects:", model.n_features_in_)
if model.score(X_test, y_test) >= 0.80:
    joblib.dump(model, "hand_sign_model-2.pkl")
    print("Model saved!")
