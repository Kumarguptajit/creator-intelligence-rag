from app.ingestion.downloader import download_audio
from app.ingestion.audio_transcript import transcribe_audio

url = "https://www.instagram.com/reel/DY32H6BINDH/?igsh=MTFzY25heXZxOHF3bg=="

audio_file = download_audio(url)

print(audio_file)

text = transcribe_audio(audio_file)

print(text)