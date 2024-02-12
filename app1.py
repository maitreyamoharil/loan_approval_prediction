from flask import Flask, render_template, redirect, url_for, request
import pickle

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("predict.html")

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        arg1 = request.form['gender']
        if arg1 == 'M':
            arg1 = 1
        elif arg1 == 'F':
            arg1 = 0

        arg2 = request.form['married']
        if arg2 == 'Y':
            arg2 = 1
        elif arg2 == 'N':
            arg2 = 0

        arg3 = request.form['education']
        if arg3 == 'Y':
            arg3 = 1
        elif arg3 == 'N':
            arg3 = 0

        arg4 = request.form['job']
        if arg4 == 'Y':
            arg4 = 1
        elif arg4 == 'N':
            arg4 = 0

        arg5 = float(request.form['income'])

        arg6 = float(request.form['loan'])
        
        arg7 = request.form['credit_score']
        if arg7 == 'Y':
            arg7 = 1
        elif arg7 == 'N':
            arg7 = 0

        var = [[arg1, arg2, arg3, arg4, arg5, arg6, arg7]]

        model = pickle.load(open('model.pkl','rb'))
        answer = model.predict(var)
        answer1 = answer[0]
        return render_template("result1.html", answer1 = answer1)

if __name__ == '__main__':
    app.run(debug=True)
