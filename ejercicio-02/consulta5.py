from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa los operadores and

from genera_base import Pais 


engine = create_engine('sqlite:///paises.db')


Session = sessionmaker(bind=engine)
session = Session()

#Presentar todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito'
paises = session.query(Pais).all()

print("Presentar todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito'")
paises = session.query(Pais).filter(or_(Pais.nombre.like("%uador%"), Pais.capital.like("%ito%"))).order_by(Pais.capital).all()
print(paises)