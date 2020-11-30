from flask import Flask, render_template,request

app = Flask(__name__)
@app.route("/")
def home():
  return render_template('base.html')

@app.route("/after",methods=['GET','POST'])
def after():
    img=request.files['file1']
    img.save('./static/file.jpg')
    return render_template('after.html')
 
if __name__ == "__main__":
    app.run()
