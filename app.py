from flask import Flask, render_template
#import Flask
import main

app = Flask(__name__) # instance of flask running

# creating route, home page
@app.route('/')
#def index():
 #   return ("Hello World")

def dynamic_page():
    return main.game()
