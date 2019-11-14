from flask import Flask

app = Flask(__name__)

def is_keyword(os):
    print(os)

@app.route('/')
def index():
    text = open('index.html').read()
    return text
    import webbrowser
    webbrowser.open('http://127.0.0.1:5000')

@app.route('/js/')
def js():
    return "protonscript.js\nmode-proton.js"

@app.route('/css/')
def css():
    return "style.css"

@app.route('/html/')
def html():
    return "index.html"

@app.route('/css/style.css')
def style():
    return open('css/style.css').read()

@app.route('/js/protonscript.js')
def protonscript():
    return open('js/protonscript.js').read()

@app.route('/js/mode-proton.js')
def mode_proton():
    return open('js/mode-proton.js').read()

if __name__ == '__main__':
    app.run(debug=True)
    
