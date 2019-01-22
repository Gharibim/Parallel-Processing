'''Script to choose students who are studying Python and their GPA is 3.15 or greater'''

import collections
import multiprocessing
from pprint import pprint
import time
import os

# Structure of students information
Student = collections.namedtuple('Student', ['Name', 'ID', 'course', 'GPA'])

# Immutable data structure that represents a group of students
Students = (
    Student(Name = 'Alex First', ID = 100, course = 'Python', GPA = 4.0),
    Student(Name = 'Alec Yotoho', ID = 101, course = 'Python', GPA = 3.12),
    Student(Name = 'Brad Janthen', ID = 102, course = 'C++', GPA = 2.90),
    Student(Name = 'Ben Frankson', ID = 103, course = 'Java', GPA = 3.57),
    Student(Name = 'Timothy Kylag', ID = 104, course = 'Perel', GPA = 3.82),
    Student(Name = 'John Kandermel', ID = 105, course = 'Python', GPA = 3.59),
    Student(Name = 'Yazi Tamara', ID = 106, course = 'Go', GPA = 2.13),
    Student(Name = 'Xia Voldmann', ID = 107, course = 'C', GPA = 4.0),
    Student(Name = 'Vladimar Yodan', ID = 108, course = 'Kotlin', GPA = 3.88),
    Student(Name = 'Zara Randton', ID = 109, course = 'Python', GPA = 3.11),
    Student(Name = 'Zydan Abbricombie', ID = 110, course = 'Python', GPA = 4.0),
)

# Uncomment pprint call to print the above data structure
# pprint(Students)

def Group(student):
    ''' Group Function that processes students info
    @:param student: a tuple of a single student into
    @:return student whose name starts with A and GPA >= 3.15
    '''
    time.sleep(1) # To delay each function call 1 second
    print(os.getpid()) # To print the process id that is processing the passed tuple
    return student.course == 'Python' and student.GPA >= 3.15

# Mark the start time
start_Time = time.time()

# Using multiprocessing
pool = multiprocessing.Pool() # You can pass (processes=len(Students)) to give each tuple a specific process
multiprocessing_output = pool.map(Group, Students)

# Normal function call without multiprocessing. Uncomment to check the execution time
# output = tuple(map(Group, Students))

# Mark the processing end time
End_Time = time.time() - start_Time

# Print the result then the execution time
print(multiprocessing_output)
print(End_Time)