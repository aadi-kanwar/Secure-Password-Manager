from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Password
from encryption import encrypt_password, decrypt_password

app = Flask(__name__)
CORS(app)
app.config.from_object("config.Config")
db.init_app(app)

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route("/store-password", methods=["POST"])
def store_password():
    data = request.json
    encrypted_pwd = encrypt_password(data["password"])
    password_entry = Password(
        user_id=data["user_id"], website=data["website"], username=data["username"], encrypted_password=encrypted_pwd
    )
    db.session.add(password_entry)
    db.session.commit()
    return jsonify({"message": "Password stored successfully"}), 201

@app.route("/get-passwords/<int:user_id>", methods=["GET"])
def get_passwords(user_id):
    passwords = Password.query.filter_by(user_id=user_id).all()
    result = [
        {"website": p.website, "username": p.username, "password": decrypt_password(p.encrypted_password)}
        for p in passwords
    ]
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
