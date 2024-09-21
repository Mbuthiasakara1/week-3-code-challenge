from models import Band,Venue,Concert,session,band_venue
from faker import Faker
import random
fake =Faker()


if __name__ == '__main__':
    session.query(Band).delete()
    session.query(Venue).delete()
    session.query(Concert).delete()
    session.query(band_venue).delete()
    session.commit()


    bands =[]
    for i in range(30):
        band = Band (
            name= fake.name(),
            hometown=fake.city()
        )
        bands.append(band)
    session.add_all(bands) 
    session.commit()

    venues =[]  
    for i in range(10):
        venue = Venue(
            title=fake.company(),
            city=fake.city()
       )
        venues.append(venue)
    session.add_all(venues)
    session.commit()

    for band in bands:
        band.venues = random.sample(venues,random.randint(1,4))
    session.commit()    

    concerts=[]
    for i in range(20):
        concert =Concert(
            date = fake.date(),
            band_id=fake.random_element(bands).id,
            venue_id=fake.random_element(venues).id
        )
        concerts.append(concert)
    session.add_all(concerts) 
    session.commit() 

    print("database seeded!")  
        
        
        