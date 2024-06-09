from flask import request, jsonify, current_app as app
from app import db
from app.models import User, Subscription


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    user = User(email=data['email'])
    db.session.add(user)
    db.session.commit()
    subscription = Subscription(user_id=user.id, location=data['location'])
    db.session.add(subscription)
    db.session.commit()
    return jsonify({"message": "Subscription successful"}), 201


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user:
        Subscription.query.filter_by(user_id=user.id).delete()
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Unsubscription successful"}), 200
    return jsonify({"message": "User not found"}), 404
