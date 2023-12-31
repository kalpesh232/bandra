from flask import Flask, url_for, make_response, render_template
HelloApp = Flask(__name__)

@HelloApp.route('/')
def index():
    return 'This is index'

# @HelloApp.route('/hello')
def hello1(num):
    msg = f"Hello Word!!!!1 - {num}"
    return msg

@HelloApp.route('/blog')
@HelloApp.route('/blog/<blog_no>')
def blog(blog_no=0):
    return 'This is blog number : '+ str(blog_no)

with HelloApp.test_request_context():
    print('1 : ', url_for('index'))
    print('2 : ', url_for('blog', blog_no = 'lkkiuy fer'))
    print('3 : ', url_for('blog', blog_no = 99, blog_name = 'nine nine'))

@HelloApp.route('/about')
def about():
    header = {
        'content-type' : 'application/json'
    }
    return make_response('This is response generated by make response',200,header)

def contact():
    return render_template('index.html')
HelloApp.add_url_rule('/contact','contact',contact)
HelloApp.add_url_rule('/hello/<int:num>','hello1',hello1)

def base():
    return render_template('base.html')
HelloApp.add_url_rule('/base','base1',base)

def home():
    return render_template('home.html')
HelloApp.add_url_rule('/home','home_here',home)

def about1():
    return render_template('about.html')
HelloApp.add_url_rule('/about1','about1',about1)

def product():
    return render_template('product.html')
HelloApp.add_url_rule('/product','product',product)


# print('Flask(__name__) : ',__name__)
if __name__ == '__main__':
    HelloApp.run(host='0.0.0.0',port=5001, debug=True)