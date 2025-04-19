from flask import Flask, render_template, jsonify, request
import datetime
import json

app = Flask(__name__)

# In-memory storage for user actions
user_actions = []

def record_action(action_type, details):
	timestamp = datetime.datetime.now().isoformat()
	action = {
		'timestamp': timestamp,
		'action_type': action_type,
		'details': details
	}
	user_actions.append(action)

def load_json_data(folder, filename):
	try:
		if not folder:
			with open(f'static/data/{filename}.json', 'r') as f:
				return json.load(f)
		else:
			with open(f'static/data/{folder}/{filename}.json', 'r') as f:
				return json.load(f)
	except FileNotFoundError:
		return {}

@app.route('/')
def home():
	page_data = load_json_data(None, 'welcome')
	return render_template('welcome.html', data=page_data)

@app.route('/start', methods=['POST'])
def start():
	record_action('start', {'page': 'welcome'})
	return jsonify({"status": "success"})

@app.route('/learn')
def learn():
	record_action('page_visit', {'page': 'learn'})
	page_data = load_json_data(None, 'learn')
	return render_template('learn.html', data=page_data)

@app.route('/learn/naturals')
def learn_naturals():
	record_action('page_visit', {'page': 'naturals'})
	page_data = load_json_data('naturals', 'naturals')
	return render_template('naturals/learn_naturals.html', data=page_data)

@app.route('/learn/treble')
def learn_treble():
	record_action('page_visit', {'page': 'treble'})
	page_data = load_json_data('naturals', 'treble')
	return render_template('naturals/learn_clef.html', data=page_data)

@app.route('/learn/bass')
def learn_bass():
	record_action('page_visit', {'page': 'bass'})
	page_data = load_json_data('naturals', 'bass')
	return render_template('naturals/learn_clef.html', data=page_data)

@app.route('/learn/accidentals')
def learn_accidentals():
	record_action('page_visit', {'page': 'accidentals'})
	page_data = load_json_data('accidentals', 'accidentals')
	return render_template('accidentals/learn_accidentals.html', data=page_data)

@app.route('/learn/challenge')
def learn_challenge():
	record_action('page_visit', {'page': 'challenge'})
	page_data = load_json_data('challenge', 'challenge')
	return render_template('challenge/learn_challenge.html', data=page_data)

if __name__ == '__main__':
	app.run(port=5001, debug=True)