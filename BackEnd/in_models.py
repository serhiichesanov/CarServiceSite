from datetime import datetime
from src.models import Session, User, Car, Rent, Admin

session = Session()

user1 = User(userName="abdul123",
             firstName="Abdul",
             lastName="Kavaleridze",
             email="abdul123@liamg.com",
             password="alakhakbar123",
             phone="198274389")

user2 = User(userName="1bulbik1",
             firstName="Miroslav",
             lastName="Sukhodroch",
             email="bulbazavr@oohay.com",
             password="1ya1lublu1sladko1dunut1",
             phone="1231488321")

user3 = User(userName="dizainer_stiralnikh_mashin",
             firstName="Albert",
             lastName="Kronshtein",
             email="fubaras@arigato.org",
             password="natasha1111",
             phone="1485713414145")

admin1 = Admin(userId="1",
               adminRights="3")

car1 = Car(carMark="Mersedez Benz",
           carSpeed="120",
           carNumber="666000666")

car2 = Car(carMark="Shellby",
           carSpeed="100",
           carNumber="981347591")

car3 = Car(carMark="Toyota",
           carSpeed="90",
           carNumber="18724567")

rent1 = Rent(userId="1",
             carId="1",
             amountOfHours="8",
             dateTimeOfReservation=datetime(2021, 10, 31, 12, 13, 17),
             status="2"
             )

rent2 = Rent(userId="1",
             carId="3",
             amountOfHours="12",
             dateTimeOfReservation=datetime(2021, 11, 2, 8, 7, 24),
             status="2"
             )

session = Session()

session.add(user1)
session.add(user2)
session.add(user3)
session.add(car1)
session.add(car2)
session.add(car3)
session.flush()
session.add(admin1)
session.add(rent1)
session.add(rent2)

# q = session.query(User).filter_by(userName="1bulbik1")
# q.delete()

session.commit()
# Base.metadata.create_all(engine)
