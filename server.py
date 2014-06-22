from flask import Flask, render_template, request

# Setup App Server #

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

if __name__ == '__main__':
  app.run(debug=True)
