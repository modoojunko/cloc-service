from app import db


class Repo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_update = db.Column(db.DateTime)
    domain = db.Column(db.String(80))
    group = db.Column(db.String(80))
    project = db.Column(db.String(80))

    def get_json(self):
        json = {"last_update": self.last_update,
                "domain": self.domain,
                "group": self.group,
                "project": self.project
                }

