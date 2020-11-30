from flask import Flask, render_template, request
from keras.models import load_model
from keras.models import model_from_json
import numpy as np
import cv2
app = Flask(__name__)
@app.route("/")
def home():
  return render_template('base.html')
@app.route('/after',methods=['GET','POST'])
def after():
  return "<h2> hii</h2>"
    
if __name__ == "__main__":
    app.run()
