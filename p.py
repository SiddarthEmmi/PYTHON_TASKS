import pandas as pd
import sys
class FeesManagementSystem:
    def __init__(self, file_name="student.xlsx"):
        self.file_name = file_name
        self.load_excel()

    def view(self):
        if self.students.empty:
            print("No students available. Please add students first.")
            self.admin()
            return

        for index, row in self.students.iterrows():
            self.sdetails(index + 1, row)

    def susn(self):
        if self.students.empty:
            print("No students available. Please add students first.")
            self.admin()
            return

        usn = input("Enter USN to search: ")
        found = self.students[self.students["USN"] == usn]
        if not found.empty:
            self.sdetails(found.index[0] + 1, found.iloc[0])
        else:
            print(f"No Student found with USN: {usn}")
            self.admin()

    def add_student(self):
        name = input("Enter Name: ")
        usn = input("Enter USN: ")
        branch = input("Enter Branch: ")
        yr = int(input("Enter Admission yr: "))
        dob=input("Enter DOB:")
        seat=input("Enter seat category(K-CET/MGMT): ")
        
        

        new_student = pd.DataFrame({"Name": [name], "USN": [usn], "branch": [branch], "Admission yr": [yr], "Seat":[seat],"DOB":[dob]})
        self.students = pd.concat([self.students, new_student], ignore_index=True)
        self.save_to_excel()
        self.admin()

    def save_to_excel(self):
        self.students.to_excel(self.file_name, index=False)
        print(f"Student details saved to {self.file_name}")

    def load_excel(self):
        try:
            self.students = pd.read_excel(self.file_name)
            if "Remaining Balance" not in self.students.columns:
                self.students["Remaining Balance"] = 0  
            print(f"Student details loaded from {self.file_name}")
        except FileNotFoundError:
            self.students = pd.DataFrame(columns=["Name", "USN", "branch", "Admission yr", "DOB", "Seat", "Remaining Balance"])
            print(f"File {self.file_name} not found. Created an empty student DataFrame.")



    def dusn(self):
        if self.students.empty:
            print("No students available. Please add students first.")
            self.admin()
            return

        dusn = input("Enter USN to delete: ")
        self.students = self.students[self.students["USN"] != dusn]
        print(f"Student with USN {dusn} deleted successfully.")
    
        self.save_to_excel()
    
        self.admin()


    def payment(self):
        if self.students.empty:
            print("No students available. Please add students first.")
            self.admin()
            return

        usn = input("Enter USN for payment: ")
        student = self.students[self.students["USN"] == usn]

        if not student.empty:
            seat_category = student.iloc[0]["Seat"]
            if seat_category == "K-CET":
                original_amount = 83526
            elif seat_category == "MGMT":
                original_amount = 300000
            else:
                print("Invalid seat category.")
                self.admin()
                return

            if "Remaining Balance" not in self.students.columns:
                self.students["Remaining Balance"] = 0  

            remaining_balance = student.iloc[0]["Remaining Balance"]

            print(f"Total amount to pay: Rs.{original_amount}")
            print(f"Remaining balance: Rs.{remaining_balance}")

            pay_option = input("Do you want to pay? (yes/no): ").lower()
            if pay_option == "yes":
                amount_paid = float(input("Enter the amount you want to pay: "))
                d=original_amount-amount_paid
                print(f"Amount paid is: Rs.{amount_paid}")
                print(f"Payment successful! Remaining balance: Rs.{d}")

                self.students.loc[self.students["USN"] == usn, "Remaining Balance"] = d
                self.save_to_excel()

            # Check if the remaining balance is zero and reset it to the original amount
                if d == 0:
                    print("Remaining balance is zero. Resetting to total amount.")
                    self.students.loc[self.students["USN"] == usn, "Remaining Balance"] = original_amount
                    self.save_to_excel()

            elif pay_option == "no":
                print("Payment canceled.")
            self.admin()
        else:
            print(f"No Student found with USN: {usn}")
            self.admin()



            
    def admin(self):
        print("1. Add student")
        print("2. View all students")
        print("3. Search by USN")
        print("4. Delete student")
        print("5. Payment")
        print("6. Exit")

        ch = input("Enter your choice: ")
        if ch == "1":
            self.add_student()
        elif ch == "2":
            self.view()
            self.admin()
        elif ch == "3":
            self.susn()
            self.admin()
        elif ch == "4":
            self.dusn()
            self.admin()
        elif ch=="5":
            self.payment()
        elif ch == "6":
            FeesManagementSystem.main()
        else:
            print("Incorrect Choice")
            self.admin()

    def sdetails(self, student_id, details):
        print(f"Student ID: {student_id}")
        print(f"Name: {details['Name']}")
        print(f"USN: {details['USN']}")
        print(f"Branch: {details['branch']}")
        print(f"Admission Year: {details['Admission yr']}")
        print(f"DOB:{details['DOB']}")
        print(f"Seat:{details['Seat']}\n")
        
    
            
    def user(self):
        if self.students.empty:
            print("No students available. Please add students first.")
            FeesManagementSystem.main()
            return

        usn = input("Enter USN: ")
        pas = input("Enter DOB: ")

        found = self.students[(self.students["USN"] == usn) & (self.students["DOB"] == pas)]
        if not found.empty:
            self.sdetails(found.index[0] + 1, found.iloc[0])
            FeesManagementSystem.main()
        else:
            print(f"No Student found with USN: {usn}")
            FeesManagementSystem.main()

    def main():
        print("1. Admin")
        print("2. Student")
        c = input("Enter your choice: ")
        if c == "1":
            FeesManagementSystem.login()
        elif c == "2":
            o.user()  
        else:
            print("Incorrect Choice")
            FeesManagementSystem.main()

    def login():
        username = input("Enter UserName: ")
        password = input("Enter password: ")
        if username == "Sidd" and password == "1234":
            o.admin()  
        else:
            print("Incorrect username or login")
            FeesManagementSystem.main()

o = FeesManagementSystem()
FeesManagementSystem.main()
o.susn()
