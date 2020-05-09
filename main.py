from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
        title="Welcome to Rope_Blog",\
        message="織田信長が今川義元を打ち取った戦いの名は？",\
    )  

@app.route('/', methods=['POST'])
def form():
    flg= 'rd'
    rd = request.form.get('radio')
    return render_template('index2_post.html',\
    flg=rd)     
if __name__ == '__main__':
    app.debug=True
    app.run(),


#def hello_world():
#    return 'welcome to Flask World!'
#if __name__ == '__main__':
#    app.debug=True
#    app.run(host='localhost')

#@app.route('/', methods=['POST'])
#def form():
#    field = request.form['field']
#    return render_template('index.html',\
#        title="Sample answer",\
#            message="Hello %s-san" % field)