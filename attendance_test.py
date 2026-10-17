# Test: marking attendance
def mark_attendance(student_id, status):
    return status in ["Present", "Absent"]

assert mark_attendance(101, "Present") == True
assert mark_attendance(101, "Invalid") == False
print("Attendance tests passed")