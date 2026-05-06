from Project import database, app
from Project.models import Usuario, Foto

with app.app_context(): 
    database.create_all()