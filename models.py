from flask_mongoalchemy import MongoAlchemy

db = MongoAlchemy()

class CustomField(db.Document):
    label = db.StringField()
    required = db.BoolField()
    type = db.EnumField(db.StringField(), 'Text', 'Enum', 'Number', 'Date')
    val = db.AnythingField()


class RiskType(db.Document):
    name = db.StringField()
    fields = db.ListField(db.DocumentField(CustomField))
