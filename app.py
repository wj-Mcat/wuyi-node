from flask import Flask, request, jsonify

app = Flask(__name__)


def success(msg):
    return jsonify({"code": 200, "msg": msg})


def data(json_data):
    return jsonify({"code": 200, "data": json_data})


def error(msg):
    return jsonify({"code": 500, "msg": msg})


@app.route('/', methods=['GET'])
def get_status():
    """get the node status and return data"""
    return data({})
