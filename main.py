from flask import Flask, jsonify, request
from core.users import AuthError, UserManager
from werkzeug.exceptions import HTTPException
from schemas.user import UserDataResponseModel, UserRegistrationModel

app = Flask(__name__)

user_manager = UserManager("users.json")


@app.errorhandler(HTTPException)
def handle_auth_error(e: HTTPException):
    return jsonify({"error": e.description, "type": type(e).__name__}), e.code


@app.route("/user")
def index():
    auth_header = request.authorization
    if auth_header is None:
        raise AuthError("No auth headers provided")

    username, password = auth_header.username, auth_header.password
    user_data = user_manager.authenticate(username, password)

    user_data_trimmed = UserDataResponseModel(**user_data.dict())
    return jsonify(user_data_trimmed.dict())


@app.route("/user", methods=["POST"])
def register():
    data = UserRegistrationModel(**request.json)
    user_manager.create_user(data.username, data.password)

    return jsonify({"info": "Success"})


if __name__ == "__main__":
    app.run(debug=True)
