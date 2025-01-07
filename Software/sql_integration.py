import mysql.connector 

try: 
    conn = mysql.connector.connect ( 
        host="localhost",
        user="root",
        password="",
        database="studentData"
    )
except:
    print("Conn failed")
else:
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM Student")
    myresult = mycursor.fetchall()

    for index in myresult:
        print(index)

    id = str(input("ID: "))
    forename = str(input("forename: "))
    surname = str(input("surname: "))

    print()

    insertStudent = "INSERT INTO Student () VALUES (%s, %s, %s)"
    data = (id, forename, surname)
    mycursor.execute(insertStudent, data)
    conn.commit()

    findID = "SELECT * FROM Student"

    idData = str(input("Please enter id: "))
    mycursor.execute(findID, idData)
    rows = mycursor.fetchall()

    print("rows", rows)