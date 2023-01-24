from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Smart Agriculture</h1>"

@app.route('/sensor-data', methods=['POST'])
def receive_sensor_data():
    # get the sensor data from the request
    sensor_data = request.json["sensor_value"]
    
    # process the sensor data here, for example using a trained model
    #prediction = model.predict(sensor_data)
    
    # return the prediction as a json object
    return jsonify(prediction=20)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
