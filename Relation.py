from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import Session,declarative_base,relationship

engine = create_engine("sqlite:///Relation.db")
Base = declarative_base()

class Doctors(Base):
    __tablename__ = "doctors"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    disease_treating = Column(String)
    patients = relationship("Patients",back_populates = "doctors")

class Patients(Base):
    __tablename__ = "patients"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    disease = Column(String)
    doctor_id = Column(Integer,ForeignKey("doctors.id"))
    doctors = relationship("Doctors",back_populates="patients")

Base.metadata.create_all(engine)
session =Session(engine)
doc1 = Doctors(name = "Kimani Dennis",disease_treating ="Diabetes")
p1 = Patients(id = 1,name = "Aden ceil",disease = "Diabetes",doctor_id=doc1.id)
session.add_all([doc1,p1])
session.commit()



