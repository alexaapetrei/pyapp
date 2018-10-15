#product service

from flask import Flask
from flask_restful import Resource , Api

app = Flask(__name__)
api = Api(app)

class Prodouct(Resource):
    def get(self):
        return {
            'products' : [
                'Ice stuff',
                'Coco',
                'Fruit',
                'eggs',
                'other',
                'spoons'
            ]
        }
api.add_resource(Prodouct, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)