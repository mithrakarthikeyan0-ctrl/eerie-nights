from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from game_logic import GameState
from scenarios import SCENARIOS

app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Global game state (for prototype simplicity - usually session based)
# In a real app, use a database or session storage
game_state = GameState()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/start', methods=['POST'])
def start_game():
    global game_state
    game_state = GameState()
    # Start at scenario '1'
    initial_scenario = SCENARIOS['1']
    return jsonify({
        'message': initial_scenario['text'],
        'choices': initial_scenario['choices'],
        'stats': game_state.get_stats(),
        'image': initial_scenario.get('image', 'default_horror.jpg')
    })

@app.route('/api/choice', methods=['POST'])
def make_choice():
    data = request.json
    choice_index = data.get('choice_index')
    
    if choice_index is None:
        return jsonify({'error': 'No choice provided'}), 400

    result = game_state.process_choice(choice_index)
    
    return jsonify(result)

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify(game_state.get_stats())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
