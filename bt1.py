print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

# LỖI LOGIC BAN ĐẦU:
# Thực tập sinh đã đặt total_budget = 0 bên trong vòng lặp
# → mỗi lần lặp biến này bị reset lại từ đầu
# → dẫn đến KHÔNG cộng dồn được, chỉ giữ giá trị cuối

# SỬA: phải khởi tạo biến tích lũy ở ngoài vòng lặp
total_budget = 0

# Vòng lặp nhập lương cho 3 nhân viên
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    # Nhập mức lương từ bàn phím
    salary = int(input("Nhập mức lương (VND): "))
    # Cộng dồn vào tổng
    # total_budget = total_budget + salary
    # viết gọn:
    total_budget += salary
    # Giải thích:
    # Sau mỗi vòng lặp:
    # total_budget sẽ giữ lại giá trị cũ + lương mới
    # → đây gọi là biến tích lũy

# Sau khi vòng lặp kết thúc → in kết quả
print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VND")

# TÓM TẮT

# Sai: đặt biến tích lũy trong loop
# → bị reset mỗi lần lặp

# Đúng: đặt biến tích lũy ngoài loop
# → cộng dồn đúng kết quả

# Đây là lỗi rất phổ biến khi học vòng lặp (for/while)