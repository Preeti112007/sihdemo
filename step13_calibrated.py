# C(x) = [f(x)-q, f(x)+q] | q = (1-alpha) quantile of |y - f(x)|
from xgboost import XGBRegressor
from mapie.regression import MapieRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv("error_database.csv")
X, y = df[["forecast"]], df["error"]
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_calib, X_test, y_calib, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
model = XGBRegressor(n_estimators=100, max_depth=4)
model.fit(X_train, y_train)
mapie = MapieRegressor(estimator=model, alpha=0.1) # 90% confidence
mapie.fit(X_calib, y_calib)
pred, interval = mapie.predict(X_test, alpha=0.1)
print(f"Pred {pred[0]:.2f} Interval {interval[0]} with 90% guarantee")