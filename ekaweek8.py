import pymongo 
from datetime import datetime
from flask import Flask,request

app = Flask(__name__)

@app.route('/eka',methods=['POST'])
def sensor():

    dt = datetime.now()
    client = pymongo.MongoClient("mongodb+srv://ekaynaw:210106@ekaweek8.hfq3wxs.mongodb.net/?retryWrites=true&w=majority")
    db = client['ekaweek8']
    my_collections = db['folder']


    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')


    nilai_sensor = {'kecepatan':kecepatan,
                    'latitude':latitude,
                    'longitude':longitude,
                    'timestamp' : dt
                    }

    results = my_collections.insert_one(nilai_sensor)
    return ('data selesai dikerjakan')  
  
  
  
if __name__ == '__main__':
    app.run(debug=True)
