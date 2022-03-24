import mysql.connector as mysql
con = mysql.connect(host="localhost", user="root", password="")
cursor = con.cursor()
cursor.execute("use studdb")
print("Welcome to student management portal...")


def insert():
    print("Provide your details")
    name = input("Enter your name: ")
    Branch = input("Enter your branch: ")
    class_year = input("Enter your academic year: ")
    fees = eval(input("Enter your fees: "))
    status = input("What is your status: ")
    contact = input("Enter your contact number: ")
    email = input("Enter your email: ")

    q = "insert into stud(Name, Branch, Class_year, Fees, Status, Contact, Email) values('" + \
        name+"', '"+Branch+"','"+class_year+"','" + \
        str(fees)+"','"+status+"', '"+contact+"', '"+email+"' )"
    cursor.execute(q)
    con.commit()
    print("Details are saved..")


def showAll():
    q = "select * from stud"
    cursor.execute(q)
    records = cursor.fetchall()
    for record in records:
        print(record)


def selectOne():
    name = input("Provide your name to get records: ")
    q = "select * from stud where name = '"+name+"'"
    cursor.execute(q)
    record = cursor.fetchone()
    print(record)


def change():
    id = input("Provide your Id: ")
    choice = input(
        "Select what you want to update: \nname, Branch, class_year, fees, status, contact, email or All:  ").lower()
    if (choice == "all"):
        name = input("Provide new name: ")
        branch = input("Enter new branch: ")
        class_year = input("Provide new Academic year: ")
        fees = input("Provide new fees: ")
        status = input("Enter new status: ")
        contact = input("Enter new contact number: ")
        email = input("Provide new email: ")
        q = "update stud set Name = '"+name+"', Branch = '"+branch+"', Class_year = '"+class_year+"', Fees = '" + \
            fees+"', Status = '"+status+"', Contact = '"+contact + \
            "', Email = '"+email+"' where id = '"+id+"'"
        cursor.execute(q)
        con.commit()
        print("Details updated...")
    elif (choice == "name"):
        name = input("Provide new name: ")
        q = "update stud set Name = '"+name+"' where id = '"+id+"'"
        cursor.execute(q)
        con.commit()
        print("Details updated...")
    elif (choice == "branch"):
        branch = input("Enter new branch: ")
        q = "update stud set Branch = '"+branch+"' where id = '"+id+"'"
        cursor.execute(q)
        con.commit()
        print("Details updated...")
    elif (choice == "Class_year"):
        class_year = input("Provide new Academic year: ")
        q = "update stud set Class_year = '"+class_year+"' where id = '"+id+"'"
        cursor.execute(q)
        con.commit()
        print("Details updated...")
    elif (choice == "Fees"):
        fees = input("Provide new fees: ")
        q = "update stud set Fees = '"+fees+"' where id = '"+id+"'"
        cursor.execute(q)
        con.commit()
        print("Details updated...")
    elif (choice == "Status"):
        status = input("Enter new status: ")
        q = "update stud set Status = '"+status+"' where id = '"+id+"'"
        cursor.execute(q)
        con.commit()
        print("Details updated...")
    elif (choice == "Contact"):
        contact = input("Enter new contact number: ")
        q = "update stud set Status = '"+contact+"' where id = '"+id+"'"
        cursor.execute(q)
        con.commit()
        print("Details updated...")
    elif (choice == "email"):
        email = input("Provide new email: ")
        q = "update stud set Email = '"+email+"' where id = '"+id+"'"
        cursor.execute(q)
        con.commit()
        print("Details updated...")

    else:
        print("Provide valid details!...")


def delete():
    name = input("Provide your name to delete your data: ")
    q = "delete from stud where Name = '"+name+"'"
    cursor.execute(q)
    con.commit()
    print("Records deleted...")


choice = int(input("What you want to do..\nEnter:-\n 1 to insert data\n 2 to get all the data\n 3 to update the data \
    \n 4 to select the specific data\n 5 to delete your data\n Select any one: "))
print()
if (choice == 1):
    insert()
elif (choice == 2):
    showAll()
elif (choice == 3):
    change()
elif (choice == 4):
    selectOne()
elif (choice == 5):
    delete()
else:
    print("Provid valid choice...")
