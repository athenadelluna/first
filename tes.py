import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if db.is_connected():
    print("Bershasil terhubung ke database")

a= input("ïnput coy> ")
b= " mantap kali bos"
print(a+b)
