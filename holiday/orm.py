from models.db_session import global_init, create_session
from models.__all_models import *

global_init('sqlite:///db/holiday.db')

session = create_session()
client = Client(full_name="Chel 1", phone="88005553535", email='sobaka@sobaka.com')
session.add(client)
session.commit()
