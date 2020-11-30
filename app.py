from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/after',methods=['GET','POST'])
def after():
    return "<h2>hello</h2>"
    
 
if __name__ == "__main__":
    app.run(debug=True)
