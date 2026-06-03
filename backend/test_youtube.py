from app.ingestion.youtube import extract_metadata
from app.ingestion.transcript import extract_transcript
from app.ingestion.service import calculate_engagement_rate, process_youtube_video

url = "https://www.youtube.com/watch?v=4PhVS4VpEbA&pp=ugUHEgVlbi1VUw%3D%3D"



# print(extract_metadata(url))

# print(extract_transcript(url)[:1000])

print(process_youtube_video(url))