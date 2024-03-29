from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Martin Pare! and this is also my first code change'


@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/favorite-course")
def favorite_course():
    # print("Subject entered was: " + request.args.get('subject'))
    # print("Course Number entered was: " + request.args.get('course_number'))
    return render_template('favorite-course.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

@app.route("/")

@app.route('/about-css')
def style():
    return render_template('about-css.html')

if __name__ == '__main__':
    app.run()
