from werkzeug.exceptions import BadRequest


foods = [
    {"id": 1, 'name':'Elvis Presley', 'food_name':'Bacon', 'url':'https://pbs.twimg.com/media/AxYHQ3TCEAIUQOh?format=jpg&name=small'},
    {"id": 2, 'name':'Whoopi Goldberg', 'food_name':'Onion', 'url':'https://pbs.twimg.com/media/BYlq1RgIQAE5X9g?format=jpg&name=small'},
    {"id": 3, 'name':'Kate Middleton', 'food_name':'Jelly Bean', 'url':'https://pbs.twimg.com/media/BiNI2q5IQAAMlNa?format=jpg&name=small'},
    {"id": 4, 'name':'Richard Nixon', 'food_name':'Aubergine', 'url':'https://cdn.firstwefeast.com/assets/2015/08/reagan-eggplant.jpg'},
    {"id": 5, 'name':'Jesus Christ', 'food_name':'Cheeto', 'url':'https://cdn.firstwefeast.com/assets/2015/08/jesus.jpg'},
    {"id": 6, 'name':'Chewbacca ', 'food_name':'Walnut', 'url':'https://pbs.twimg.com/media/BRGy95mCUAABfqA?format=png&name=small'},
    {"id": 7, 'name':'George Washington', 'food_name':'Chicken Nugget', 'url':'https://ichef.bbci.co.uk/news/1024/media/images/58896000/jpg/_58896092_014177188-1.jpg'},
    {"id": 8, 'name':'Donald Trump', 'food_name':'Butter', 'url':'https://pbs.twimg.com/media/CNNLgytWsAEI9-j?format=png&name=small'},
    {"id": 9, 'name':'Iggy Azalea', 'food_name':'Salmon', 'url':'https://64.media.tumblr.com/a88b7050baf908501e3d3bba1b369409/tumblr_natzzzL9uA1tjiwazo1_1280.png'},
    {"id": 10, 'name':'Mother Thersea', 'food_name':'Cinnamon Roll', 'url':'https://pbs.twimg.com/media/B0UJrhIIUAEQc8s?format=jpg&name=small'},
    {"id": 11, 'name':'Sylvester Stallone', 'food_name':'Green Pepper', 'url':'https://pbs.twimg.com/media/CFsLRHwW8AAy2yb?format=jpg&name=small'}
]

def index(req):
    return [f for f in foods], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_food = req.get_json()
    new_food['id'] = sorted([f['id'] for f in foods])[-1] + 1
    foods.append(new_food)
    return new_food, 201

def update(req, uid):
    food = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        food[key] = val
    return food, 200

def destroy(req, uid):
    food = find_by_uid(uid)
    foods.remove(food)
    return food, 204

def find_by_uid(uid):
    try:
        return next(food for food in foods if food['id'] == uid)
    except:
        raise BadRequest(f"We don't have a food lookalike with id {uid}!")