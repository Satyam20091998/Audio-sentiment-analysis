import json
import boto3

s3=boto3.resource("s3")
comprehend=boto3.client("comprehend")

def lambda_handler(event, context):
   
    if event:
        s3_object= event["Records"][0]["s3"]
        Bucket_Name=s3_object["bucket"]["name"]
        File_Name=s3_object["object"]["key"]
        
        print("now")
        obj = s3.Object(Bucket_Name, File_Name)
        data = json.load(obj.get()['Body'])
        paragraph=data["results"]["transcripts"][0]["transcript"]
        response=comprehend.batch_detect_sentiment(
            TextList=data_chunk(paragraph),
            LanguageCode="en")
        print(response)  
 
        
        
        final_response=average_sentiment(response)
        print(final_response)
        
        s3boto=boto3.client("s3")
        s3boto.put_object(Bucket="comprehende-output",Key=File_Name,Body=final_response)
        print("done")

def data_chunk(paragraph,chunk_size=5000):
    text=[]
    while paragraph:
        text.append(str(paragraph[:chunk_size]))
        paragraph=paragraph[chunk_size:]
        return text
        
def average_sentiment(response):
    positive,negative,neutral,mixed=0,0,0,0
  
    for scores in response["ResultList"]:
        positive += scores["SentimentScore"]["Positive"]
        negative += scores["SentimentScore"]["Negative"]
        neutral += scores["SentimentScore"]["Neutral"]
        mixed += scores["SentimentScore"]["Mixed"]
        
    total_rec=len(response["ResultList"])
    
    mapping={
        "POSITIVE":positive/total_rec,
        "NEGATIVE":negative/total_rec,
        "NEUTRAL":neutral/total_rec,
        "MIXED":mixed/total_rec,
    }
    
    response=json.dumps([{
        "Sentiment": max(mapping,key=mapping.get),
        "SentimentScore":{
            "Positive":mapping["POSITIVE"],
            "Negative":mapping["NEGATIVE"],
            "Neutral":mapping["NEUTRAL"],
            "Mixed":mapping["MIXED"],
            
        }
    }])
    return response
