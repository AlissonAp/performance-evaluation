from flask import Flask, request
import json
import functools 


app = Flask(__name__)


@app.route("/", methods=['GET'])
def base64():
    return "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", 200


@app.route("/", methods=['PUT'])
def multi():
    return str(functools.reduce(lambda total,num : total * num, request.data)), 200


@app.route("/", methods=['DELETE'])
def delete():
    return str(request.get_json()["Nome"]), 200


@app.route("/", methods=['POST'])
def multiplica():

    result = 2324 * 234 * 1234

    return str(result), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')