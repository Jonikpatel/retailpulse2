import numpy as np
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
from statsmodels.tsa.statespace.sarimax import SARIMAX
from xgboost import XGBRegressor


def train_sarima(y_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)):
    model = SARIMAX(y_train, order=order, seasonal_order=seasonal_order, enforce_stationarity=False)
    return model.fit(disp=False)


def sarima_forecast(fitted_model, steps):
    forecast = fitted_model.get_forecast(steps=steps)
    return forecast.predicted_mean


def build_lag_features(y, lags=12):
    df = y.to_frame(name="target")
    for lag in range(1, lags + 1):
        df[f"lag_{lag}"] = df["target"].shift(lag)
    df.dropna(inplace=True)
    X = df.drop(columns=["target"])
    y_new = df["target"]
    return X, y_new


def train_xgboost(X_train, y_train):
    model = XGBRegressor(
        n_estimators=300,
        max_depth=5,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="reg:squarederror",
        random_state=42,
    )
    model.fit(X_train, y_train)
    return model


def regression_metrics(y_true, y_pred):
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    mae = float(mean_absolute_error(y_true, y_pred))
    mape = float(mean_absolute_percentage_error(y_true, y_pred))
    return {"rmse": rmse, "mae": mae, "mape": mape}
