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
	user_actions = []
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

@app.route('/learn/naturals/notes')
def learn_natural_notes():
	record_action('page_visit', {'page': 'natural_notes'})
	page_data = load_json_data('naturals', 'notes')
	return render_template('naturals/learn_notes.html', data=page_data)

@app.route('/learn/naturals/notes/<note>')
def learn_note(note):
	record_action('page_visit', {'page': f'note_{note}'})
	note = note.upper()
	notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
	if note not in notes:
		return "Note not found", 404
	
	note_data = {
		'note': note,
		'clef_image': f'/static/images/Naturals_Learning/{note.lower()}_clef.webp',
		'piano_image': f'/static/images/Naturals_Learning/{note.lower()}_piano.webp',
		'sound': f'/static/audios/naturals/{note.lower()}6.mp3',
		'description': f'This is the note {note}. It is a natural note played on a white key.',
	}
	
	note_index = notes.index(note)
	if note_index < len(notes) - 1:
		note_data['next_note'] = notes[note_index + 1]
	
	return render_template('naturals/note.html', data=note_data)

@app.route('/learn/accidentals/notes')
def learn_accidentals_notes():
	record_action('page_visit', {'page': 'natural_notes'})
	page_data = load_json_data('accidentals', 'notes')
	return render_template('accidentals/learn_notes.html', data=page_data)

@app.route('/learn/accidentals/notes/<note>')
def learn_accidentals_note(note):
	record_action('page_visit', {'page': f'note_{note}'})
	#note = note.upper()
	print(note)
	notes = ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'C♭', 'D♭', 'E♭', 'F♭', 'G♭', 'A♭', 'B♭']
	if note not in notes:
		return "Note not found", 404
	if note[-1] == "#":
		note_file = note[0] + "_sharp"
	else:
		note_file = note[0] + "_flat"
	print(note_file)
	
	note_data = {
		'note': note,
		'treble_clef_image': f'/static/images/Accidentals_Learning/{note_file}/treble.png',
		'bass_clef_image': f'/static/images/Accidentals_Learning/{note_file}/bass.png',
		'piano_image': f'/static/images/Accidentals_Learning/{note_file}/piano.png',
		'sound': f'/static/audios/accidentals/{note_file}.mp3',
		'description': f'This is the note {note}. It is a natural note played on a white key.',
	}
	print(note_data)
	
	note_index = notes.index(note)
	print(note_index)
	if note_index < len(notes) - 1:
		note_data['next_note'] = notes[note_index + 1]
	return render_template('accidentals/note.html', data=note_data)

if __name__ == '__main__':
	app.run(port=5001, debug=True)