import mysql.connector
from tkinter import *

window = Tk()

window.title('Shopping List')

label_text = StringVar()
label_text.set('welcome')

total_label = StringVar()
total_label.set('total: ')

label = Label(window, textvariable = label_text,
              anchor = "center")
label2 = Label(window, textvariable = total_label,
               anchor = "center")

def total_price():
    cnx = mysql.connector.connect(user = 'root', password = '1234',
                              host='localhost',
                              database='shopping_list')
    cursor = cnx.cursor()
    
    cursor.execute("SELECT SUM(cost * amount) FROM fundementals")

    results = cursor.fetchone()

    total_label.set("Total: $" + str(results[0]))

    cnx.commit()
    cursor.close()
    cnx.close()

def insert(amount, name, cost):
    global label_text
    cnx = mysql.connector.connect(user = 'root', password = '1234',
                              host='localhost',
                              database='shopping_list')
    cursor = cnx.cursor()
    
    insert_fundementals ="""INSERT INTO fundementals(amount, name, cost) VALUES(%s, %s, %s);"""
    insert_f_data = (amount, name, cost)
    cursor.execute(insert_fundementals, insert_f_data)

    label_text.set("Inserted " + name + " costing $" + cost)
    
    cnx.commit()
    total_price()
    cursor.close()
    cnx.close()


def delete(name, cost):
    cnx = mysql.connector.connect(user = 'root', password = '1234',
                              host='localhost',
                              database='shopping_list')
    cursor = cnx.cursor()

    
    delete_fundementals = "DELETE FROM fundementals WHERE name = %s;"
    delete_f_data = (name, )
    cursor.execute(delete_fundementals, delete_f_data)

    label_text.set("Deleted " + name + " costing $" + cost)
    
    cnx.commit()
    total_price()
    cursor.close()
    cnx.close()


def create_txt_file():
    cnx = mysql.connector.connect(user = 'root', password = '1234',
                              host='localhost',
                              database='shopping_list')
    cursor = cnx.cursor()

    cursor.execute("SELECT name, cost, amount FROM fundementals")


    shopping_list = cursor.fetchall()
    f = open('shopping list.txt', 'w')
    for x in shopping_list:
        f.write("|%s|%i|%i| \n\r" % shopping_list[x][0] % shopping_list[x][1] % shopping_list[x][2])
    
    f.close()


amount_field = Entry(window)

name_field = Entry(window)

cost_field = Entry(window)




insert_button = Button(window, text = 'insert',
                       command = lambda: insert(amount_field.get(), name_field.get(),
                                                cost_field.get()))

delete_button = Button(window, text = 'delete',
                       command = lambda: delete(name_field.get(), cost_field.get()))


print_button = Button(window, text = 'print shopping list',
                      command = create_txt_file)


label.grid(row = 0, column = 0,
           columnspan = 8, pady = 2)

label2.grid(row = 3, column = 0,
            columnspan = 8, pady = 2)

amount_field.grid(row = 1, column = 0,
                  columnspan = 2, padx = 5)
                       
name_field.grid(row = 1, column = 3,
                  columnspan = 2, padx = 5)
                       
cost_field.grid(row = 1, column = 5,
                  columnspan = 2, padx = 5)
                       
insert_button.grid(row = 2, column = 0,
                   columnspan = 2, padx = 5,
                   pady = 10)
delete_button.grid(row = 2, column = 3,
                   columnspan = 2, padx = 5,
                   pady = 10)
print_button.grid(row = 2, column = 6,
                  padx = 5, pady = 10)
