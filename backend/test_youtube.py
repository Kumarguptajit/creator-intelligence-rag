from app.ingestion.youtube import extract_metadata
from app.ingestion.transcript import extract_transcript

url = "https://www.youtube.com/watch?v=4PhVS4VpEbA&pp=ugUHEgVlbi1VUw%3D%3D"

data = extract_metadata(url)

print(data)

print(extract_transcript(url)[:1000])