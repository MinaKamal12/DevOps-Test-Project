import os
from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello():
    return jsonify({
        'message': 'Hello from DevOps Flask Project!',
        'timestamp': datetime.utcnow().isoformat()
    })
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'OK'}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
