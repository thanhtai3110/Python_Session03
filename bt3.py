# Input:
# - employee_id: string (không được rỗng, không chỉ chứa khoảng trắng)
# - full_name: string (không được rỗng, không chỉ chứa khoảng trắng)
# - department: string (có thể nhập bình thường)

# Output:
# - Nếu hợp lệ:
#   In "Phiếu Hồ sơ Nhân sự"
# - Nếu không hợp lệ:
#   In cảnh báo và bỏ qua hồ sơ đó

# - Dùng vòng lặp for chạy đúng 3 lần
# - Mỗi lần:
#     + Nhập dữ liệu
#     + Dùng strip() để loại bỏ khoảng trắng
#     + Kiểm tra:
#         nếu employee_id hoặc full_name rỗng → báo lỗi
#         dùng continue để bỏ qua
#     + Nếu hợp lệ → in hồ sơ

# lặp từ 1 đến 3:
#     nhập employee_id
#     nhập full_name
#     nhập department

#     nếu employee_id rỗng hoặc full_name rỗng:
#         in cảnh báo
#         bỏ qua vòng lặp (continue)

#     in phiếu hồ sơ

print("=== HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN SỰ ===")

# Vòng lặp xử lý 3 nhân viên
for i in range(1, 4):

    print("\n--- Nhập thông tin nhân viên", i, "---")

    # Nhập dữ liệu
    employee_id = input("Nhập mã nhân viên: ")
    full_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")
    # XỬ LÝ EDGE CASE
    # strip() dùng để loại bỏ khoảng trắng đầu/cuối
    # nếu sau khi strip mà chuỗi rỗng → dữ liệu không hợp lệ

    if employee_id.strip() == "" or full_name.strip() == "":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        
        # bỏ qua nhân viên này, chuyển sang người tiếp theo
        continue
    # DỮ LIỆU HỢP LỆ → IN HỒ SƠ
    print("\n----- PHIẾU HỒ SƠ NHÂN SỰ -----")
    print("Mã nhân viên :", employee_id)
    print("Họ và tên    :", full_name)
    print("Phòng ban    :", department)
    print("--------------------------------")

print("\nĐã hoàn tất nhập hồ sơ cho 3 nhân viên")


#  Sử dụng vòng lặp for để nhập 3 nhân viên
#  Dùng strip() để xử lý dữ liệu rác (khoảng trắng)
#  Dùng if để kiểm tra dữ liệu hợp lệ
#  Dùng continue để bỏ qua dữ liệu sai
#  Chỉ in hồ sơ khi dữ liệu hợp lệ