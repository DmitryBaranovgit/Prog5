from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = ''
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=30)
jwt = JWTManager(app)

# Пример данных о пользователях и бонусной программе
users = {
    "user1": {"password": "password1", "spending": 500, "level": "Silver"},
    "user2": {"password": "password2", "spending": 1500, "level": "Gold"},
    }

bonus_levels = {
    "Silver": {"next_level": "Gold", "min_spending": 1000},
    "Gold": {"next_level": "Platinum", "min_spending": 2000},
    "Platinum": {"next_level": None, "min_spending": None},
}

# Обработчик корневого маршрута

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Bonus Program API!",
        "endpoints": {
            "login": "/login (POST)",
            "get_bonus_info": "/bonus (GET)"
        }
    })

#Эндпоинт для авторизации
@app.route('/login', methods = ['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or user['password'] != password:
        return jsonify({"msg": "Invalid username or password"}), 401
    
    token = create_access_token(identity=username)
    return jsonify({"token": token})

# Эндпоинт для получения данных о бонусной программе
@app.route('/bonus', methods=['GET'])
@jwt_required()
def get_bonus_info():
    current_user = get_jwt_identity()
    user_data = users.get(current_user)

    if not user_data:
        return jsonify({"msg": "User not found"}), 404
    
    current_level = user_data['level']
    spending = user_data['spending']
    level_info = bonus_levels[current_level]

    response = {
        "current_level": current_level,
        "spending": spending,
        "next_level": level_info.get("next_level"),
        "next_level_min_spending": level_info.get("min_spending"),
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)