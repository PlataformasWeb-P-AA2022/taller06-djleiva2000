from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa los operadores and


from genera_base import Pais 



engine = create_engine('sqlite:///paises.db')


Session = sessionmaker(bind=engine)
session = Session()

# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
paises = session.query(Pais).all()

print("Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa")
paises = session.query(Pais).filter(Pais.continente=="EU").order_by(Pais.capital).all()
print(paises)