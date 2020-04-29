courses = dict()
with open("text_6.txt", encoding="UTF-8") as cool:
    for line in cool.readlines():
        line = line.strip()
        course_name = line[0:line.index(":")]
        course_info = line[line.index(":"):].strip()
        course_info = "".join([x for x in course_info if x.isspace() or x.isdigit()])
        course_lessons = sum(map(int, course_info.strip().split()))
        courses[course_name] = course_lessons

print(courses)