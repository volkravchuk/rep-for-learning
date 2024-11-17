from flask import request, jsonify
from application import app
from models.model import History


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    first_number = int(data['firstNumber'])
    operator = str(data['operator'])
    second_number = int(data['secondNumber'])
    result: int = eval(f"{first_number} {operator} {second_number}")

    history_entry = History(
        first_number = first_number,
        operator = operator,
        second_number = second_number,
        result = result
        )

    history_entry.save()

    return jsonify({'result': result})