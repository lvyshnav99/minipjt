from flask import Flask, render_template,request
app = Flask(__name__)
import cv2

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/after',methods=['GET','POST'])
def after():
    img=request.files['file1']
    img.save('./static/file.jpg')
    image=cv2.imread('./static/file.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return render_template('after.html')
    
 
if __name__ == "__main__":
    app.run(debug=True)
