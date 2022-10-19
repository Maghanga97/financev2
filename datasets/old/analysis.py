import pandas as pd 
import matplotlib.pyplot as plt
 
def extract_data(file):
	dataset = pd.read_excel(file)
	dataset.dropna(inplace=True)
	return dataset

print(extract_data())