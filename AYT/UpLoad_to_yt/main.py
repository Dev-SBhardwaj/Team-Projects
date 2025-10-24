import os
import googleapiclient.discovery
import google_auth_oauthlib.flow

# YouTube OAuth credentials
CLIENT_ID = "ENTER_CLIENT_ID" 
CLIENT_SECRET = "ENTER_SECRET"

# YouTube API setup  
API_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Video file details
VIDEO_FILE = "D:\Projects\youtube_automation\ideo.mp4" 

# Auth flow to get credentials
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_config(
    client_config={
        "web": {
            "client_id": CLIENT_ID,
            "project_id": "scrap-393110",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": CLIENT_SECRET
        }
    },
    scopes=SCOPES
)
credentials = flow.run_local_server() 

# Build YouTube API client
youtube = googleapiclient.discovery.build(
    API_NAME, API_VERSION, credentials=credentials)

# Upload video
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Video title",
            "description": "Video description",
            "videoCategory": "28" 
        },
        "status": {
            "privacyStatus": "public" 
        }
    },
    media_body=VIDEO_FILE
)
response = request.execute()

print("Video uploaded with ID:", response["id"])

