class School:
    
    def __init__(self,name):
        self.name = name
        self.roster = {}
    
    def add_student(self,name,grade):
        if grade not in self.roster.keys():
            students = [name]
            self.roster[grade] = students
        else:
            self.roster[grade].append(name)
        
        grades = list(self.roster.keys())
        grades.sort()
        sorted_dict = {i: self.roster[i] for i in grades}
        self.roster = sorted_dict
        return self.roster

    def grade(self,grade):
        return self.roster.get(grade)
    
    def sort_roster(self):
        for key,val in self.roster.items():
            self.roster[key] = sorted(val)
        return self.roster
        