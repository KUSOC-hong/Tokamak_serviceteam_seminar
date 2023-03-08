from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbbonmedia

@app.route('/')
def home():
    return render_template('index.html')


# API
@app.route('/api/list', methods=['GET'])
def news_list():
    news = list(db.news.find({}, {'_id': False}).sort('publishedat', -1))
    # db 데이터 정상적으로 조회했다면 success와 함께 news_list 목록을 프론트에 전달
    return jsonify({'result': 'success', 'news_list': news})

@app.route('/search', methods=['POST','GET'])
def search():
    searchbox = request.form['text']
    query   = list(db.news.find({"title": {"$regex": searchbox, "$options": "i"}}, {'_id': False}).sort('publishedat', -1))
    # print(query)
    return jsonify({'result': 'success', 'queries': query })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)