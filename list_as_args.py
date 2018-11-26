class Instructor:
    def __init__(self, instructor_name, experience, technology_skill, avg_feedback):
        self.__instructor_name = instructor_name
        self.__experience = experience
        self.__technology_skill = 0
        for i in technology_skill:
            self.__technology_skill[i] = technology_skill
        self.__avg_feedback = avg_feedback

    def check_eligibility(self):
        if self.__experience > 3 & self.__avg_feedback >= 4.5:
            self.allocate()
        else:
            print("Cannot allocate a course!!!")

    def allocate(self):
        print("Allocated- ")
        for i in self.__technology_skill:
            print(self.__technology_skill[i]) + "to " + self.__instructor_name


Jon = Instructor("Jon", 5.7, ["Science", "Math"], 6)
Jon.check_eligibility()
