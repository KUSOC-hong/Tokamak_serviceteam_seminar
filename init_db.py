### init_db.py ###
import requests
from newsapi.newsapi_client import NewsApiClient
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbbonmedia

# regex = '.*tech.*'
# results = collection.find({'company': {'$regex': regex}})

# for result in results:
#     print(result)


# DB에 저장할 newsapi의 article을 가져오는 함수
def get_articles():
    newsapi = NewsApiClient(api_key ='70fdb9ba81ba40b6bda148e672898bd9')
    articles = newsapi.get_everything(q='(crypto OR web3)',
                                    domains='techcrunch.com,coindesk.com,cryptonews.com,decrypt.co,cointelegraph.com,coinrivet.com,dailycoin.com,coinedition.com',
                                    from_param='2023-02-27',
                                    # to='2023-02-23',
                                    language='en',
                                    sort_by='publishedAt',
                                    page=1)
    print(articles)
    return articles


# article로부터 정보를 가져오고 news 컬렉션에 저장하는 함수
def insert_article(articles):
    for article in articles['articles']:
        doc = {
            'title': article['title'],
            'description': article['description'],
            'srcname': article['source']['name'],
            'img': article['urlToImage'],
            'url': article['url'],
            'publishedat': article['publishedAt'] 
        }
        print('complete!', article['title'])
        db.news.insert_one(doc)


# 기존 news 컬렉션을 삭제하고, article들을 가져온 후, 크롤링하여 DB에 저장하는 함수
def insert_all():
    db.news.drop()  # news 콜렉션을 모두 지워줍니다.
    articles = get_articles()
    insert_article(articles)


# execute
insert_all()