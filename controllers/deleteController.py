from flask import jsonify
from application import app
from models.model import db, History

@app.route('/delete/<int:history_id>', methods=['DELETE'])
def delete_history_entry(history_id):
    history_entry = History.query.get(history_id)
    if history_entry:
        db.session.delete(history_entry)
        db.session.commit()
        return jsonify({'message': 'Entry deleted successfully'}), 200
    else:
        return jsonify({'message': 'Entry not found'}), 404