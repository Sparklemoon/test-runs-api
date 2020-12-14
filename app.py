from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy   
from flask_marshmallow import Marshmallow  
from flask_cors import CORS  
from flask_heroku import Heroku  

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ""

db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)
Heroku(app)



class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, image):
        self.text = text

class ImageSchema(ma.Schema):
    class Meta:
        fields = ("id", "image")

image_schema = ImageSchema()
multiple_image_schema = ImageSchema(many=True)


@app.route("/image/add", methods=["POST"])
def image_question():
    if request.content_type != "application/json":
        return"Error: must be set as JSON."

    post_data = request.get_json()
    image = post_data.get("image")

    record = Question(image)
    db.session.add(record)
    db.session.commit()

    return jsonify("Image added good job")

@app.route("/image/get", methods=["GET"])
def get_all_images():
    all_images = db.session.query(Image).all()
    return jsonify(multiple_image_schema.dump(all_images))

if __name__ == "__main__":
    app.run(debug=True)