import sql_update
from flask import Flask, request,jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)

class getRec(Resource):
    def get( self, personId,contentId,eventType ):
        sql_update.update_csv( personId,contentId,eventType )
        return {'data': 'SUCCESS'}
        #return jsonify(ghn_rec_collab.api_rec( userId))
        #return ghn.hybrid( userId)
        
api.add_resource(getRec, '/ghn/<personId>/<contentId>/<eventType>')

if __name__ == '__main__':
    app.run()
