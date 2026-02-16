import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv(r"Data\gas_prices.csv")

models = {}



# IMPORTANT FIX (2D)
x = df[['Year']]

for country in df.columns[1:]:

    temp_df = df[['Year', country]].dropna()

    x = temp_df[['Year']]
    y = temp_df[country]

    model = LinearRegression()
    model.fit(x, y)

    models[country] = model


pickle.dump(models, open("country_models.pkl", "wb"))

print("All countries are running successfully")
