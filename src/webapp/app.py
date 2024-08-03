from flask import Flask, render_template, request, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
from llm_trio import LLMTrio

app = Flask(__name__)
trio = LLMTrio(local=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    topic = request.json['topic']
    few_shot_examples = request.json['few_shot_examples']
    refined_data_sample = trio.invoke_trio(topic, few_shot_examples, verbose=False)
    result = {"output": refined_data_sample, "status_code": 200}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)