"""
สมมติว่าคุณเป็นผู้ดูแลข้อมูลในคลังสินค้า และมีสินค้าหลายรายการ โดยแต่ละสินค้าจะมีข้อมูลดังนี้:

Input
สร้าตัวแปลเก็บข้อมูลสิ้นค้าไว้ 3 อย่าง และแต่ละอย่างต้องมีข้อมูลตามนี้

ชื่อสินค้า - ข้อความ
ราคา - จำนวนทศนิยม
จำนวนสินค้าในสต็อก - จำนวนเต็ม

โดยใช้คำสั่ง input()ในการป้อนข้อมูล

Output
{'Name': 'Alice', 'Age': 30, 'Salary': 50000.5, 'Position': 'Software Engineer'}

ตัวอย่าง code การเพิ่มข้อมูลใน dit
ชื่อตัวแปล["ตัวแปลที่เราต้องการเพิ่ม"] = "ค่าของตัวแปล(ตัวหนังสือหรือตัวเลขก็ได้)"
employee_1["phone"] = "123-456-7890"
 
จงเขียน code

"""
item1 = {}
item2 = {}
item3 = {}

name = input("Name :")
item1["Name"] = name

price = int(input("Price :"))
item1["Age"] = price

quantity = float(input("Quantity :"))
item1["Salary"] = quantity

print(item1)

name = input("Name :")
item2["Name"] = name

price = int(input("Price :"))
item2["Age"] = price

quantity = float(input("Quantity :"))
item2["Salary"] = quantity

print(item2)

name = input("Name :")
item3["Name"] = name

price = int(input("Price :"))
item3["Age"] = price

quantity = float(input("Quantity :"))
item3["Salary"] = quantity

print(item3)