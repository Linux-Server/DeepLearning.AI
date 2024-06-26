import pandas as pd

housing_data = pd.read_csv("./datasets/melb_data.csv")

housing_data.describe()