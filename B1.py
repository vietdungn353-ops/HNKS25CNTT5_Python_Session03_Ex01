# Lỗi sai: đặt biến tính tổng lương vào bên trong vòng
#   lặp khiến mỗi khi bắt đầu chạy 1 vòng thì biến tổng lại 
#   reset về giá trị ban đầu. Khi chạy xong vào lặp thì giá 
#   trị biến tổng lương sẽ là giá trị của lương người cuối 
#   cùng chạy trong vòng lặp
# Sửa: Cho biến tính tổng lương ra bên ngoài vòng lặp

print (" --- PHẦN MEM TINH TONG QUY LƯONG -- ")

# Khoi tạo chiếc hộp dựng tổng tiền
total_budget = 0


# Vòng Lặp chạy 3 Lần dể nhập Lương cho 3 nhân viên
for employee_number in range(1, 4):

    print ("Đang xử lý nhân viên số", employee_number)
    # Nhập mức Lương
    salary = int(input(" Nhập mức Lương (VNĐ): "))

    # Thực hiện thao tác cộng dồn tiền vào chiếc hộp
    total_budget = total_budget + salary

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print("= KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUAN BỊ LÀ:", total_budget, "VNĐ")