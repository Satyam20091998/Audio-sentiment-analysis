# Audio Sentiment Analysis

## Project Overview

This project focuses on analyzing the sentiment of audio data using various AWS services. It processes audio files, transcribes them into text, and performs sentiment analysis on the transcripts. The results are stored and visualized for further insights. The integration of AWS Lambda, Comprehend, and Snowflake ensures scalability and efficient data processing.

## Objectives

- **Audio Transcription**: Convert audio files (MP3) into textual transcripts using AWS Lambda.
- **Sentiment Analysis**: Leverage AWS Comprehend to analyze sentiment from the transcribed data.
- **Storage & Retrieval**: Store processed data in an S3 bucket and use Snowpipe to ingest into Snowflake for analysis.
- **Visualization**: Present the sentiment analysis results for insights into audio sentiment trends.

## Technology Stack

- **AWS Lambda**: For automating audio transcription and processing.
- **AWS S3**: Storage of audio files and processed results.
- **AWS Comprehend**: Sentiment analysis on the transcribed text.
- **Snowflake**: Data warehousing for processed results, integrated via Snowpipe.
- **Python**: Primary programming language for scripting and automation.

## Architecture Diagram

![Architecture Diagram](https://user-images.githubusercontent.com/92753984/211182576-6ee0c82a-fe3d-495c-bb8b-a77e54b993f0.png)

_Include a detailed architecture diagram of the workflow, highlighting AWS services and the data flow between them._

## Project Workflow

1. Upload audio files to an S3 bucket.
2. AWS Lambda triggers transcription of the audio files into text.
3. The transcript is processed by AWS Comprehend for sentiment analysis.
4. Results are stored back into S3, then ingested into Snowflake using Snowpipe.
5. Analyze and visualize sentiment trends from Snowflake.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/Satyam20091998/Audio-sentiment-analysis.git
    ```
2. Follow the instructions in the `requirements.txt` file to install dependencies.
3. Configure AWS services (Lambda, S3, Comprehend, etc.) as per the provided scripts.
4. Use the `main.py` file to trigger the workflow.

## Future Enhancements

- Real-time sentiment analysis on streaming audio.
- Support for multiple languages using AWS Translate.
- Advanced visualization techniques for sentiment trends.

## Contributing

Contributions are welcome! Please follow the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

