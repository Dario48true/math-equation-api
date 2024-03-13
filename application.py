from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get input data from request
        data = request.json

        # Perform some calculation
        result = data['minutes'] + data['hours']*60 + data['days']*60*24

        # Return the result
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
