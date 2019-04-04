from flask import Flask,render_template,request
from day0404_s import func

app = Flask(__name__)

@app.route('/subject',methods=['GET','POST'])
def subject():
    sub = ''
    fname = ''
    msg = ''
    if request.method == 'POST':
        sub = request.form['sub']
        fname = func.getSubject(sub)
        if fname == 'no':
            msg = "과목을 입력해 주세요"
    return render_template('subject.html',sub=sub,fname= fname,msg=msg)

if __name__ == '__main__':
    app.run(debug=True, host='203.236.209.95')
