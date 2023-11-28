import requests

api_key = "43f86ffc46984db794b257b903c78bf1"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=43f86ffc46984db794b257b903c78bf1"

# Make a request with newsapi
request = requests.get(url)

# Get a dictionary in JSON format
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])