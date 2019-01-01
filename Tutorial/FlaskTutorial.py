from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/home')
def my_name():
    return 'My name is the Name Thingy'

def tutorial_test1():
    return 'This is a Tutorial'
app.add_url_rule('/tutorial', 'tutorial', tutorial_test1)

#@app.route('/<name>')
#def my_name2(name):
#    return 'My name is %s' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

@app.route('/admin')
def hello_admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as guest' % guest

@app.route('/<name>')
def hello_welcome(name):
    return 'Welcome back %s' % name

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
        print('inside if admin')
        return redirect(url_for('hello_admin'))
   else:
        print('inside else admin')
        return redirect(url_for('hello_welcome', name = name))

if __name__ == '__main__':
    app.run(debug = True)