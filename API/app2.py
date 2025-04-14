from flask import Flask, jsonify
from utils.dummy_data import dummy_data_blogs, dummy_data_users
from utils.fetch_api import fetch_data

app = Flask(__name__)

data = fetch_data('https://api.thecatapi.com/v1/breeds')
minififed_data = [ {
        'id': cat['id'],
        'name': cat['name'],
        'origin': cat['origin'],
        'temperament': cat['temperament'],
        'description': cat['description'],
        'weight': cat['weight']['metric'],
        'life_span': cat['life_span'],
       "image_url":  f"https://cdn2.thecatapi.com/images/{cat.get('reference_image_id')}.jpg" if  cat.get('reference_image_id') else ''
        } for cat in  data]

@app.route('/')
def home():
    return '<h1 style="color:red;font-size:120px; text-align:center;">Home sweet home!<h1>'

@app.route('/api/v1/users')
def users():
    return dummy_data_users

@app.route('/api/v1/blogs')
def blogs():
    return dummy_data_blogs

@app.route('/api/v1/blogs/<id>')
def blog(id):
    blog1= [item for item in dummy_data_blogs if item['id'] == int(id)]

    return blog1[0]

@app.route('/api/v1/cats')
def cats():
    return minififed_data
    '''
    change the life span to average
    '''


@app.route('/api/v1/cats/id/<id>')
def cat_by_id(id):
    return [cat for  cat in minififed_data if cat['id'] == id] 



@app.route('/api/v1/cats/origin/<origin>')
def cats_by_origin(origin):
    return [cat for  cat in minififed_data if cat['origin'] == origin]

if __name__ == '__main__':
    app.run(host='localhost', port = 5000, debug=True)