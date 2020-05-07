from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
        title="Welcome to Rope_Blog",\
        message="Who are you?")

@app.route('/', methods=['POST'])
def form():
    field = request.form['field']
    return render_template('index.html',\
        title="Sample answer",\
            message="Hello %s-san" % field)

if __name__ == '__main__':
    app.debug=True
    app.run()

#def hello_world():
#    return 'welcome to Flask World!'
#if __name__ == '__main__':
#    app.debug=True
#    app.run(host='localhost')