from flask import Flask, jsonify
from utils.dummy_data import dummy_data_blogs, dummy_data_users
from utils.fetch_api import fetch_data

app = Flask(__name__)



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
    data = fetch_data('https://api.thecatapi.com/v1/breeds')
    '''
    TODO
    {
"description": "The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals.",
"id": "abys",
"image_url": "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg",
"life_span": 14.5,
"name": "Abyssinian",
"origin": "Egypt",
"temperament": "Active, Energetic, Independent, Intelligent, Gentle",
"weight": 4
},
    
    '''
    return data


if __name__ == '__main__':
    app.run(host='localhost', port = 5000, debug=True)