import requests

response = requests.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-01&sortBy=publishedAt&apiKey=e8c8a6b0a0824682bfcc590fc3d4bbc9")
data = response.json()