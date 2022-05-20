from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa los operadores and


from genera_base import Pais 



engine = create_engine('sqlite:///paises.db')


Session = sessionmaker(bind=engine)
session = Session()

# Presentación de los lenguajes de cada pais
paises = session.query(Pais).all()

print("Presentación de los lenguajes de cada pais")
paises = session.query(Pais.nombre, Pais.lenguajes).all()
print(paises)