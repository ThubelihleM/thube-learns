from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/bioinf')
def bioinf():
  return render_template('bioinf.html')

@app.route('/compsci')
def compsci():
  return render_template('compsci.html')

@app.route('/datasci')
def datasci():
  return render_template('datasci.html')

@app.route('/math')
def math():
  return render_template('math.html')

if __name__ == "__main__":
  app.run(debug=True)