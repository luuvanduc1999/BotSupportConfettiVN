ORC bằng TesseractORC, search bằng Selenium

Đối với câu hỏi "CHƯA", "KHÔNG" sẽ search số kết quả tìm được của từng question+"option[]" . Kết quả nhỏ nhất là đáp án
Ngược lại:
Search câu hỏi với google và wiki mỗi thứ 50 kết quả, đếm số lần xuất hiện của cả mỗi option[] trong trang đó. Không lấy data và chạy count bằng python vì nó rất lâu, nên sẽ đếm bằng javascript
Kết quả chính là phần nguyên. Để tránh cùng kết quả, đếm thêm số lần xuất hiện của từng từ trong option[]. Đây là phần thập phân

Lưu ý:
1. Để setup số lượng kết quả là 50, sử dụng cookies import từ file vào mỗi lần sử dụng. cái này search pickle
