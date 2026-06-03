from app.ingestion.youtube import extract_metadata

url = "https://www.youtube.com/watch?v=4PhVS4VpEbA&pp=ugUHEgVlbi1VUw%3D%3D"

data = extract_metadata(url)

print(data)