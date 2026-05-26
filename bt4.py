# Input:
# - Số lượng nhân sự mới: kiểu số nguyên (int)

# Yêu cầu hợp lệ:
# - Phải là số nguyên > 0

# Output:
# - Nếu <= 0: in thông báo lỗi và yêu cầu nhập lại
# - Nếu > 0: in thông báo thành công và kết thúc chương trình

# - Dùng vòng lặp vô hạn
# - Nếu nhập sai → tiếp tục lặp
# - Nếu đúng → break để thoát

# - Khởi tạo biến quantity = 0
# - while quantity <= 0:
#     bắt nhập lại
# - Khi > 0 → tự thoát vòng lặp

# Chọn: while điều kiện

# Lý do:
# - Dễ đọc, dễ hiểu với người mới
# - Logic rõ ràng: "chừng nào còn sai thì còn lặp"
# - Phù hợp với bài toán validation input

print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")
# KHỞI TẠO GIÁ TRỊ BAN ĐẦU (KHÔNG HỢP LỆ)
employee_count = 0
# VÒNG LẶP KIỂM TRA DỮ LIỆU
# Chỉ dừng khi employee_count > 0
while employee_count <= 0:
    # Nhập dữ liệu từ người dùng
    employee_count = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    # KIỂM TRA ĐIỀU KIỆN
    if employee_count <= 0:
        print("[Lỗi] Số lượng không hợp lệ. Vui lòng nhập một con số lớn hơn 0.")
        # Sau khi in lỗi, vòng lặp sẽ chạy lại do điều kiện while
    else:
        # DỮ LIỆU HỢP LỆ
        print("[Thành công] Đã ghi nhận yêu cầu cấp phát tài sản cho", employee_count, "nhân sự mới!")

print("--- CHƯƠNG TRÌNH KẾT THÚC ---")



# - Sử dụng vòng lặp while để kiểm tra dữ liệu đầu vào
# - Điều kiện lặp: employee_count <= 0
# - Nếu nhập sai → in lỗi và lặp lại
# - Nếu nhập đúng (>0) → thoát vòng lặp
# - Đảm bảo không cho phép nhập số âm hoặc số 0