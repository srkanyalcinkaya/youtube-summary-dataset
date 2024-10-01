import pandas as pd
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import isodate 

# Your YouTube API Key
api_key = ''

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Function to get video details
def get_video_details(video_id):
    try:
        request = youtube.videos().list(part='snippet,contentDetails', id=video_id)
        response = request.execute()

        if len(response['items']) > 0:
            video_info = response['items'][0]
            title = video_info['snippet']['title']
            url = f'https://www.youtube.com/watch?v={video_id}'
            iso_duration = video_info['contentDetails']['duration']
            duration = isodate.parse_duration(iso_duration).total_seconds()
            language = video_info['snippet'].get('defaultAudioLanguage', 'N/A')
            return title, url, duration, language
    except Exception as e:
        print(f"Video bilgileri alınırken hata oluştu: {e}")
    return None

# Altyazı bilgilerini alacak fonksiyon
def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([entry['text'] for entry in transcript_list])
        return transcript
    except Exception as e:
        print(f"Altyazı alınırken hata oluştu: {e}")
        return None

# Function to create the dataset
def create_dataset(video_ids):
    data = []
    for video_id in video_ids:
        video_details = get_video_details(video_id)
        if video_details:
            title, url, duration, language = video_details
            transcript = get_video_transcript(video_id)
            data.append({
                'Title': title,
                'URL': url,
                'Duration (seconds)': duration,
                'Language': language,
                'Transcript': transcript if transcript else "Transcript not available"
            })

    df = pd.DataFrame(data)
    df.to_csv('youtube_dataset.csv', index=False)
    return df

# Sample video ID list (update for 100 videos)
video_ids = ['kX3nB4PpJko', "_qAJMXfL6o0", "ndAQfTzlVjc", "KkCXLABwHP0", "Pv0iVoSZzN8", "fuhE6PYnRMc", "TJ2ifmkGGus", "jdMNoQE3mIQ", "cV2gBU6hKfY", "j2ZdF9qo7IA", "T1aZxcyiYAw", "phn0bXbcZY", "oQWmagZmogQ", "NKgXBjkKI_E", "3uTmcG7CgdI", "8CUEPNcGtWs", "QJB0nmEjbDY", "uuc6bXxgvh8", "vtjHHnu_IB0", "HsaSaYcnTKg", "fl1i6RtM4o8", "oT5pDvdMzhk", "_vDZmVXtA7k", "IwYut9qF-jM", "bH3O69BscYg", "qwCBEgjUluU", "MNw9x53Ybos", "XFhY4Vy3IHc", "DcdufLc3QSA",
             "ulHWR0Dp6Rk", "teJAmgiMVIo"]
# Veri setini oluştur
df = create_dataset(video_ids)
print(df.head())
