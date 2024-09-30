import mysql.connector as mydb
from _mysql_connector import *
from Create_Acc import frame
import Create_Acc as Create_Acc


class mysql_brgy_proffiling():
    connect = mydb.connect(
        host='localhost',
        user='root',
        database='db_brgyprofilling'
    )
    cursor = connect.cursor()
    cursor.execute(''' Select * from tbl_adminlogin;''')

    # Fetch the results
    results = cursor.fetchall()

    # Print the results (optional)
    for row in results:
        print(row)

    cursor.close()
    connect.close()