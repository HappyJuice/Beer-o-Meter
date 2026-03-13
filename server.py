from flask import Flask, render_template, request, jsonify
import json
import os


app = Flask(__name__)
DATA_FILE = 'votes.json'


# Načti hlasy ze souboru
def load_votes():
    if not os.path.exists(DATA_FILE):
        return {"0. patro": 0, "1. patro": 0, "2. patro": 0, "3. patro": 0, "4. patro": 0, "5. patro": 0}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


# Ulož hlasy do souboru
def save_votes(votes):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(votes, f, ensure_ascii=False, indent=2)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vote_page')
def vote_page():
    return render_template('vote_page.html')


@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    option = data.get('option')
    votes = load_votes()
    votes[option] += 1
    save_votes(votes)
    return ('', 204)


@app.route('/get_votes')
def get_votes():
    votes = load_votes()
    return jsonify(votes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
