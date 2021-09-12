from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
import pdfkit

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#pdfkit.from_url("http://google.com", "out.pdf", configuration=config)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ships.db'
db = SQLAlchemy(app)

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

class Ships(db.Model):
    ship_id = db.Column(db.Integer(), primary_key=True)
    ship_name = db.Column(db.String(length=30), nullable=False, unique=False)
    ship_date = db.Column(db.String(length=30), nullable=False, unique=False)
    ship_time = db.Column(db.String(length=30), nullable=False, unique=False)
    ship_location = db.Column(db.String(length=30), nullable=False, unique=False)
    ship_charterer = db.Column(db.String(length=30), nullable=False, unique=False)

    def __repr__(self):
        return f'Ship {self.ship_name}'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/report", methods=["POST", "GET"])
def report():
    if request.method == "POST":
        ship_id = request.form["ship_id"]
        ship_name = request.form["ship_id"]
        ship_date = request.form["ship_date"]
        ship_time =request.form["ship_time"]
        ship_location = request.form["ship_location"]
        ship_charterer = request.form["ship_charterer"]

        ship = Ships(ship_id=ship_id, ship_name=ship_name, 
                    ship_date=ship_date, ship_time=ship_time, 
                    ship_location=ship_location, ship_charterer=ship_charterer)
                    
        db.session.add(ship)
        db.session.commit()
        return redirect(url_for("pdf_template", 
            ship_id=ship_id, ship_name=ship_name, ship_date=ship_date, 
            ship_time=ship_time, ship_location=ship_location, ship_charterer=ship_charterer))
    else:
        return render_template('report.html')


@app.route('/<ship_id>/<ship_name>/<ship_date>/<ship_time>/<ship_location>/<ship_charterer>/') #http://localhost:5000/alvin/565464#
def pdf_template(ship_id, ship_name, ship_date, ship_time, ship_location, ship_charterer):
    rendered = render_template('pdf_template.html', 
        ship_id=ship_id, ship_name=ship_name, ship_date=ship_date, 
        ship_time=ship_time, ship_location=ship_location, ship_charterer=ship_charterer)
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response


@app.route('/history')
def history():
    ships = Ships.query.all()
    # ships=[
    #     {'ship_id':"762415", 'ship_name':"Yamato", 'ship_date':"01/04/96",'ship_time': "06:00:00",'ship_location': "Japan",'ship_charterer': "Nippon Shipping"},
    #     {'ship_id':"762415", 'ship_name':"Yamato", 'ship_date':"01/04/96",'ship_time': "06:00:00",'ship_location': "Japan",'ship_charterer': "Nippon Shipping"}
    # ]
    return render_template('historical.html', ships=ships)

if __name__ == '__main__':
    app.run(debug=True)