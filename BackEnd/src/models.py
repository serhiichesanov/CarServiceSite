from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, CheckConstraint, Enum, Boolean, Float

engine = create_engine("mysql+pymysql://root:sss@db_host/mydb")
engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()
BaseModel.query = Session.query_property()


class Car(BaseModel):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True)
    carMark = Column(VARCHAR(256), nullable=True)
    carSpeed = Column(Integer,
                      CheckConstraint("carSpeed >= 60 AND carSpeed <=120"),
                      nullable=False)
    carNumber = Column(Integer, nullable=True)


class User(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(256), nullable=True)
    firstName = Column(VARCHAR(256), nullable=True)
    lastName = Column(VARCHAR(256), nullable=True)
    email = Column(VARCHAR(256), nullable=True)
    password = Column(VARCHAR(256), nullable=True)
    phone = Column(VARCHAR(256), nullable=True)
    userStatus = Column(Boolean, nullable=True)


class Admin(BaseModel):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    userId = Column(Integer,
                    ForeignKey("user.id",
                               onupdate="CASCADE",
                               ondelete="CASCADE"),
                    unique=True,
                    nullable=True)
    adminRights = Column(Enum("employee", "managment", "owner"),
                         nullable=True)


class Rent(BaseModel):
    __tablename__ = "rent"

    id = Column(Integer, primary_key=True)
    userId = Column(Integer,
                    ForeignKey("user.id",
                               onupdate="CASCADE",
                               ondelete="CASCADE"),
                    nullable=True)
    carId = Column(Integer,
                   ForeignKey("car.id",
                              onupdate="CASCADE",
                              ondelete="CASCADE"),
                   nullable=True)
    startRent = Column(DateTime, nullable=True)
    endRent = Column(DateTime, nullable=True)
    totalPrice = Column(Float,
                    nullable=True)


BaseModel.metadata.create_all(engine)
