#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column,String,Integer,ForeignKey,Table
from sqlalchemy.orm import relationship,backref

engine = create_engine('sqlite:///concert.db')

Base = declarative_base()

band_venue=Table(
    'band_venue',
    Base.metadata,
    Column('band_id', ForeignKey('bands.id'), primary_key=True),
    Column('venue_id', ForeignKey('venues.id'), primary_key=True),
    extend_existing=True,
    )

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    hometown = Column(String())
    venues = relationship('Venue', secondary=band_venue, back_populates='bands')
    concerts=relationship('Concert',backref=backref('band'))

    def __repr__(self):
        return (f"<Band id={self.id},name={self.name},hometown={self.hometown}>")


    

    
class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    bands= relationship('Band', secondary=band_venue, back_populates='venues')
    concerts=relationship('Concert',backref=backref('venue'))

    def __repr__(self):
        return (f"<Venue id={self.id},title={self.title},city={self.city}>")
    
    




class Concert(Base):
    __tablename__ ="concerts"  

    id=Column(Integer(),primary_key=True) 
    date=Column(String())


    band_id =Column(Integer(),ForeignKey('bands.id'))
    venue_id=Column(Integer(),ForeignKey('venues.id'))

    def __repr__(self):
        return(f"<Concert id={self.id},band_id={self.band_id},venue_id={self.venue_id},date={self.date}>")
    
    