from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


from forms import MovieForm

app = Flask(__name__)

db = SQLAlchemy(app)


# configuring our database uri
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'any secret string'


# basic model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    timing = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(400), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/create', methods=['GET', 'POST'])
def movie_create():
    form = MovieForm()
    if form.validate_on_submit():
        movie = Movie(name=form.name.data,
                      timing=form.timing.data,
                      location=form.location.data)
        db.session.add(movie)
        db.session.commit()
        return redirect('/create')
    movie = Movie.query.all()
    return render_template('index.html', form=form, movie=movie)


@app.route("/update/<movie_id>", methods=['GET', 'POST'])
def edit_movie(movie_id):
    movie = db.session.query(Movie).get(movie_id)

    form = MovieForm(obj=movie)
    if form.validate_on_submit():
        form.populate_obj(movie)
        db.session.add(movie)
        db.session.commit()
        return redirect('/create')

    return render_template('update.html', form=form, movie=movie)


@app.route("/delete/<movie_id>", methods=['GET', 'POST'])
def delete_movie(movie_id):
    movie = db.session.query(Movie).get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect('/create')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
