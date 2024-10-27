"""
สมมติว่าคุณเป็นนักพัฒนาโปรแกรม และได้รับมอบหมายให้สร้างระบบเพื่อจัดการข้อมูลของพนักงานในบริษัท โดยข้อมูลแต่ละคนจะมีดังนี้:

Input
ชื่อ - ข้อความ
อายุ - จำนวนเต็ม
เงินเดือน - จำนวนทศนิยม
ตำแหน่งงาน - ข้อความ

Output
{'Name': 'Alice', 'Age': 30, 'Salary': 50000.5, 'Position': 'Software Engineer'}

ตัวอย่าง code การเพิ่มข้อมูลใน dit
ชื่อตัวแปล["ตัวแปลที่เราต้องการเพิ่ม"] = "ค่าของตัวแปล(ตัวหนังสือหรือตัวเลขก็ได้)"
employee_1["phone"] = "123-456-7890"
 
จงเขียน code

"""
deta = {}
name = input("Name :")
deta["Name"] = name
age = int(input("Age :"))
deta["Age"] = age
salary = float(input("Salary :"))
deta["Salary"] = salary
position = input("Position :")
deta["Position"] = position

print(deta)