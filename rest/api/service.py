from flask import Flask, render_template, request, url_for 
from flask_restful import reqparse, abort, Api, Resource
import lib
import os
import json


IMAGE_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Hello':'World'}
api.add_resource(HelloWorld, '/')

class GeoIds(Resource):
    def get(self):
        return lib.get_ids()
api.add_resource(GeoIds, '/id')

class Find(Resource):
    def post(self, distance):
        geojson = request.get_json(force=True)
        return lib.get_ids_within_distance(geojson, distance)
api.add_resource(Find, '/find/<int:distance>')

class Statistics(Resource):
    def get(self, id, distance):
        return lib.get_geo_stats(id_list=[id], distance=distance)
api.add_resource(Statistics, '/stats/<string:id>/<int:distance>')

@app.route('/<id>')
@app.route('/index')
def show_index(id):
    full_filename = os.path.join(IMAGE_FOLDER, id+'.jpeg')
    if not os.path.isfile(full_filename):
        lib.download_image(id, IMAGE_FOLDER)
    
    print(full_filename)
    return render_template("index.html", user_image = full_filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

