from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/let')
def leto():
    return render_template('let.html')

@app.route('/osen')
def osen():
    return render_template('osen.html')

@app.route('/vesn')
def vesna():
    return render_template('vesn.html')

@app.route('/wint')
def winter():
    return render_template('wint.html')

if __name__=='__main__':
    app.run(debug=True)