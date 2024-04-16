# Import Flask class from the flask module
import os
from flask import Flask, send_from_directory, redirect


# Create an instance of the Flask class
app = Flask(__name__, static_folder='client/build')


@app.route('/')
def serve():

    # if debugger is on, serve the react app from port 3000
    if app.debug:
        # fwd 301 to react @ port 3000
        return redirect("http://localhost:3000", code=302)
        

    return send_from_directory(app.static_folder, 'index.html')


# Flask API endpoint
@app.route('/api/data')
def get_data():
    return {'data': 'Your data here'}




# Check if the executed file is the main program
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)