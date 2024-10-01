# YouTube Video Data Collector

This project collects basic video information and transcripts for specified YouTube video IDs and saves them to a CSV file.

## About the Project

This Python script uses the YouTube Data API and YouTube Transcript API to collect the following information:

- Video Title
- Video URL
- Video Duration (in seconds)
- Video Language
- Video Transcript (if available)

## Requirements

To run the project, you need the following libraries:

- pandas: Used for data processing and creating CSV files.
- google-api-python-client: Used for interacting with the YouTube Data API.
- youtube-transcript-api: Used to retrieve video transcripts.
- isodate: Used to parse ISO 8601 duration format.

You can install these libraries using the `requirements.txt` file.

## Installation

1. Clone or download this repository.
2. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```
3. Add your own YouTube Data API key to the `api_key` variable in the `youtube_dataset.py` file.

## Usage

1. Add the YouTube video IDs you want to the `video_ids` list in the `youtube_dataset.py` file.
2. Run the script:
   ```
   python youtube_dataset.py
   ```
3. The script will collect information for the specified video IDs and create a CSV file named `youtube_dataset.csv`.

## Notes

- There is a daily quota limit for using the YouTube Data API. Be careful not to exceed this limit when collecting data for a large number of videos.
- Transcripts may not be available for some videos. In this case, the transcript field will be filled with "Transcript not available".
- If video language information is not available, it will be recorded as "N/A".

## License

This project is licensed under the [MIT License](LICENSE).
