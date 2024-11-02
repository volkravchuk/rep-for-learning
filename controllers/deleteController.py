from flask import jsonify
from application import app
from models.model import History

@app.route('/delete/<string:history_id>', methods=['DELETE'])
def delete_history_entry(history_id):
    history_entry = History.objects(id=history_id).first()
    if history_entry:
        history_entry.delete()
        return jsonify({'message': 'Entry deleted successfully'}), 200
    else:
        return jsonify({'message': 'Entry not found'}), 404