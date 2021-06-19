import csv

def main():
    students_dictionary = read_file("students.csv")
    while True:
        i_number = input("What is the I-number? ")
        try:
            students_dictionary[i_number]
            break
        except(KeyError):
            print("No such student.")
    print(students_dictionary.get(i_number))



def read_file(filename):
    students_dictionary = {}
    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key_Inumber= row[0]
            values_student_names = row[1]
            students_dictionary.update({key_Inumber : values_student_names})
    print(students_dictionary)       
    return students_dictionary

main()