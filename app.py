from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import foods
from werkzeug import exceptions
from flask import Flask
# from flask_mail import Mail

app = Flask(__name__)
CORS(app)

# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = '97e041d5e367c7'
# app.config['MAIL_PASSWORD'] = 'cfaf5b99f8bafb'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# mail = Mail(app)

# @app.route("/")
# def index():
#   msg = Message('Hello from the other side!', sender =   'peter@mailtrap.io', recipients = ['paul@mailtrap.io'])
#   msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
#   mail.send(msg)
#   return "Message sent!"

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/foods', methods=['GET', 'POST'])
def foods_handler():
    fns = {
        'GET': foods.index,
        'POST': foods.create
    }
    print(foods.index)
    resp, code = fns[request.method](request)
    print(resp[0])
    return jsonify(resp), code

@app.route('/api/foods/<int:food_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def food_handler(food_id):
    fns = {
        'GET': foods.show,
        'PATCH': foods.update,
        'PUT': foods.update,
        'DELETE': foods.destroy
    }
    resp, code = fns[request.method](request, food_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
