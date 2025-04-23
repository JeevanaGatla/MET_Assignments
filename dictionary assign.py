john = {"age": 30, "married": False}
print("Age using []:", john["age"])
print("Age using get():", john.get("age"))
print("All keys:", john.keys())
print("All values:", john.values())


book = {"title": "Wings of Fire", "author": "APJ Abdul Kalam", "price": 250}
del book["author"]
book.pop("price")
book.clear()
print(book)



student = {"name": "Asha", "grade": "A", "age": 14}
student["is_fee_paid"] = True
student.update({"grade": "A++"})
student["name"] = "Mr. Asha"
print("Updated student dictionary:", student)



a = {"name": "joy"}
b = {"age": 45}
combined = a.copy()  
combined.update(b)
print(combined)
