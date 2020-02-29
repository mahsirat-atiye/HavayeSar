import pandas as pd
import numpy as np
ad = pd.read_csv("datadays2020_contest_public_dataset/ad.csv")
ad_image = pd.read_csv("datadays2020_contest_public_dataset/ad_image.csv")

result = pd.merge(ad, ad_image, on='adId')

print(result.head())