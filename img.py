import requests
url = "https://upload.wikimedia.org" \
       "/wikipedia/commons/thumb/7/79" \
       "/Flag_of_Nigeria.svg" \
       "/255px-Flag_of_Nigeria.svg.png"

response = requests.get(url)
data = response.content
with open('img.png', 'wb') as image:
    image.write(data)