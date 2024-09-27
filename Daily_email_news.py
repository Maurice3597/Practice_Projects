import requests
from api_fxns import send_email

api_key = "9ae7a2ef77b3478c8c8d24ba29e438c7"
url = "https://newsapi.org/v2/top-headlines?" \
       "sources=techcrunch&apiKey=" \
       "9ae7a2ef77b3478c8c8d24ba29e438c7"

request = requests.get(url)
content = request.json()
articles = content['articles']
body = "Subject: Daily Tech news\n"
for article in articles:
    body += (article['title'] + "\n"
             + article['description'] + "\n"
             + article['url'] + 2*"\n")

body = body.encode('utf-8')
send_email(body)