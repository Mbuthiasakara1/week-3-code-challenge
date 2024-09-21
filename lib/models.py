#!/usr/bin/env python3
from sqlalchemy import create_engine

from sqlalchemy import Column,String,Integer,ForeignKey,Table
from sqlalchemy.orm import relationship,backref,sessionmaker,declarative_base

engine = create_engine('sqlite:///concert.db')
Session = sessionmaker(bind=engine)
session = Session()


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
    concerts=relationship('Concert',backref=backref('band'))#a single band can perform in many concerts

    def play_in_venue(self,venue,date):
        #create a new concert
        new_concert =Concert(band_id=self.id,venue_id=venue.id,date=date)
        session.add(new_concert)
        session.commit()
        return new_concert#return the new concert we have created
    
    def all_introductions(self):#retrieves all the concerts where this band has played 
        # List to store all introductions
        introductions = []

        
        for concert in self.concerts:
           
            introductions.append(concert.introduction())

        
        return introductions
    
    @classmethod
    def band_with_most_concerts(cls):
        bands= session.query(cls).all()
        concerts_counts={band: len(band.concerts) for band in bands} 
        most_active = max(concerts_counts,key=concerts_counts.get)if concerts_counts else None

        return most_active


    def __repr__(self):
        return (f"<Band id={self.id},name={self.name},hometown={self.hometown}>")


    

    
class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    bands= relationship('Band', secondary=band_venue, back_populates='venues')
    concerts=relationship('Concert',backref=backref('venue'))


    def concert_on(self,date):#search for the first concert scheduled at a venue on that specific date
        return session.query(Concert).filter_by(venue_id=self.id, date=date).first()
    

    def most_frequent_band(self):
        band_count = {}#the keys in this dict will be the band instances

        
        for concert in self.concerts:
            band = concert.get_band()
            if band:
                band_count[band] = band_count.get(band, 0) + 1

       
        most_frequent_band = max(band_count, key=band_count.get)

        return most_frequent_band


   

    def __repr__(self):
        return (f"<Venue id={self.id},title={self.title},city={self.city}>")
    
    




class Concert(Base):
    __tablename__ ="concerts"  

    id=Column(Integer(),primary_key=True) 
    date=Column(String())


    band_id =Column(Integer(),ForeignKey('bands.id'))
    venue_id=Column(Integer(),ForeignKey('venues.id'))

    def get_band(self):
        return session.query(Band).filter_by(id=self.band_id).first()
    
    def get_venue(self):
        return session.query(Venue).filter_by(id=self.venue_id).first()
    
    def hometown_show(self):
        band=self.get_band()
        venue=self.get_venue()

        if band and venue:
            return venue.city == band.hometown
    def introduction(self):#creates a custom message for the band at a specific concert
        band = self.get_band()
        venue = self.get_venue()
        
        # Check if both band and venue exist
        if band and venue:
            return (f"Hello {venue.city}!!!!! We are {band.name} and we're from {band.hometown}")
        
        return "Band or Venue not found"
    


    
    def __repr__(self):
        return(f"<Concert id={self.id},band_id={self.band_id},venue_id={self.venue_id},date={self.date}>")

    

    
    