import pandas as pd
import json
import numpy as np
# reformating data
page_topic = pd.read_csv("datadays2020_contest_public_dataset/page_topic.csv")
print(page_topic.head())
new_page_topic =[]
current_row = dict()
current_pageId = -1
for index, row in page_topic.iterrows():
    print(row['pageId'], row['topicId'])
    if current_pageId != int(row['pageId']):
        new_page_topic.append(current_row)
        current_row = dict()
        current_pageId = row['pageId']
        current_row['pageId'] = current_pageId
        current_row[str(int(row['topicId']))] = row['confidence']
    else:
        current_row[str(int(row['topicId']))] = row['confidence']
dataform = pd.read_json(str(json.dumps(new_page_topic)))
dataform.fillna(value=0, inplace=True)
print(dataform.head())
dataform.to_csv(path_or_buf='a.csv', index=False)



# =======================================================================





# result = pd.merge(ad, ad_image, on='adId')
#
# print(result.head())
