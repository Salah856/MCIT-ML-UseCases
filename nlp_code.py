import boto3
import json

df = pd.read_csv(path_to_csv)
df.info()
reviews = df['reviews.txt'][:10000]
reviews[2]

ln = len(reviews) # 10000 text
comprehend = boto3.client(service_name='comprehend', region_name=boto3.Session().region_name)
print('Calling DetectSentiment')

# loop over 10000 text then apply comprehend api 
for i in range(ln):
   print(json.dumps(comprehend.detect_sentiment(Text=reviews[i], LanguageCode='en'), sort_keys=True, indent=4))
      
       
print('ending calling')

