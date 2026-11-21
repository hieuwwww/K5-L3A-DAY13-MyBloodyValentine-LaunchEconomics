# Báo cáo cá nhân — Bùi Quang Hiếu (2A202603639)

## 1. Thông tin thành viên

- Họ tên: Bùi Quang Hiếu
- MSSV: 2A202603639
- Email: chưa cung cấp
- Lớp: L3A
- Vai trong nhóm: thành viên duy nhất; viết code, kiểm số, phân loại lỗi và giữ hồ sơ. Không có người gắn nhãn thứ hai nên không đo đồng thuận độc lập.

## 2. Phần việc phụ trách

Hoàn thiện mô hình chi phí và các phân tích A–E; lập hồ sơ launch v0 và pilot plan cho phạm vi đề xuất.

## 3. Đóng góp cụ thể

- Triển khai phép tính chi phí trên mọi lần chạy, tính chi phí thành công và thử giới hạn retry trong `src/lab13.py`.
- Tính theo loại yêu cầu, độ nhạy, chi phí cả hệ thống, kịch bản review toàn bộ và cỡ mẫu pilot.
- Điền `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md` và `TEAM.md`.
- Đánh dấu rõ số dùng phút `*_simulated`; không khẳng định có phân loại độc lập hoặc peer review.

## 4. Bằng chứng

- A1: 1,20 · 1,25 · 1,25; ba phép thử đạt.
- A2: token 245.585 đ, tool 84.000 đ, tổng 4.373.585 đ, 978 việc thành công; CPS 4.472 đ (simulated).
- Độ nhạy: làm lại tăng gấp đôi đưa CPS lên 6.787 đ (+51,8%, simulated).
- Pilot: 20 nhân viên mỗi arm; MDE 6 điểm, 859 yêu cầu/arm; power khoảng 0,64 nếu tác động thực là 5 điểm.
- Tự kiểm tra: `python -m unittest -v test_lab13` (3 test đạt), `python lab13.py`, YAML parse, `git diff --check`.

## 5. Công cụ AI đã dùng

OpenCode assistant hỗ trợ diễn giải yêu cầu, triển khai code và soạn cấu trúc báo cáo. Tôi tự chạy script và kiểm thử, đối chiếu kết quả với hướng dẫn trong repo; cần tự giải thích công thức và quyết định pilot khi trình bày.

## 6. Tự đánh giá

Đã hoàn thiện phần tính toán và tài liệu trong phạm vi dữ liệu có sẵn. Hạn chế: làm một mình nên không thể có hai bộ nhãn độc lập; chưa có hồ sơ nhóm khác để chấm; email và URL repo chưa được cung cấp.
