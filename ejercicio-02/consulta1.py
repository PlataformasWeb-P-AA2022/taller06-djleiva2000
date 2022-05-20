from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa los operadores and

from genera_base import Pais 

engine = create_engine('sqlite:///paises.db')


Session = sessionmaker(bind=engine)
session = Session()

#  1: Presentar todos los países del continente americano

paises = session.query(Pais).all()

print("Presentación de todos los paises del continente americano")
paises = session.query(Pais).filter(or_(Pais.continente=="NA", Pais.continente=="SA")).all()
print("\n",paises)

