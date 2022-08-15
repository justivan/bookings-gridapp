from flask import render_template, jsonify, request, abort
from app import app, db
from .models import Booking


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api/data')
def data():
    query = Booking.query.order_by(Booking.hotel_name, Booking.in_date)

    return {
        'data': [bkg.to_dict for bkg in query]
    }
