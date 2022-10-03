import pymysql

def connection():
    s='127.0.0.1'
    d='employer_information'
    u='root'
    p='root'
    conn =pymysql.Connect(host=s, user=u, database=d, password=p )
    return conn

emp=connection()
print(emp)
cur=emp.cursor()
cur.execute("SELECT *FROM info_tbl")
employee_details=cur.fetchall()
for i in employee_details:
    print(i)