# Project 1: Basic school administration tool
import csv


def write_into_csv(info_list):
    with open("student_info.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Write header only if file is empty
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "E-Mail ID"])

        writer.writerow(info_list)


if __name__ == "__main__":
    condition = True
    student_num = 1

    while condition:
        student_info = input(
            "Enter student information for student #{} in the following format "
            "(Name Age Contact_Number E-mail_ID): ".format(student_num)
        )

        # Split input
        student_info_list = student_info.split(" ")

        # Validate input length
        if len(student_info_list) != 4:
            print("❌ Invalid input format. Please enter exactly 4 values.")
            continue

        print(
            "\nThe entered information is:\n"
            "Name: {}\nAge: {}\nContact_number: {}\nE-Mail ID: {}\n"
            .format(
                student_info_list[0],
                student_info_list[1],
                student_info_list[2],
                student_info_list[3]
            )
        )

        choice_check = input("Is the entered information correct? (yes/no): ").lower()

        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input(
                "Enter (yes/no) if you want to enter information for another student: "
            ).lower()

            if condition_check == "yes":
                student_num += 1
                condition = True
            elif condition_check == "no":
                condition = False
            else:
                print("❌ Invalid choice. Exiting.")
                condition = False

        elif choice_check == "no":
            print("\nPlease re-enter the values!\n")

        else:
            print("❌ Invalid choice. Please type yes or no.")
