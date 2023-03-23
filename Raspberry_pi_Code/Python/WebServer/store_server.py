from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', js_file='script.js')

@app.route('/handle-click', methods=['POST'])
def handle_click():
    # Do something here
    return 'Button clicked!'

if __name__ == '__main__':
    app.run()