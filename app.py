from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# settings
app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mypassword@127.0.0.1/contactsdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone


@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/new', methods=['POST'])
def add_contact():
    if request.method == 'POST':

        # receive data from the form
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        # create a new Contact object
        new_contact = Contact(fullname, email, phone)

        # save the object into the database
        db.session.add(new_contact)
        db.session.commit()

        flash('Contact added successfully!')

        return redirect('/')


@app.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    # get contact by Id
    print(id)
    contact = Contact.query.get(id)

    if request.method == "POST":
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('index'))

    return render_template("update.html", contact=contact)

@app.route("/delete/<id>", methods=["GET"])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for('index'))

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
