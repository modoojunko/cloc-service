from app import db, models
from datetime import datetime

## remove db first

db.drop_all()

## init db

db.create_all()

## insert data

dt=datetime.now()
test_data = models.Repo(last_update=dt.strftime('%Y%m%d%H%M%S'),
                        domain="www.github.com",
                        group="modeoojunko",
                        project="modoojunko"
                        )

db.session.add(test_data)
db.session.commit()

## query data

update_data = models.Repo.query.filter_by(domain="www.github.com").first()
update_data.project = "zhuke"
db.session.commit()

## delete data

delete_data = models.Repo.query.filter_by(project="zhuke").first()
db.session.delete(delete_data)
db.session.commit()

## drop all data

db.drop_all()
