import pandas as pd
import json
import numpy as np

# reformating data
page_topic = pd.read_csv("datadays2020_contest_public_dataset/page_topic.csv")
# print(page_topic.head())
new_page_topic_list = []
current_row = dict()
current_pageId = -1
for index, row in page_topic.iterrows():
    # print(row['pageId'], row['topicId'])
    if current_pageId != int(row['pageId']):
        new_page_topic_list.append(current_row)
        current_row = dict()
        current_pageId = row['pageId']
        current_row['pageId'] = current_pageId
        current_row[str(int(row['topicId']))] = row['confidence']
    else:
        current_row[str(int(row['topicId']))] = row['confidence']
new_page_topic = pd.read_json(str(json.dumps(new_page_topic_list)))
new_page_topic.fillna(value=0, inplace=True)
# print(new_page_topic.head())
# new_page_topic.to_csv(path_or_buf='a.csv', index=False)


# =======================================================================
# reformating data

user_page_view = pd.read_csv("datadays2020_contest_public_dataset/user_page_view.csv")
# reduction
user_page_view["timestamp"] = user_page_view["timestamp"].apply(lambda x: x >> 30)

new_user_page_view = (user_page_view.groupby(['pageId', 'userId'], sort=False).sum().reset_index())

# =================================================
# merging page views & page topics
result = pd.merge(new_page_topic, new_user_page_view, on='pageId', how='left')
# print(result.head())
# ===================================================
result.drop('pageId', axis=1, inplace=True)
print(result.describe())
for column in list(result.columns):
    if column != 'userId' and column != 'timestamp':
        print(column)
        print(result[column])
        print("***************")
        result[column] = np.multiply(result[column], result['timestamp'])
        print(result[column])
        print(result['timestamp'])
#         todo debug multiplying
print("____________________________________________________")
print(result.describe())

result = result.groupby('userId', as_index=False, sort=False)
