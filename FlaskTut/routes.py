from maritime import app
from flask import render_template, request, redirect, url_for, make_response
from maritime.models import Ships
from maritime import db
import pdfkit

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


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

        ship = Ships(request.form["ship_id"], request.form["ship_name"],
                    request.form["ship_date"],request.form["ship_time"],
                    request.form["ship_location"],request.form["ship_charterer"] )
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
    return render_template('historical.html', ships=ships)