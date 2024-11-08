
import random

def read_student_ids(file):
    
    try:
        with open(file, 'r') as f:
            student_ids = [line.strip() for line in f if line.strip()]

        if not student_ids:
            print("Error: The file is empty. Please add student IDs.")
            return None
        
        return student_ids
    
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found. Please check the file name and try again.")
        return None


def select_students(file):

    all_students = read_student_ids(file)

    if all_students is None:
        return  

    unselected_students = all_students[:]
    viva_counter = 1

    print("\nStarting viva selection process...\n")

    while True:
        if not unselected_students:
            print("All students have been selected once.")
            unselected_students = all_students[:]
            viva_counter = 1 
            input("Press Enter to start a new selection round...")

        selected_student = random.choice(unselected_students)
        unselected_students.remove(selected_student)

        print(f"Viva #{viva_counter}: Selected student - {selected_student}")
        viva_counter += 1

def main():
    file = 'student.txt'
    select_students(file)


main()
