# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: cá nhân / thành viên duy nhất · Thành viên: Bùi Quang Hiếu · MSSV: 2A202603639 · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công (simulated), chưa gồm cố định; scope + cố định 4.599 đ ở 45.000 yêu cầu/tháng | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại +51,8% → 6.787 đ; xem lại +40,7% → 6.292 đ; lương +23,1% → 5.506 đ (simulated) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Cả hệ thống ở giới hạn 3 lần: (4.373.585 + 222×12.000)/1.200 = 5.865 đ/yêu cầu, so với 12.000 đ (simulated) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | 82,83%; 27,12%; 4,25% trong mẫu chạy thử; chưa có đối chứng nên không quy kết tác động | Xong, có bằng chứng | Người viết code |
| 5 · Bảng lỗi và cách khắc phục | 5 loại, 5 biện pháp đo được; chưa có đánh giá đồng thuận độc lập do chỉ 1 người | Chưa | Vai trò đề xuất: người gắn nhãn / giữ hồ sơ |
| 6 · Pilot plan | 20 staff/arm; MDE 6 điểm, n=859/arm, power ~0,64 nếu hiệu quả thật 5 điểm; 3 luật dừng | Xong, có bằng chứng | Vai trò đề xuất: Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Xem lại 100%: 11.743 đ (0,98×), hoặc 12.415 đ (1,03×) nếu rework 15,3 phút (simulated) | Giả lập | Vai trò đề xuất: PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ gồm `noi_dia` và `hang_nang`; không mở rộng sang loại khác. Đây là đề xuất giả định của bài tập, không phải cam kết đã nhận từ chủ vai trò. Điều kiện trước khi bắt đầu: (1) vai trò đề xuất Kỹ sư trưởng agent sửa chống hoàn trùng và đối soát sổ cái trước 2026-12-20; (2) vai trò đề xuất Giám đốc vận hành ký chấp nhận MDE 6 điểm và power ~0,64 nếu tác động thật là 5 điểm trước 2026-12-20; (3) vai trò đề xuất PM bật đủ event `trace_id` và thay phút simulated bằng đo thật trong tuần đầu; (4) vai trò đề xuất Trưởng nhóm CSKH phê duyệt lộ trình giảm review theo bậc trước 2026-12-20. Nếu không đạt điều kiện, No-go cho khởi động pilot và quay lại Gate 2a sau khi đóng các việc này.
