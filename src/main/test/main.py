from Student import Student

def main():
    # Create student objects
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student4 = Student()
    student5 = Student()
    student6 = Student()
    student7 = Student()
    student8 = Student()
    student9 = Student()
    student10 = Student()
    
    student1.name = "Madhu"
    student1.age = 21
    student1.grade = "A"
    student1.dob = ("2002-04-15")  # Example DOB
    
    student2.name = "Aishu"
    student2.age = 20
    student2.grade = "A"
    student2.dob = ("2003-05-20")
    
    student3.name = "Monica"
    student3.age = 22
    student3.grade = "B"
    student3.dob = ("2001-02-10")
    
    # Add more students as required
    student4.name = "Aswi"
    student4.age = 19
    student4.grade = "C"
    student4.dob = ("2004-07-01")
    
    student5.name = "Jeeva"
    student5.age = 23
    student5.grade = "B"
    student5.dob = ("2000-12-30")
    
    student6.name = "Ilan"
    student6.age = 18
    student6.grade = "A"
    student6.dob = ("2005-11-11")
    
    student7.name = "Ani"
    student7.age = 21
    student7.grade = "B"
    student7.dob = ("2002-08-05")
    
    student8.name = "Rithikaa"
    student8.age = 22
    student8.grade = "A"
    student8.dob = ("2001-03-18")
    
    student9.name = "Sumi"
    student9.age = 20
    student9.grade = "B"
    student9.dob = ("2003-01-25")
    
    student10.name = "Vinitha"
    student10.age = 21
    student10.grade = "A"
    student10.dob = ("2002-06-10")
    
    # Display student information
    print("Student Information:")
    student1.display_info()
    student2.display_info()

    # Creating list of students
    student_tuples = [
        ("Madhu", student1), ("Aishu", student2), ("Monica", student3),
        ("Aswi", student4), ("Jeeva", student5), ("Ilan", student6),
        ("Ani", student7), ("Rithikaa", student8), ("Sumi", student9),
        ("Vinitha", student10)
    ]
    
    for name, student in student_tuples:
        print(f"Tuple Key (Name): {name}")
        student.display_info()

    # Creating dictionary of students
    student_dict = {
        "Madhu": student1, "Aishu": student2, "Monica": student3,
        "Aswi": student4, "Jeeva": student5, "Ilan": student6,
        "Ani": student7, "Rithikaa": student8, "Sumi": student9,
        "Vinitha": student10
    }

    for name, student in student_dict.items():
        print(f"  Dictionary Key (Name): {name}")
        student.display_info()

    # Input from user to filter names by the first letter
    input_letter = input("Enter a letter to filter names by the first letter: ").strip().upper()
    filtered_students_by_letter = {
        key: value for key, value in student_dict.items() if key.upper().startswith(input_letter)
    }
    
    if filtered_students_by_letter:
        print(f"Students with names starting with '{input_letter}':")
        for name, details in filtered_students_by_letter.items():
            print(f"Name: {name}")
    else:
        print(f"No students found with names starting with '{input_letter}'.")

    # Input from user to filter by age (below the given age)
    try:
        input_age = int(input("Enter an age to filter students who are below that age: ").strip())
        
        # Filter dictionary by students whose age is less than the input age
        filtered_students_by_age = {
            key: value for key, value in student_dict.items() if value.age < input_age
        }
        
        if filtered_students_by_age:
            print(f"Students with age below '{input_age}':")
            for name, details in filtered_students_by_age.items():
                print(f"Name: {name}")
                details.display_info()
        else:
            print(f"No students found below the age of '{input_age}'.")
    
    except ValueError:
        print("Please enter a valid numeric age.")

    # Input from user to filter by birth year
    try:
        input_year = int(input("Enter a birth year to filter students born before that year: ").strip())
        
        # Filter dictionary by students whose birth year is before the input year
        filtered_students_by_year = {
            key: value for key, value in student_dict.items() if value.dob.year < input_year
        }
        
        if filtered_students_by_year:
            print(f"Students born before the year '{input_year}':")
            for name, details in filtered_students_by_year.items():
                print(f"Name: {name}")
                details.display_info()
        else:
            print(f"No students found born before the year '{input_year}'.")
    
    except ValueError:
        print("Please enter a valid numeric year.")

if __name__ == "__main__":
    main()
