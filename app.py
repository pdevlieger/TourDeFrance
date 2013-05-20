from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/graph')
def graph():
    return render_template('graph.html')

if __name__ == '__main__':
    port_number = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port_number, debug=True)