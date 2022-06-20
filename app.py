import sqlalchemy

from Post import *
from flask import jsonify
import requests


# get
@app.route('/get/post/id/<id>', methods=['GET'])
def get_post_id(id):

    try:
        result = Post.query.filter(Post.id == id).one().__dict__
        result_dict = {}
        keys = ["id", "userId", "title", "body"]

        for key in keys:
            result_dict[key] = result[key]

        return jsonify(result_dict), 200

    except sqlalchemy.exc.NoResultFound:

        api_url = "https://jsonplaceholder.typicode.com/posts/" + id.__str__()
        response = requests.get(api_url)

        if response.status_code == 200:
            api_url = "http://127.0.0.1:5000/add/post"
            resp = requests.post(api_url,json=response.json())

            if resp.status_code != 201:
                return jsonify({"message": "Error"}), 400   # neuspesne pridanie

            return response.json()
        else:
            return jsonify({"message": "Post not found"}), 404


@app.route('/get/post/userId/<userId>', methods=['GET'])
def get_post_userId(userId):
    results = Post.query.filter(Post.userId == userId).all()

    results = [d.__dict__ for d in results]

    list_of_results = []
    keys = ["id", "userId", "title", "body"]

    for result in results:
        result_dict = {}
        for key in keys:
            result_dict[key] = result[key]
        list_of_results.append(result_dict)

    if len(list_of_results) > 0:
        return jsonify(list_of_results), 200
    else:
        return jsonify({"message": "Post not found"}), 404


# add
@app.route('/add/post', methods=['POST'])
def add_post():
    args = post_args.parse_args()

    api_url = "https://jsonplaceholder.typicode.com/users/" + args["userId"].__str__()
    response = requests.get(api_url)

    if response.status_code == 200:

        post = Post(id=args["id"], userId=args["userId"], title=args["title"], body=args["body"])
        try:
            db.session.add(post)
            db.session.commit()
        except:
            return jsonify({"message": "Fail"}), 400

        return jsonify({"message": "Success"}), 201
    else:
        return jsonify({"message": "userId not found"}), 404


# delete
@app.route('/delete/post/<id>', methods=['DELETE'])
def delete_post(id):

    try:
        db.session.delete(Post.query.get_or_404(id))
        db.session.commit()
        return jsonify({"message": "Deleted"}), 200

    except:
        return jsonify({"message": "Post not found"}), 404


# update
@app.route('/update/post/<id>', methods=['PUT'])
def update_post(id):
    args = update_post_args.parse_args()
    title = args["title"]
    body = args["body"]

    try:
        post = Post.query.get_or_404(id)
        if title is not None:
            post.title = title
        if body is not None:
            post.body = body
        if title is None and body is None:
            return jsonify({"message": "No changes"}), 400
        db.session.commit()
        return jsonify({"message": "Updated"}), 200
    except :
        return jsonify({"message": "Id not found"}), 404


if __name__ == '__main__':
    app.run()
