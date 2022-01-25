from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import foods
from werkzeug import exceptions
from flask import Flask
import smtplib
# from flask_mail import Mail

app = Flask(__name__)
CORS(app)

my_email = "cairns.python@gmail.com"
password = "grihqzcxfknjppls"

email_to = "cairns.python@gmail.com"

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
    if request.method == 'GET': 
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()  # makes connection secure
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email_to,
                                    msg=f"Subject:Food has just been added to the database".encode("utf8"))
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
