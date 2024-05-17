from flask import Flask, request, jsonify, render_template
import openai
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config["openai"]["api_key"]


app = Flask(__name__)

openai.api_key = api_key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processQuery', methods=['POST'])
def process_query():
    data = request.json
    user_query = data['query']

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f'Extract the relevant company performance metrics from the following query and return as JSON: "{user_query}"',
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )

        metrics = response.choices[0].text.strip()
        metrics_json = jsonify(eval(metrics))  # Convert string to JSON

        return metrics_json
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
