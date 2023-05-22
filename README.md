![audio_ananlysis](https://user-images.githubusercontent.com/92753984/211182576-6ee0c82a-fe3d-495c-bb8b-a77e54b993f0.png)

## Audio Sentiment Analysis


## Steps to setup projects

1.Create a lamda function using boto 3 which will consume mp3 file from s3 bucket and will transcript and will save in JSON file.
2.Create another lambda function which will consume transcripted file and will pass the data in comprehend to analyse the data.
3.Then analysed data will get loaded into the s3 bucket from there we will pull in snowflake using snowpipe.
4.then will use the data to visualize the analysis
