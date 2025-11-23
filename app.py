from flask import Flask, render_template, request, jsonify
from src.gemini_agent import GeminiAgent
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
DATASET_PATH = os.path.join(os.path.dirname(__file__), 'Dataset', 'education-economy-data.csv')

# Initialize Agent
# Ensure you have authenticated with gcloud: `gcloud auth application-default login`
try:
    agent = GeminiAgent(PROJECT_ID, LOCATION, DATASET_PATH)
    print("Gemini Agent initialized successfully.")
except Exception as e:
    print(f"Failed to initialize Gemini Agent: {e}")
    agent = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    if not agent:
        return jsonify({'error': 'Agent not initialized. Check server logs and credentials.'}), 500
    
    data = request.json
    query = data.get('query')
    
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    
    try:
        # 1. Generate Code
        generated_code = agent.generate_response(query)
        
        # 2. Execute Code
        output, plot_base64 = agent.execute_code(generated_code)
        
        return jsonify({
            'code': generated_code,
            'output': output,
            'plot': plot_base64
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
