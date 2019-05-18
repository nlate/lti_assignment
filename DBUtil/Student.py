from models.Student import Student
from base import Base, Session

class StudentDAO():    
    def get_students(self):        
        '''
          General description:
          Args:
             no Args
          Returns:
                  Returns Database entities existing in the Students table.
          Example :
          get_student()
        '''
        session = Session()
        students = []
        student = {}
        res = session.query(Student).all()
        for data in res:
            student["name"] = data.name 
            student["id"] = data.id
            student["class_id"] = data.class_id
            student["created_on"] = data.created_on
            student["updated_on"] = data.updated_on
            students.append(student)
        return students

    def get_student_by_id(self, _id):
        '''
          General description:
          Args:
              param1 (object_id) : This is the Account Id which is stored in database
          Returns:
                  Returns Database entity of Account for the given Student Id
          Example :
              get_student_by_id(id)
        '''
        
        session = Session()
        student = {}
        response = session.query(Student).filter(Student.id == _id).first()
        student["name"] = response.name 
        student["id"] = response.id
        student["class_id"] = response.class_id
        student["created_on"] = response.created_on
        student["updated_on"] = response.updated_on
        return student
     
    def add_student(self, data):
        '''
          General description:
          Args:
              param1 (object_id) : This is the Account Id which is stored in database
          Returns:
                  Returns Database entity of Account for the given Student Id
          Example :
              get_student_by_id(id)
        '''
        session = Session()
        print("inside dao")
        print(data)
        input_obj = Student(data["id"], data["name"], data["class"], data["created_on"], data["updated_on"])
        res = session.add(input_obj)
        print(res)
        return session.commit()
    
    def update_student(self, data):
        '''
          General description:
          Args:
              param1 (object_id) : This is the Account Id which is stored in database
          Returns:
                  Returns Database entity of Account for the given Student Id
          Example :
              get_student_by_id(id)
        '''
        session = Session()
        print("inside dao")
        print(data)
        input_obj = Student(data["id"], data["name"], data["class"], data["created_on"], data["updated_on"])
        res = session.update(input_obj)
        print(res)
        return session.commit()
    
    def delete_student(self, _id):
        '''
          General description:
          Args:
              param1 (object_id) : This is the Account Id which is stored in database
          Returns:
                  Returns Database entity of Account for the given Student Id
          Example :
              get_student_by_id(id)
        '''
        session = Session()
        obj = session.query(Student).filter_by(id=_id).one()
        if obj is not None:
            res = session.delete(obj)
            session.commit()            
            if res is None:            
                return True
            else:
                return False
        else:
            return False