from flask import Flask
HelloApp = Flask(__name__)

# @HelloApp.route('/hello')
def hello():
    msg = "Hello Word!!!!1"
    return msg

@HelloApp.route('/blog')
@HelloApp.route('/blog/<int:blog_no>')
def blog(blog_no=0):
    return 'This is blog number : '+ str(blog_no)

HelloApp.add_url_rule('/hello','hello',hello)
print('Flask(__name__) : ',__name__)
if __name__ == '__main__':
    HelloApp.run(host='0.0.0.0',port=5001, debug=False)