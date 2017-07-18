"""
Python 3.5
SQLite
"""
# TODO Create a webapp

import sqlite3

conn = sqlite3.connect('schedule.db')  # Connect to the database
c = conn.cursor()  # Create the cursor


def start():  # Asking what the user wants to do
    option = input("'Add' to database.\n'Update' the database\n'List' the database.\n'Exit'\n"
                   "What would you like to do? ")  # User input
    if option == "Add":
        data_entry()
    if option == "Update":
        update_database()
    if option == "List":
        list_database()
    if option == "Exit":
        print("Exiting and Saving")
        c.close()  # Close the cursor
        conn.close()  # Close connection to the database


# TODO Force proper inputs for the questions. ie: Date, Time, Cost
def data_entry():  # User input to add to the database
    e = input("What is the name of the event? 'MDU' 'SD' 'TD' ")  # Event name is the table for the database
    d = input("What date does the event take place or start? 'mm/dd/yy' ")
    t = input("What time does the event start? 24 hour format 'HH:MM' ")
    l = input("What is the name of the track? ")
    a = input("What is the address? ")
    df = input("What is the cost to drive? ")
    sf = input("What is the cost to spectate? ")
    o = input("Any other useful information, requirements, tech inspections? ")
    c.execute('CREATE TABLE IF NOT EXISTS DriftSchedule'+e+' (Date DATE, Time TIME, Location TEXT, Address TEXT,'
                                                           ' DriverFee INTEGER, SpectatorFee INTEGER, Other TEXT)')
    c.execute('INSERT INTO DriftSchedule'+e+' (Date, Time, Location, Address, DriverFee, SpectatorFee, Other) VALUES '
                                            '(?, ?, ?, ?, ?, ?, ?)', (d, t, l, a, df, sf, o))
    print("Saving data....")
    conn.commit()  # Commit the changes to the database
    print("Restarting")
    start()


# TODO Make the update_database work
def update_database():  # Still working on this
    c.execut('SELECT * FROM DriftSchedule')
    [print(row) for row in c.fetchall()]
    input("Press Enter to continue...")
    start()

# TODO This needs fixed because of the other tables
def list_database():  # Listing the database
    c.execute('SELECT * FROM DriftSchedule')
    for row in c.fetchall():
        print(row)
    input("Press Enter to continue...")
    start()


start()
