from flask import Flask, render_template, request, jsonify
from prompts_looping import printing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    html_code = request.form['paragraph1']
    data = request.form['paragraph2']
    # printing(html_code, data)
    # Do something with the paragraphs
    return render_template('progress.html')


@app.route('/progress', methods=['POST'])
def update_progress():
    data = request.get_json()
    progress = data.get('progress')

    # Do something with the progress value
    print('Progress Update:', progress)

    return jsonify({'message': 'Progress updated.'})

if __name__ == '__main__':
    app.run(debug=True)
