from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quote', methods=['GET'])
def get_quote():
    try:
        response = requests.get('https://api.quotable.io/random')
        data = response.json()
        return jsonify({
            'content': data['content'],
            'author': data['author']
        })
    except Exception as e:
        return jsonify({'error': 'Could not fetch a quote', 'details': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
