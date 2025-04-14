from flask import Flask
app = Flask (__name__)
data = [
    {
    "name":"Asab",
    "gender":"male",
    "age":250
},
{
    "name":"Yoni",
    "gender":"male",
    "age":25
}
]

@app.route ('/users')
def users():
    return data

@app.route('/')
def home():
    return 'This is home'
if __name__ == '__main__':
    app.run(host='localhost', port = 5000, debug=True)
print ('Flask Server is Running')

