from flask import jsonify
from application import app
from models.model import History

@app.route('/history', methods=['GET'])
def get_history():
    history_entries = History.query.all()
    history_list = []
    
    for entry in history_entries:
        history_list.append({
            'first_number': entry.first_number,
            'operator': entry.operator,
            'second_number': entry.second_number,
            'result': entry.result,
            'calculated': entry.calculated.isoformat()
        })
    
    return jsonify(history_list)