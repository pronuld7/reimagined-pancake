import time
import sqlite3
# get the start time
st = time.time()

# main program (input your code here)
print("Hello")
time.sleep(1)
print("World!")

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

# ask for importing
sql_import = input("Import execution time into database?\n")

# if user answers yes, import into database
if sql_import == "Yes" or sql_import == "yes":
    print("Creating and connecting to database...")
    connection = sqlite3.connect("elapsedtime.sl3", 5)
    cur = connection.cursor()
    print("Creating table...")
    cur.execute("CREATE TABLE first_table (elapsedtime TEXT);")
    print("Inserting elapsed time into table...")
    cur.execute(f"INSERT INTO first_table (elapsedtime) VALUES('Time:');")
    cur.execute(f"INSERT INTO first_table (elapsedtime) VALUES('{elapsed_time} seconds');")
    connection.commit()
    print("Closing connection...")
    connection.close()
    print("Done!")
elif sql_import == "No" or sql_import == "no":
    print("Ok! Goodbye!")