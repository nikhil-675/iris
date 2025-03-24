import pandas as pd
from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

OUTPUT_PATH = 'src/utils/iris_pipeline.pkl'

# Load data
iris = load_iris(as_frame=True)
df = iris.frame

X = df.drop(columns=['target'])
y = df['target']

# Define numeric preprocessing pipeline
numeric_features = X.columns.tolist()
numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])

# ColumnTransformer
preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features)
])

# Complete pipeline: preprocessing + model
clf_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

# Train model
clf_pipeline.fit(X, y)

# Save the pipeline
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
joblib.dump(clf_pipeline, OUTPUT_PATH)

print(f"Pipeline trained and saved to {OUTPUT_PATH}")
