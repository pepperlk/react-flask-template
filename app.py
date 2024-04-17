# Import Flask class from the flask module
import os
from flask import Flask, send_from_directory, redirect


# Create an instance of the Flask class
app = Flask(__name__, static_folder='client/build')


@app.route('/')
def serve():

    # if client/build folder exists then return the index.html file
    if os.path.exists('client/build'):
        return send_from_directory(app.static_folder, 'index.html')
    else:
        return {'message': 'client/build folder not found'}
    

# return static files in the client/build folder
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)
        




# Flask API endpoint
@app.route('/api/data')
def get_data():
    return {'data': 'Your data here'}




# Check if the executed file is the main program
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)