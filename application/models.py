from . import db

#THE CLOTH DATABASE MODEL
class Cloth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(10000))
    size = db.Column(db.String(10))
    color = db.Column(db.String(10))


#THE OUTFIT DATABASE MODEL
class Outfit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    descr = db.Column(db.String(1000))
    rating = db.Column(db.Integer)


#THE RELATION TABLE
class Outfit_Cloth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    outfitId = db.Column(db.Integer)
    clothId = db.Column(db.Integer)

    def clothname(self):
        cloth = Cloth.query.filter_by(id=self.clothId).first()
        return cloth.item