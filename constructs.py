from flask import Flask, render_template
app=Flask(__name__)

@app.route('/<float:marks>')
def hello_name(marks):
    return render_template('pass.html',m=marks)

if __name__=='__main__':
    app.run(debug=True)