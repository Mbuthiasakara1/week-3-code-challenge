from models import session,Band,Venue,Concert

def main():
     # Test for Concert band()
    concerts_bands=session.query(Concert).all()
    print("Concerts and their Bands and Venues:")
    print("=" * 40)
    for concert in concerts_bands:
       print(concert.get_band())

      #Test for Concert venue()
       print(concert.get_venue())
       
     #Test Venue concerts()
    venues= session.query(Venue).all()
    print("Venues and their Concerts and Bands :")
    print("=" * 40)
    for venue in venues:
      print(venue.concerts)  

      #Test for Venue bands()
      print(venue.bands)  


    #Test for Band Concerts()
    bands=session.query(Band).all()
    print("Bands and their Concerts and Venues:")
    print("=" * 40)
    for band in bands:
       print(band.concerts)
       #Test for Band venues()
       print(band.venues)

    # Aggregate and Relationship Methods
    #Test for Concert hometown_show()

    concert_in_hometown=session.query(Concert).first() 
    print("True")if concert_in_hometown.hometown_show() else print("False")#output{false}
     
     #Test Concert introduction()
    concert_message = session.query(Concert).first()#output{Hello Sanchezmouth!!!!! We are Kevin Howard and we're from Antonioside}
    print(concert_message.introduction())


    # #Band
    # #Test Band play_in_venue(venue, date)
    band=session.query(Band).filter_by(name="John Ruiz").first()
    venue=session.query(Venue).filter_by(title="Wang LLC").first()
    new_concert=band.play_in_venue(venue,'2024-09-21')
    print(new_concert)#output new_concert{<Concert id=25,band_id=4,venue_id=2,date=2024-09-21>}

    # #Test Band all_introductions()
    band = session.query(Band).filter_by(name='Shirley Martinez').first()
    introductions = band.all_introductions()

    for i in introductions:
      print(i)#output{Hello Evansfurt!!!!! We are Shirley Martinez and we're from Bennettshire}

    # # Test for Band most_performances()
    most_active= Band.band_with_most_concerts()

    if most_active:
     print(f"The band with the most concerts is: {most_active.name} from {most_active.hometown}")
    else:
     print("No bands found in the database.")#output{The band with the most concerts is: John Ruiz from New Erin}


    # #  Test for Venue concert_on(date)
    venue=session.query(Venue).filter_by(title='Weaver-Ford').first()
    date_check='1989-12-13'
    concert=venue.concert_on(date_check)

    if concert:
        print(f"{concert}")#output{<Concert id=18,band_id=18,venue_id=4,date=1989-12-13>}
    else:

      print("No concert scheduled on {date_check}")


    # #Test for Venue most_frequent_band()
    venue=session.query(Venue).filter_by(title='Gentry-Patrick').first()
    if venue:
         frequent_band=venue.most_frequent_band()
         print(f"{frequent_band.name}"if frequent_band else "No bands found")#output{John Ruiz}
    
        



    

if __name__ == "__main__":
    main()   