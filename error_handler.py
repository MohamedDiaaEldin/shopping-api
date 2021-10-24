from flask import jsonify
from main import app


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


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

@app.errorhandler(501)
def handel_not_implemented_error(e='not implemented'):
        return jsonify({
                'message' : e , 
                'status_code' : 501
        }), 501
