import rec_int_ghn
from flask import Flask, request,jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)

class getRec(Resource):
    def get(self, User_Id ):
        return {'data': rec_int_ghn.recommend(User_Id)}
        #return jsonify(ghn_rec_collab.api_rec(userId))
        #return ghn.hybrid( userId)
        
api.add_resource(getRec, '/ghn3/<User_Id>')

if __name__ == '__main__':
    app.run()
