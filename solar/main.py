from http.server import BaseHTTPRequestHandler, HTTPServer
import numpy as np
import pandas as pd
import pickle
import json

# Load the trained model
with open('solar_model.pkl', 'rb') as model_file:
    regressor = pickle.load(model_file)

# Define the prediction function
def predict(para):
    predictions = regressor.predict([para])
    response = int(predictions[0])
    break_even = para[4] / response
    return response, break_even

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        input_attributes = json.loads(post_data)

        result, break_even = predict(input_attributes)

        response_data = {
            "Annual_Savings": result,
            "Break_Even_Point_Years": break_even
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
