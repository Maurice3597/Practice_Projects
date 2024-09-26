import requests

api_key = "9ae7a2ef77b3478c8c8d24ba29e438c7"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=9ae7a2ef77b3478c8c8d24ba29e438c7"

request = requests.get(url)
content = request.json()
articles = content['articles']
print(type(articles))
body = ""
for article in articles:
    body = body + article['title'] + "\n" + article['description'] + 2*"\n"
    print(body)