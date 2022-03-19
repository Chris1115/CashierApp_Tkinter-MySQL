from turtle import back
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

        before = self.getRowCounts()
        cursor.execute(syntax)
        con.commit()
        after = self.getRowCounts()

        if before < after:
            return True
        elif before == after:
            return True
        elif before > after:
            return True
        else:
            return False

    def getRowCounts(self):
        con = mysql.connect(host='localhost', user='root', password='', database='cashier_app')
        cursor = con.cursor()

        cursor.execute("SELECT COUNT(id) FROM product;")
        return cursor.fetchall()