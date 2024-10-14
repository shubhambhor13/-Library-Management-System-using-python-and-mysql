# Library Management System
import mysql.connector # type: ignore
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "library"
 )
my = db.cursor()

print("Welcome to  Aadarsh Libarary")
nam = input("Enter your name:")

print("1.User\n2.Management")
print("Enter one option:")
choice = input()

if choice == "User" or choice == '1':
    print("you are User")
elif choice == "Management" or choice == '2':
    print("you are a Manager")
else:
    print("chosse the wrong option")
    exit()
print("Welcome!!",nam)

if choice == 'Management' or choice == '2':
    print("Book tracking \n1.availability\n2.Borrowing\n3.Returning\nMember Management\n4.Registration\n5.Profile Updates\n6.Search functinality\n7.Add Books\n8.Update reserved book status")
    print("Enter select a one option:")
    choose = input()

elif choice == 'User' or choice == '1':
    print("1.Registration\n2.Login\n3.Book Search and reservation\n4.Booking a book\n\nMember profile management\n5.Personal Details\n6.Display the books borrowed\n7.Return the book to the libarary")
    print("Enter select a one option:")
    choose = input()
    
else:
    print("we are selected wrong option")
    exit()

if choice == 'Management' or choice == '2':
    if choose == '7':
     print("Add books")
     while True:
        d = input("Enetr your Book_Name:")
        e = input("Enetr your Book_Id:")
        f = input("Enetr your Book_Writer:")
        sql = "Insert into book(Book_Name,Book_Id,Book_Writer) Values(%s,%s,%s)"
        val = (d,e,f)
        my.execute(sql,val)
        db.commit()
        print("Adding Book Successfully")

    elif choose == '1':
        print("availability")

        sql = "Select*From book"
        my.execute(sql)
        result = my.fetchall()
        for r in result:
            print(r)
        print("This books are available")
    
    elif choose == '2':
        print("Borrowing")
        my.execute("Select*From borrowing_books where Status = 'borrowed'")
        res = my.fetchall()
        for s in res:
            print(s)
        print("Borrowing Books")
    
    elif choose == '3':
        print("Returning")
        sql = "Select * from borrowing_books where Status = 'borrowed'"
        my.execute(sql)
        res = my.fetchall()
        
        if res:
         print("Currently borrowed books:")
        for s in res:
            print(s)
        
        book_id = input("Enter the Book_Id of the book you want to return: ")
        sql = "Select * from borrowing_books where Book_Id = %s and Status = 'borrowed'"
        val = (book_id,)
        my.execute(sql, val)
        res = my.fetchall()
        
        if res:
            print("Book details:")
            for d in res:
                print(d)

            import datetime
            return_date = datetime.datetime.now()
            for d in res:
                book_name = d[1]
                book_id = d[2]
                book_writer = d[3]

                sql = "Insert Into returned_books(Book_Name, Book_Id, Book_Writer, Status, Date_and_Time) Values (%s, %s, %s, %s, %s)"
                val = (book_name, book_id, book_writer, 'Returned', return_date)
                my.execute(sql, val)
                db.commit()

                print(f"Book '{book_name}' returned successfully on {return_date.strftime('%Y-%m-%d %H:%M:%S')}")

            sql = "Update borrowing_books Set Status = 'returned' Where Book_Id = %s"
            val = (book_id,)
            my.execute(sql, val)
            db.commit()

            print(f"Book '{book_name}' status updated to 'returned'.")
        else:
            print("This book was either not borrowed or the Book_Id is incorrect.")
   
   
    elif choose == '4':
        print("Registration")
        a = input("Enter your Name:")
        b = input("Enter your Manger_id:")
        c = input("Enter your Gender:")
        d = input("Enter your Address:")
        if a and b and c and d :
            sql = "Insert Into management(Name,Manger_id,Gender,Address) Value(%s,%s,%s,%s)"
            val = (a,b,c,d)
            my.execute(sql,val)
            db.commit()
            print("Registration successfully") 
        else:
            print("Registration Unsuccessfully !! Try Again")
    
    elif choose == '5':
        print("Profile Updates")
        sql = "Select*From management"
        my.execute(sql)
        res = my.fetchall()
        for s in res:
            print(s)
        print("Manager Data")

        d = input("Enter a update data:")
        column = input("Enter a column:")
        e = input("Enter Id, where the update data:")
        sql = f"Update management Set {column} = %s Where Id = %s"
        val = (d,e)
        my.execute(sql,val)
        db.commit()
        print("Updating Successfully")
    
    elif choose == '6':
        print("Search functinality")

        a = (input("Enter a searching Book_Name:"))

        sql = "Select*From book Where Book_Name = %s"
        val = (a,)
        my.execute(sql,val)
        result = my.fetchall()
        if result:
         for s in result:
            print(s)
         print("Book is Found")
        else:
            print("No matching books found")
            exit()

    elif choose =='8':
        print("Update Reserved Book Status")
        sql = "select*from reservation where Status = 'Reserved'"
        my.execute(sql)
        res = my.fetchall()
        for t in res:
            print(t)
        f = input("Enter id, where you update Status:")   
        sql = "Update reservation set Status ='borrowed' Where Status = 'Reserved' and id = %s"
        val = (f,)
        my.execute(sql,val)
        db.commit()
        print("Updating successfully")
    
