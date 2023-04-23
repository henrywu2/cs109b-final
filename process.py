import pandas as pd

business = pd.read_json('data/yelp_dataset/yelp_academic_dataset_business.json', lines=True)
max_city = business['city'].value_counts().idxmax()
business = business.loc[(business['city'] == max_city) & (business['categories']).str.contains('Restaurants')]
print(business)

chunk_size = 1000000
batch_no = 1
review = []
for chunk in pd.read_json('data/yelp_dataset/yelp_academic_dataset_review.json', lines=True, chunksize=chunk_size):
    chunk = chunk.loc[chunk['business_id'].isin(business['business_id'])]
    review.append(chunk)
    print(review[-1].shape[0])
    chunk.to_csv('review'+str(batch_no)+'.csv',index=False)
    batch_no+=1
reviews = pd.concat(review)

chunk_size = 100000
batch_no=1
users = []
for chunk in pd.read_json('data/yelp_dataset/yelp_academic_dataset_user.json', lines=True, chunksize=chunk_size):
    chunk = chunk.loc[chunk['user_id'].isin(reviews['user_id'])]
    users.append(chunk)
    print(users[-1].shape[0])
    chunk.to_csv('user'+str(batch_no)+'.csv',index=False)
    batch_no+=1