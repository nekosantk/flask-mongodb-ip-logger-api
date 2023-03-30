from . import db


class IpAccessLog(db.Document):
    ip_address = db.StringField(required=True)
    last_accessed_timestamp = db.DateTimeField()