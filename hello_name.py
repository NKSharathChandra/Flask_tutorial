# Example for adding a variable rule part in the route function
# from flask import Flask
# app = Flask(__name__)

# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name

# if __name__ == '__main__':
#    app.run(debug = True)


#Example for adding variable datatypes in variable part
from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()