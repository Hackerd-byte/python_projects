from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
import os 
app=Flask(__name__)
bashdir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(bashdir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
ma=Marshmallow(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    contact=db.Column(db.String(100),unique=False)
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=User
        load_instance=True
        #fields=('rn','name','contact')
        
user_schema=UserSchema()
users_schema=UserSchema(many=True)


@app.route("/user",methods=["POST"])
def add_user():
    name=request.json['name']
    contact=request.json['contact']
    existing_user = User.query.filter_by(contact=contact).first()
    if existing_user:
        return jsonify({"error": "Contact already exists"})
    new_user=User(name=name,contact=contact)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)
@app.route('/user',methods=["GET"])
def getallusers():
    all_users=User.query.all()
    result=users_schema.dump(all_users)
    return jsonify(result)
@app.route('/user/<id>',methods=['GET'])
def getuserbyid(id):
    user=User.query.get(id)
    return user_schema.jsonify(user)
@app.route('/user/<id>',methods=['PUT'])
def updateuserbyid(id):
    user=User.query.get(id)
    name=request.json['name']
    contact=request.json['contact']
    user.name=name
    user.contact=contact
    db.session.commit()
    return user_schema.jsonify(user)
@app.route('/user/<id>',methods=['DELETE'])
def deleteuser(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schma.jsonify(user)
if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=3456)
