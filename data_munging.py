import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading from a comma seperated value file
df = pd.read_csv(r'C:\Users\Stanzoman\Documents\projects\train.csv')

#check missing values from the dataset
print(df.apply(lambda x: sum(x.isnull()),axis=0))