elif choice == 'User' or choice == '1':
        
    if choose =='1':
        print("Registration!!")

        a  = input("Enter your Name:")
        b  = input("Enter your Gender:")
        c = input("Enter your Address:")
        if a and b and c:
            sql = "Insert Into registration_user(Name,Gender,Address) Value(%s,%s,%s)"
            val = (a,b,c)
            my.execute(sql,val)
            db.commit()
            print("Adding Registartion data")
            print("Registraton Succesfully")
        else:
            print("Registration Unsuccessfully !! Try Again")
            exit()

        a = input("Enter your User_Name:" )
        b = input("Enter Your User_id:")
        if a and b:
            sql = "Insert Into login_data_user(User_Name,User_id) Value(%s,%s)"
            val = (a,b)
            my.execute(sql,val)
            db.commit()
            print("Added login data successfully")
            print("Login successfully")
        else:
            print("Login Unsuccessfully")
            exit()
        
    
    elif choose == '2': 
        print("Please Login!!")
        a = input("Enter your User_Name:" )
        b = input("Enter Your User_id:")
        if a and b:
            sql = "Insert Into login_data_user(User_Name,User_id) Value(%s,%s)"
            val = (a,b)
            my.execute(sql,val)
            db.commit()
            print("Added login data successfully")
            print("Login successfully")
        else:
            print("Login Unsuccessfully")
            exit()
    
    elif choose =='3':
        print("Book Search and reservation")

        a = (input("Enter a searching Book_Name:"))

        sql = "Select*From book Where Book_Name = %s"
        val = (a,)
        my.execute(sql,val)
        result = my.fetchall()
        if result:
         for s in result:
            print(s)
         print("Book is Found")
        else:
            print("No matching books found")
            
        s= input("Do you want to reserve a book? (yes/no)")
        if s == 'yes':
            sql  = "Select*From book"
            my.execute(sql)
            res = my.fetchall()
            for d in res:
                print(d)
            print("These books are avaliable in libarary")
        elif s == 'no':
            print("Exit")
            exit()
        else:
            print("wrong input enter")
            exit()
    
        ava = input("Enter a book_id you are reserved:")

        sql = "Select*From book Where Book_id = %s"
        val = (ava,)
        my.execute(sql,val)
        res = my.fetchall()
        if res:
         for e in res:
            print(e)
         print("Reserved book Successfully")
        else:
            print("Enter wrong book id")
            exit()


        for e in res:
            id = e[0]
            Book_Name = e[1]
            Book_Id = e[2]
            Book_Writer = e[3]

            sql = "Insert Into reservation(Book_Name,Book_Id,Book_Writer,Status) Value(%s,%s,%s,%s)"
            val  = (Book_Name,Book_Id,Book_Writer,"Reserved")
            my.execute(sql,val)
            db.commit()
            print("Reserved book successfully added")

    elif choose =='4':
        print("Booking a book")
        sql = "select*from book"
        my.execute(sql)
        res = my.fetchall()
        for t in res:
            print(t)
        print("These Books are Available")

        b = input("Enter the book_id of the book you want to borrow: ")

        sql = "Select*From book Where Book_Id = %s"
        val = (b,)
        my.execute(sql,val)
        res = my.fetchall()
        for g in res:
            print(g)
        
        for g in res:
            import datetime
            RD = datetime.datetime.now()
            id =g[0]
            Book_Name = g[1]
            Book_Id = g[2]
            Book_Writer = g[3]
            
            sql = "Insert Into borrowing_books(Book_Name,Book_Id,Book_Writer,Status,Date_and_Time) Values(%s,%s,%s,%s,%s)"
            val = (Book_Name,Book_Id,Book_Writer,"borrowed",RD)
            my.execute(sql,val)
            db.commit()
            print("Successfully borrowing book")

    elif choose == '5':    
        print("Added personal detalis")
        while True:
            a = input("Enter Your Name:")
            v = input("Enter Your Address:")
            f = input("Enter your Id_proof:")
            s = input("Enter your Email_ID:")   

            sql = "Insert Into user(Name,Address,Id_proof,Email_ID) Values(%s,%s,%s,%s)"
            val = (a,v,f,s)
            my.execute(sql,val)
            db.commit()
            print("Adding user Personal details successfully")

    elif choose == '6':
        print("Display the books borrowed") 

        sql = "Select*From borrowing_books where Status = 'borrowed'"
        my.execute(sql)
        res = my.fetchall()
        for s in res:
            print(s)
        print("Borrowed books successfully fetching")

    elif choose =='7':
        print("Return the book to the libarary")

        sql = "Select*from borrowing_books where Status = 'borrowed'"
        my.execute(sql)
        res = my.fetchall()
        if res:
            print("borrowed books")
            for s in res:
             print(s)
        
        book = input("Enter the Book_Id of the book you want to return:")

        sql = "select*from borrowing_books where Book_Id = %s and Status = 'borrowed'"
        val = (book,)
        my.execute(sql,val)
        res = my.fetchall()
        for d in res:
            print(d)
        
        if res:
            import datetime
            RD = datetime.datetime.now()
            id = d[0]
            Book_Name = d[1]
            Book_Id = d[2]
            Book_Writer = d[3]
        
            sql = "Insert Into returned_books(Book_Name,Book_Id,Book_Writer,Status,Date_and_Time) Value(%s,%s,%s,%s,%s)"
            val = (Book_Name,Book_Id,Book_Writer,'Returned',RD)
            my.execute(sql,val)
            db.commit()
            print("Book returned successfully on",RD)
        else:
            print("This book was either not borrowed by you or the Book_Id is incorrect.")

        sql = "Update borrowing_books Set Status = 'returned' Where Book_Id = %s "
        val = (book,)
        my.execute(sql, val)
        db.commit()
        print("successfully returned book")

    
