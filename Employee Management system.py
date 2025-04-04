# Dictionary to store employee details
employees = {}  # Fixed typo: 'employess' to 'employees'

# Function to add employee
def add_employee(emp_id, name, age, salary, department):
    employees[emp_id] = {
        "Name": name,
        "Age": age,
        "Salary": salary,
        "Department": department
    }
    print(f"Employee {name} added successfully!")

# Function to view all employees
def view_employees():  
    if employees:
        for emp_id, emp_details in employees.items():
            print(f"ID: {emp_id}, Details: {emp_details}")
    else:
        print("No employees added yet!")

# Function to update Employee Details

def update_employees(emp_id,name=None,age=None,salary=None,department=None):
    
    try:
        if emp_id in employees:
            if name:
                employees[emp_id]["Name"] = name

            if age:
                employees[emp_id]["Age"] = age

            if salary:
                employees[emp_id]["Salary"] = salary

            if department:
                employees[emp_id]["Department"] = department

            print(f"Employee {emp_id} ABM Employee Information Updated Successfully...!")

        else:
            print(f"Employee With ID{emp_id} Not Found in ABM Record")

    except KeyError as e:

        print(f"Error Updating Employee Details: {e}")


# Function to remove an Employee :

def remove_employee(emp_id):

    try:
        emp = employees.pop(emp_id)

        print(f"Employees {emp['Name']} ABM Employee Detailed Removed Successfully....!")
    
    except KeyError :

        print(f"Employee with ID {emp_id}Not Found in ABM Record")

# Function to save employee data to a file without JSON

def save_to_file(filename):
    
    try:

        with open(filename,"w") as file:

            for emp_id,details in employees.items():

                line= f"{emp_id} :->  {details['Name']},{details["Age"]},{details['Salary']},{details['Department']}\n"
                file.write(line)
        print(" ABM Employee Data Saved Successfully.....!")
    
    except Exception as e:
        print(f"Error : {e}") 

# Function to load employee data from a file without JSON

def load_from_file(filename):

    try:

        with open(filename,'r') as file:

            global employees

            employees = {} # clear the existing dictionary before loading

            for line in file:
                emp_data = line.strip().strip(',')
                emp_id,name,age,salary,department = emp_data


                employees[emp_id]={
                    "Name":name,
                    "Age":age,
                    "Salary":salary,
                    "Department":department
                }
        print("ABM Employee Data Loaded Successfully.....!")

    except FileNotFoundError:

        print(f"File {filename} not found")
    
    except Exception as e:
        print(f"Error : {e}")



# Main menu function
def menu():
    while True:
        print("\nWelcome to ABM:")
        print("1. Add Employee")
        print("2. View Employee details")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save to File")
        print("6. Load from file")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            age = input("Enter Employee Age: ")
            salary = input("Enter Employee Salary: ")
            department = input("Enter Department: ")
            add_employee(emp_id, name, age, salary, department)
        elif choice == "2":
            view_employees()  
        elif choice == "3":

            emp_id = input("Enter Employee Id: ")
            name = input("Enter New Name(Leave Blank to skip: )")or None
            age = input("Enter New Age(Leave Blank to skip: )")or None
            salary = input("Enter New Salary(Leave Blank to skip: )")or None
            department = input("Enter New Department(Leave Blank to skip: )")or None

            update_employees(emp_id,name,age,salary,department)
        elif choice == "4":
            emp_id = input("Enter Employee ID to Remove : ")
            
            remove_employee(emp_id)
        elif choice == "5":

            filename = input("Enter Filename to Save to : ")
            save_to_file(filename)
            
        elif choice == "6":

            filename = input("Enter Filename to Load from : ")

            load_from_file(filename)
            
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


menu()