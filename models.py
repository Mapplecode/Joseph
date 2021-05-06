from app import db

class filestorage(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    filename = db.Column(db.String(500))
    ftype = db.Column(db.String(50))  
    created_date = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, filename, ftype, created_date):
        self.filename = filename
        self.ftype = ftype
        self.created_date = created_date