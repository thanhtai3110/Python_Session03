print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")
# Vòng lặp chạy 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")
    # Nhập số ngày công
    working_days = int(input("Nhập số ngày công trong tháng: "))

    # PHÂN TÍCH LỖI LOGIC
    # if working_days == 0:
    #     print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
    
    # Lỗi ở đây:
    # - Khi working_days == 0, chương trình chỉ in cảnh báo
    # - Sau đó KHÔNG dừng lại
    # - Vẫn tiếp tục chạy xuống dưới
    
    # Kết quả:
    # - vẫn tính bonus_amount = 0 * 200000 = 0
    # - vẫn gửi email "chúc mừng nhận được 0 VND"
    #
    # Đây là lỗi thiếu điều hướng trong vòng lặp
    # (không dùng continue hoặc không có else)

    # SỬA LỖI
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        # Bỏ qua phần còn lại của vòng lặp
        # chuyển sang nhân viên tiếp theo
        continue
    # CHỈ THỰC HIỆN KHI working_days > 0
    bonus_amount = working_days * 200000

    print("Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VND tiền thưởng")
    print()

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên")

# TRACE CODE (TRƯỜNG HỢP working_days = 0)
# Bước 1: nhập working_days = 0
# Bước 2: vào if -> in cảnh báo
# Bước 3: gặp continue -> quay lại vòng lặp
# Bước 4: KHÔNG chạy phần tính thưởng và gửi email
#
# => Đúng yêu cầu nghiệp vụ
# Kêt luận
# Lỗi: thiếu điều hướng trong vòng lặp
# Hậu quả: vẫn thực thi code phía dưới dù không thỏa điều kiện
# Cách sửa: dùng continue để bỏ qua trường hợp không hợp lệ