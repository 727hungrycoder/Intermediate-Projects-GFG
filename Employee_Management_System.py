import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost", user="root", password="password", database="emp"
    )

    def check_employee(employee_id):
        try:
            sql = "SELECT * FROM `Employee Record` WHERE id = %s"
            c = con.cursor(buffered=True)
            c.execute(sql, (employee_id,))
            r = c.rowcount
            if r == 1:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def Add_Employ():
        try:
            Id = input("Enter Employee Id : ")
            if check_employee(Id):
                print("Employee already exists\nTry Again\n")
                menu()
            else:
                Name = input("Enter Employee Name : ")
                Post = input("Enter Employee Post : ")
                Salary = input("Enter Employee Salary : ")
                data = (Id, Name, Post, Salary)
                sql = "INSERT INTO `Employee Record` (id, name, post, salary) VALUES (%s, %s, %s, %s)"
                c = con.cursor()
                c.execute(sql, data)
                con.commit()
                print("Employee Added Successfully ")
                menu()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            menu()

    def Remove_Employ():
        try:
            Id = input("Enter Employee Id : ")
            if check_employee(Id) == False:
                print("Employee does not exist\nTry Again\n")
                menu()
            else:
                sql = "DELETE FROM `Employee Record` WHERE id = %s"
                c = con.cursor()
                c.execute(sql, (Id,))
                con.commit()
                print("Employee Removed")
                menu()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            menu()

    def Promote_Employee():
        try:
            Id = int(input("Enter Employee's Id: "))
            if check_employee(Id) == False:
                print("Employee does not exist\nTry Again\n")
                menu()
            else:
                Amount = int(input("Enter increase in Salary: "))
                sql = "SELECT salary FROM `Employee Record` WHERE id = %s"
                c = con.cursor()
                c.execute(sql, (Id,))
                r = c.fetchone()
                new_salary = r[0] + Amount
                update_sql = "UPDATE `Employee Record` SET salary = %s WHERE id = %s"
                c.execute(update_sql, (new_salary, Id))
                con.commit()
                print("Employee Promoted")
                menu()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            menu()

    def Display_Employees():
        try:
            sql = "SELECT * FROM `Employee Record`"
            c = con.cursor()
            c.execute(sql)
            employees = c.fetchall()
            for emp in employees:
                print("Employee Id : ", emp[0])
                print("Employee Name : ", emp[1])
                print("Employee Post : ", emp[2])
                print("Employee Salary : ", emp[3])
                print("-------------------------------------")
            menu()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            menu()

    def menu():
        try:
            print("Welcome to Employee Management Record")
            print("Press ")
            print("1 to Add Employee")
            print("2 to Remove Employee ")
            print("3 to Promote Employee")
            print("4 to Display Employees")
            print("5 to Exit")
            ch = int(input("Enter your Choice "))
            if ch == 1:
                Add_Employ()
            elif ch == 2:
                Remove_Employ()
            elif ch == 3:
                Promote_Employee()
            elif ch == 4:
                Display_Employees()
            elif ch == 5:
                exit(0)
            else:
                print("Invalid Choice")
                menu()
        except ValueError:
            print("Invalid input! Please enter a valid choice.")
            menu()

    menu()

except mysql.connector.Error as err:
    print(f"Error: {err}")
