# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Phân loại của một người (không phải hai bộ độc lập)

Người thực hiện: thành viên duy nhất của nhóm. Đối chiếu cùng định nghĩa trong hướng dẫn; bảng dưới là phân loại tham khảo theo từng ca, **không phải hai lần gắn nhãn độc lập**. Vì không có người gắn nhãn thứ hai, đồng thuận độc lập chưa đo được; không nhận điểm tiêu chí này như thể đã đạt.

| Ca | Phân loại của người làm bài | Nhãn người thứ hai | So sánh độc lập | Phân loại dùng trong bảng |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Không có người thứ hai | Chưa thể so sánh | Do người dùng |
| 2 | Hệ thống | Không có người thứ hai | Chưa thể so sánh | Hệ thống |
| 3 | Ngữ cảnh | Không có người thứ hai | Chưa thể so sánh | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Không có người thứ hai | Chưa thể so sánh | Giới hạn hệ thống |
| 5 | Ngầm | Không có người thứ hai | Chưa thể so sánh | Ngầm |
| 6 | Do người dùng | Không có người thứ hai | Chưa thể so sánh | Do người dùng |
| 7 | Hệ thống | Không có người thứ hai | Chưa thể so sánh | Hệ thống |
| 8 | Hệ thống | Không có người thứ hai | Chưa thể so sánh | Hệ thống |
| 9 | Do người dùng | Không có người thứ hai | Chưa thể so sánh | Do người dùng |
| 10 | Ngữ cảnh | Không có người thứ hai | Chưa thể so sánh | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Không có người thứ hai | Chưa thể so sánh | Giới hạn hệ thống |
| 12 | Ngầm | Không có người thứ hai | Chưa thể so sánh | Ngầm |
| 13 | Giới hạn hệ thống | Không có người thứ hai | Chưa thể so sánh | Giới hạn hệ thống |
| 14 | Do người dùng | Không có người thứ hai | Chưa thể so sánh | Do người dùng |
| 15 | Hệ thống | Không có người thứ hai | Chưa thể so sánh | Hệ thống |
| 16 | Ngữ cảnh | Không có người thứ hai | Chưa thể so sánh | Ngữ cảnh |
| 17 | Ngầm | Không có người thứ hai | Chưa thể so sánh | Ngầm |
| 18 | Ngữ cảnh | Không có người thứ hai | Chưa thể so sánh | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Không có người thứ hai | Chưa thể so sánh | Giới hạn hệ thống |
| 20 | Hệ thống | Không có người thứ hai | Chưa thể so sánh | Hệ thống |

**Tỉ lệ đồng thuận độc lập:** chưa đo (chỉ có 1 người gắn nhãn; không tự điền 20/20).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 6, 9, 14: lỗi gốc là khách nhập/chọn sai nên là do người dùng; đề xuất cải thiện giao diện thuộc biện pháp khắc phục.
- Ca 8, 15: lỗi đã lộ ra và được nhân viên bắt được nên là lỗi hệ thống, không phải lỗi ngầm.
- Ca 13: ngoài phạm vi xử lý là giới hạn hệ thống, dù chất lượng chuyển tiếp có thể kém.
- Ca 18: phép tính đúng nhưng không khớp kỳ vọng/hoàn cảnh khách là ngữ cảnh.
- Ca 12: sai lệch chi phí không ai nhận ra cho tới kiểm tra là lỗi ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | `input_validation_failed`; cảnh báo khi >2% yêu cầu/ngày | Nhận diện mã sàn và tra mã vận đơn; nếu không được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: thông báo “đã hoàn” thiếu bản ghi sổ cái ok cùng trace_id; ngưỡng 0 | Chỉ báo hoàn khi sổ cái trả ok; sau 3 lần lỗi 503 chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo tuần, đếm mở lại vì số tiền dù kiểm tra thấy đúng | Tin nhắn ghi phép tính và cách tính khoản hoàn | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Đếm `handoff_to_staff` với reason `thieu_du_lieu` theo loại mỗi tuần | Chuyển kèm tóm tắt; loại `quoc_te` khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá; cảnh báo khi >1% sai | Xóa cache khi bảng giá đổi và ghi version vào trace | Kế toán trưởng |
