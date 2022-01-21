# import cv2
# import numpy as np
# import face_recognition
import pandas as pd

path = 'Data\Experience_Salaries.csv'
data = pd.read_csv(path)
print(data.describe())
print(data.head())
print("Shape of the data:", data.shape)
# mean = data.itmBrand.mean()
# mean = data['itmBrand'].mean()
# print(mean)
data.columns
