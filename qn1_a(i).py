def cal_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 50:
        return 'E'
    else:
        return 'Fail'

def main():
    while True:
        try:
            percentage = float(input("Enter the student's percentage: "))
            if percentage < 0 or percentage > 100:
                print("Percentage should be between 0 and 100.")
            else:
                grade = cal_grade(percentage)
                print(f"The student's grade is: {grade}")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "_main_":
    main()
