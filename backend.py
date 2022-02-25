import mysql.connector as mysql

class backend():
    def select(self, syntax):
        con = mysql.connect(host='localhost', user='root', password='', database='cashier_app')
        cursor = con.cursor()

        cursor.execute(syntax)
        rows = cursor.fetchall()

        return rows
    
    def action(self, syntax):
        con = mysql.connect(host='localhost', user='root', password='', database='cashier_app')
        cursor = con.cursor()

        cursor.execute(syntax)
        cursor.execute("commit")

        return True