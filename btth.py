# Dùng vòng lặp 'while True' ở ngoài cùng để quản lý việc "Tiếp tục hoặc Kết thúc" chương trình (Yêu cầu 5)
while True:
    # 1. Nhập số lượng nhân viên (Yêu cầu 1)
    # Chuyển đổi dữ liệu nhập vào thành kiểu số nguyên int()
    so_luong = int(input("Nhập số lượng nhân viên: "))
    print()  # In dòng trống cho thoáng và giống kết quả mẫu

    # Vòng lặp 'for' kết hợp 'range()' để duyệt qua từng nhân viên dựa trên số lượng đã nhập
    for i in range(so_luong):
        # Hiển thị số thứ tự nhân viên (i bắt đầu từ 0 nên cần + 1)
        print(f"Nhân viên {i + 1}")
        
        # 2. Nhập thông tin nhân viên (Yêu cầu 2)
        ten_nv = input("Tên nhân viên: ")
        # Số ngày đi làm cần chuyển sang kiểu số nguyên để so sánh ở bước sau
        so_ngay = int(input("Số ngày đi làm: "))
        
        # 3. Hiển thị thông tin vừa nhập (Yêu cầu 3)
        print("Thông tin nhân viên:")
        print(f"Tên: {ten_nv}")
        print(f"Số ngày đi làm: {so_ngay}")
        
        # 4. Đánh giá chuyên cần (Yêu cầu 4)
        # Sử dụng cấu trúc rẽ nhánh if-else để kiểm tra điều kiện
        if so_ngay < 20:
            print("Cần cải thiện chuyên cần")
        else:
            print("Nhân viên chuyên cần tốt")
        
        print()  # In dòng trống phân tách giữa các nhân viên hoặc trước khi hỏi tiếp tục

    # 5. Tiếp tục hoặc kết thúc chương trình (Yêu cầu 5)
    # Hỏi ý kiến người dùng sau khi đã xử lý xong danh sách nhân viên
    lua_chon = input("Tiếp tục chương trình? (y/n): ")
    
    # Nếu người dùng nhập 'n' hoặc 'N', ta dùng lệnh 'break' để thoát khỏi vòng lặp while True
    if lua_chon.lower() == 'n':
        print("Chương trình kết thúc")
        break
    
    # Nếu nhập 'y', vòng lặp while sẽ tự động quay lại từ đầu (Yêu cầu 1)
    print()  # Dòng trống tạo khoảng cách cho lần chạy tiếp theo