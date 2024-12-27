from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('homepage.html')

@app.route('/contact-us')
def contact_us():
  return render_template('contact-us.html')

@app.route('/services')
def services():
  return render_template('services.html')

@app.route('/gallery')
def gallery():
  return render_template('gallery.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/login')
def login():
  return render_template('login.html')

if __name__ == '__main__':
  app.run(debug=True)