# Test: login validation for AttendX
def login(user, pwd):
    return user == "student1" and pwd == "pass123"

assert login("student1", "pass123") == True
assert login("student1", "wrong") == False
print("Login tests passed")