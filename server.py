from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_root():
    return jsonify({'message': 'Welcome to the Flask API!'}), 200

if __name__ == '__main__':
    app.run(debug=True)