from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/image', methods=["POST"])
def submit():
    content_type = request.files['image'].content_type
    response = make_response(request.files['image'].read())
    response.headers.set('Content-Type', content_type)
    return response
