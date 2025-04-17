from holoviews.plotting.bokeh.styles import font_size
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target
df['target_name'] = df['target'].map(dict(enumerate(wine.target_names)))

# Features and labels
x = df[wine.feature_names]
y = df['target'] # Three classes 0, 1, 2

# Feature Standardization
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x) # Each feature has a mean of 0 and sd of 1

# Splitting the data into train and test
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size = 0.2, random_state = 42, stratify = y) # stratify ensure equal class distribution in train and test models
# random_state is used for reproducibility

# Logistic Regression
model = LogisticRegression(max_iter = 1000) # To avoid convergence issue
model.fit(x_train, y_train)

# Prediction
y_pred = model.predict(x_test)

# Performance Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Feature importance
feature_importance_lr = pd.Series(abs(model.coef_[0]), index=wine.feature_names)
feature_importance_lr = feature_importance_lr.sort_values(ascending=False)

sns.set(style='white', font_scale=1.2, rc={"figure.dpi": 150})
plt.figure(figsize=(12, 10))
feature_importance_lr.plot(kind='bar', color='skyblue')
plt.title('Feature Importance from Logistic Regression Coefficients', fontsize=14, fontweight='bold')
plt.xlabel('Features', fontsize=12, fontweight='bold')
plt.ylabel('Absolute Coefficient Value', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("wine_feature_importance.png", dpi=300, bbox_inches='tight')


# Confusion matrix visualization
conf_mat = confusion_matrix(y_test, y_pred)
sns.set(style='white', font_scale=1.2, rc={"figure.dpi": 150})
plt.figure(figsize=(12, 10))
sns.heatmap(conf_mat, annot=True, cmap='Blues', fmt='g', xticklabels=wine.target_names, yticklabels=wine.target_names)
plt.xlabel("Predicted", fontsize = 12, fontweight = 'bold')
plt.ylabel("Actual", fontsize = 12, fontweight = 'bold')
plt.title("Confusion Matrix - Logistic Regression", fontsize = 14, fontweight = 'bold')
plt.tight_layout()
plt.savefig("wine_confusion_matrix.png", dpi=300, bbox_inches='tight')
plt.show()
