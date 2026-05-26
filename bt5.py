# Tên biến          | Câu hỏi input                                  | Kiểu dữ liệu | Điều kiện validation
# ------------------|-----------------------------------------------|--------------|------------------------
# employee_id       | Enter Employee ID (VD: DEV01)                 | str          | không rỗng
# employee_name     | Enter Full Name                               | str          | không rỗng
# current_salary    | Enter current Salary in VND (> 0)             | float        | > 0
# performance_score | Enter Performance Score (1.0 đến 5.0)         | float        | 1.0 <= x <= 5.0
# experience_years  | Enter Years of Experience (>= 0)              | int          | >= 0   

# in tiêu đề hệ thống

# while True:
#     nhập employee_id (kiểm tra rỗng)
#     nhập employee_name (kiểm tra rỗng)

#     while salary <= 0:
#         bắt nhập lại

#     while KPI không trong [1.0, 5.0]:
#         bắt nhập lại

#     while experience < 0:
#         bắt nhập lại

#     in hồ sơ nhân sự
#     in log hệ thống

#     hỏi tiếp tục (y/n)
#     nếu n → break

# in thông báo kết thúc

print("===== KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI =====")
# VÒNG LẶP NGOÀI: NHẬP NHIỀU NHÂN VIÊN
while True:

    print("\n[Nhập thông tin nhân viên]")
    # NHẬP DỮ LIỆU CHUỖI
    while True:
        employee_id = input("1. Enter Employee ID (VD: DEV01): ")
        if employee_id.strip() == "":
            print("[Lỗi] Mã nhân viên không được để trống. Vui lòng nhập lại.")
        else:
            break
    while True:
        employee_name = input("2. Enter Full Name: ")
        if employee_name.strip() == "":
            print("[Lỗi] Tên nhân viên không được để trống. Vui lòng nhập lại.")
        else:
            break
    # NHẬP LƯƠNG 
    while True:
        current_salary = float(input("3. Enter current Salary in VND (Number > 0): "))
        if current_salary <= 0:
            print("[Lỗi] Lương không thể là số âm hoặc bằng 0. Vui lòng nhập lại.")
        else:
            break
    # NHẬP KPI
    while True:
        performance_score = float(input("4. Enter Performance Score (1.0 to 5.0): "))
        if performance_score < 1.0 or performance_score > 5.0:
            print("[Lỗi] Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0.")
        else:
            break
    # NHẬP SỐ NĂM KINH NGHIỆM
    while True:
        experience_years = int(input("5. Enter Years of Experience (Integer >= 0): "))
        if experience_years < 0:
            print("[Lỗi] Số năm kinh nghiệm không hợp lệ.")
        else:
            break
    # IN HỒ SƠ NHÂN SỰ
    print("\n========== E-PROFILE CẬP NHẬT ==========")
    print("ID       :", employee_id)
    print("Name     :", employee_name)
    print("Salary   :", current_salary, "VND")
    print("KPI Score:", performance_score, "/ 5.0")
    print("Experience:", experience_years, "years")
    # LOG HỆ THỐNG
    print("\n========== IT SYSTEM LOG ==========")
    print("employee_id       |", type(employee_id))
    print("employee_name     |", type(employee_name))
    print("current_salary    |", type(current_salary))
    print("performance_score |", type(performance_score))
    print("experience_years  |", type(experience_years))

    # HỎI TIẾP TỤC
    choice = input("\nDo you want to enter another employee? (y/n): ")

    if choice.lower() == "n":
        break
# KẾT THÚC CHƯƠNG TRÌNH
print("\nĐang tắt Kiosk... Tạm biệt!")


# - Dùng while True cho vòng lặp ngoài (nhập nhiều nhân viên)
# - Dùng while riêng cho từng input để validate
# - Kiểm tra:
#   + string: không rỗng (strip)
#   + salary > 0
#   + KPI từ 1.0 đến 5.0
#   + experience >= 0
# - Sau khi hợp lệ: in hồ sơ + log hệ thống
# - Cho phép tiếp tục hoặc dừng bằng y/n