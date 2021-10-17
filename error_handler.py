from flask import jsonify
from main import app

@app.errorhandler(500)
def handle_internal_server_error(e='internal server error'):
    return jsonify({
            'message' : e,
            'status_code' : 500
    }), 500

@app.errorhandler(422)
def handel_unprocessable_entity(e='unprocessable entity'):
        return jsonify({
                'message' : e ,
                'status_code': 422
        }), 422


@app.errorhandler(404)
def handle_not_found_error(e='not found'):
    return jsonify({
            'message' : e,
            'status_code' : 404
    }),404