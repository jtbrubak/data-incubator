from flask import Flask, render_template, request, url_for, send_from_directory
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', img=False)

@app.route('/submit', methods=["POST"])
def submit():
    f = request.files['image']
    f.save('assets/image.jpg')
    return render_template('index.html', img=True)

@app.route('/image')
def send_file():
    return send_from_directory('assets', 'image.jpg')
