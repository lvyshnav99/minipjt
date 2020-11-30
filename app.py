from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/after',methods=['GET','POST'])
def after():
  img=request.files['file1']
  return "<h2>hello world</h2>"
if __name__ == "__main__":
    app.run(debug=True)
