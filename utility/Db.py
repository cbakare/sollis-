
import mysql.connector
class DB():
    def __init__(self, driver):
        self.driver = driver

    def create_connectonwithDB(self,mydb):
        mydb = self.driver.mysql.connector.connect(host='shstageeusmysql01.mysql.database.azure.com',port='3306', user='', passwd='')
        print(mydb)
