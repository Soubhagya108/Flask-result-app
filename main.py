# Building URL Dynamically

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result/<int:score>')
def result(score):
    res=''
    if score>=50:
        res='pass'
    else:
        res='fail'

    return render_template('result.html',result=res,scored=score)
# Result checker
@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        cprog=float(request.form['cprog'])
        datasci=float(request.form['datasci'])
        total_marks=(science+maths+cprog+datasci)/4
        res='result'
        
        return redirect(url_for(res,score=total_marks))



if __name__=='__main__':
    app.run(debug=True)