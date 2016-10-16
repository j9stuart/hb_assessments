"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
        The first advantage is called abstraction which allows a user to run a method without having to understand the details of the source code or implementation.
        The second advantage is called encapsulation, which makes it easier to attain facts about the data and functions since they're stored in single unit. 
        The third advantage is polymorphism which provides flexibility as methods & objects can be processed differently depending on their type. 

2. What is a class?
        A class is essentially a template or how-to-guide that describes how to use, create, and implement a set of objects. 

3. What is an instance attribute?
        An instance attribute is a characteristic of a particular object in a class. For example, the "dog" instance in the class "animal" can have the attribute "name".

4. What is a method?
        A method is a procedure or function that is defined as part of a class and can be used by any object of that class.

5. What is an instance in object orientation?
        An instance is a specific representation or example of an object in a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
        A class attribute is a characteristic that is given to every object within the class, while an instance attribute is for a particular object within the class.
        You may use a class attribute of "sole" for all shoes, but use the instance attribute "straps" for sandals, since not all shoes have straps. 


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def create_student_dict(self):
        student_dict = {"first name": self.first_name, 
                        "last name": self.last_name, 
                        "address": self.address}
        return student_dict


class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def create_question_dict(self):
        question_dict = {"question": self.question, 
                         "correct_answer": self.correct_answer}
        return question_dict

    def ask_and_evaulate(self):
        answer = raw_input(self.question)
        return answer == self.correct_answer


class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []
        
    def exam_storage(self):
        exam_dict += {'name': self.name, 
                     'questions': self.questions
                        }
        return exam_dict

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        score = 0
        for question in self.questions:
            score += question.ask_and_evaulate()
        return score

class Quiz(Exam):

    def administer(self):
        score = super(Quiz, self).administer()
        percentage = float(score)/len(self.questions)
        return percentage >= .5


def take_test(exam, student):
    """ Takes instance of an exam and instance of a student
    """
    student_score = exam.administer()

    student.score = student_score

    print student_score

def example():

    exam = Exam("exam")

    exam.add_question("Who is the best student at Hackbright?", "Cephra Stuart")
    exam.add_question("Who is the best basketball player on Earth?", "Lebron James")
    exam.add_question("What is the best programming language?", "Python")

    henry = Student("Henry", "Chen", "San Francisco, CA")

    take_test(exam, henry)



