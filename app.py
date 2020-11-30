from flask import Flask, render_template,request
import numpy as np
import cv2

app = Flask(__name__)
@app.route("/")
def home():
  return render_template('base.html')

@app.route("/after",methods=['GET','POST'])
def after():
    img=request.files['file1']
    img.save('./static/file.jpg')
    image=cv2.imread('./static/file.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')
    faces = cascade.detectMultiScale(gray, 1.1, 3)
    
    for x,y,w,h in faces:
      cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
      cropped=image[y:y+h,x:x+w]
    cv2.imwrite('./static/after.jpg', image)
    
    return render_template('after.html',data=5)
 
if __name__ == "__main__":
    app.run()
