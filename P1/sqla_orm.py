# creation of a database table using sqlachemy orm
# import the modules
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

connection_string = "mysql+mysqlconnector://sumpylab:Su.guess.Who?"\
                    "@localhost:3306/school"
#Database engine creation
engine  = create_engine(connection_string)

#Declarative Base Class
Base = declarative_base()
#here base is the Base class from where other classess will be inherited

#3declaring a new derived class student which will be used to create a table in the database
class Student(Base):
    __tablename__ = "Student"
    student_id = Column (Integer, primary_key = True)
    name = Column(String(40), nullable = False)
    date_of_birth = Column(Date, nullable = False)


#Now let's create the table
Base.metadata.create_all(engine)
#the create_all function creates all tablesa s per the metadata
#here a table named student will be created

# as the above table is already in our database we ahve disabled the create_all function to avoid any error
# actually, if the table exists., it will not create the table again, but it is a good practice to disable the function.

#now lets create a session
Session = sessionmaker(bind=engine)
session = Session()

#Now create ana object of a student class

student = Student(name= "Ann", date_of_birth = "1985-04-12")
session.add(student)  #inserts the onject as arecorn in the student table
session.commit()  #commits the changes to the database

