class Job(object):
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary 
    def job_intro(self):
        meg = "The job is "
        meg += self.name
        return meg

    def job_detailed(self):
        meg = "The salary of" + self.job_intro()
        meg += "is" + self.salary + "."
        return meg

name = "Teacher" 
salary = "5000"
teacher = Job(name=name, salary=salary)

print(teacher.job_detailed())
