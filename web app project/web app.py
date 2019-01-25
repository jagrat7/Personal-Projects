from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
     if request.method == 'POST':
          input = request.form["input"]

          
          return render_template('input.html', input=input)
     

     return render_template('index.html')

@app.route('/aboutme')
def ab():
     
    return render_template('aboutme.html')


if (__name__ =="__main__"):
    app.run(debug=True)