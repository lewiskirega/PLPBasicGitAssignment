def is_in_school(student, school):

    if student in school:
        return True
    else:
        return False

school=["Alice", "Bob", "Carol"]
print(is_in_school("Alice", school))
print(is_in_school("David", school))

