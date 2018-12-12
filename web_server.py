from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import redirect

from database import Database, Goal

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


db = Database()


@app.route('/')
def home():
    return render_template('ugly.html')


@app.route('/goal', methods=['POST'])
def goal():
    goal = Goal(
        activity=request.form['activity'],
        quantity=int(request.form['quantity']),
        metric=request.form['metric'],
        period=request.form['period'],
    )
    db.add_goal(goal)
    return redirect(url_for('goals'))


@app.route('/goals')
def goals():
    return render_template('goals.html', goals=db.goals)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
