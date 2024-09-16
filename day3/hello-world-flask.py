from flask import Flask

app = Flask(__name__) #created a flask instance 


#adding decorator
@app.route("/mdsk")

def hello():
    return 'hello :)'

app.run('0.0.0.0')
