# 功課表設計範例

class Course:
    def __init__(self, name, teacher, time):
        self.name = name
        self.teacher = teacher
        self.time = time

class Timetable:
    def __init__(self):
        self.schedule = {}

    def add_course(self, day, course):
        if day not in self.schedule:
            self.schedule[day] = []
        self.schedule[day].append(course)

    def display(self):
        for day, courses in self.schedule.items():
            print(f"{day}:")
            for c in courses:
                print(f"  {c.time} - {c.name} ({c.teacher})")
            print()

# 範例使用
timetable = Timetable()
timetable.add_course("星期一", Course("數學", "王老師", "08:00-09:00"))
timetable.add_course("星期一", Course("英文", "李老師", "09:10-10:10"))
timetable.add_course("星期二", Course("自然", "陳老師", "08:00-09:00"))
timetable.add_course("星期三", Course("社會", "張老師", "10:20-11:20"))

timetable.display()