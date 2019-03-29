import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

movie_data = pd.read_csv(r"movie_metadata.csv")

# lets see the data frame and see number of rows and column
print(movie_data.shape)


