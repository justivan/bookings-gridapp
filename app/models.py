from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime
from sqlalchemy import text
from app import db


class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True


@compiles(utcnow, 'postgresql')
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


@compiles(utcnow, 'mssql')
def ms_utcnow(element, compiler, **kw):
    return "GETUTCDATE()"


class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    ref_id = db.Column(db.Integer, index=True, nullable=False)
    res_id = db.Column(db.Integer, index=True, nullable=False)
    hotel_name = db.Column(db.String(100), index=True, nullable=False)
    opr_name = db.Column(db.String(10), index=True, nullable=False)
    opr_code = db.Column(db.String(10), nullable=False)
    bkg_ref = db.Column(db.String(100), index=True, nullable=False)
    guest_name = db.Column(db.String(100), nullable=False)
    import_date = db.Column(db.DateTime, index=True, nullable=False)
    sales_date = db.Column(db.DateTime, index=True, nullable=False)
    in_date = db.Column(db.DateTime, index=True, nullable=False)
    out_date = db.Column(db.DateTime, index=True, nullable=False)
    room = db.Column(db.String(100), nullable=False)
    meal = db.Column(db.String(24), nullable=False)
    days = db.Column(db.SmallInteger, nullable=False)
    adult = db.Column(db.SmallInteger, nullable=False)
    child = db.Column(db.SmallInteger, nullable=False)
    purchase = db.Column(db.Float(), nullable=False)
    sales = db.Column(db.Float(), nullable=False)
    opr_cost = db.Column(db.Float(), nullable=False, server_default=text("0"))
    statu4 = db.Column(db.String(10), nullable=False)
    gwg_p_id = db.Column(db.Integer, nullable=False)
    gwg_p_name = db.Column(db.String(100), nullable=False)
    gwg_p_code = db.Column(db.String(100), nullable=False)
    gwg_s_id = db.Column(db.Integer, nullable=False)
    gwg_s_name = db.Column(db.String(100), nullable=False)
    gwg_s_code = db.Column(db.String(100), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey(
        'status.id'), nullable=False, server_default=text("-1"))
    created_at = db.Column(db.DateTime, server_default=utcnow())
    updated_at = db.Column(
        db.DateTime, server_default=utcnow(), onupdate=utcnow())

    @property
    def to_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }


class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    bookings = db.relationship('Booking', backref='status', lazy=True)

    @property
    def to_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
        }
