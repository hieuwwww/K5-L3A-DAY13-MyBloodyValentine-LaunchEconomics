# Báo cáo cá nhân/nhóm — Lab 13

## 1. Thông tin nhóm

- Tên nhóm: cá nhân / thành viên duy nhất.
- Lớp: L3A.
- Thành viên: Bùi Quang Hiếu (2A202603639); email và URL repo cần bổ sung.

## 2. Mục tiêu và cách tiếp cận

Mục tiêu là định giá chi phí mỗi việc thành công, đo chỉ số sử dụng/an toàn, phân loại lỗi và lập pilot có đối chứng. Làm bài một mình nên tôi tự thực hiện code, kiểm số, phân loại theo hướng dẫn và tổng hợp hồ sơ; không tuyên bố có hai người gắn nhãn độc lập.

## 3. Giải pháp

Nhiệm vụ A/B: triển khai mô hình trace và độ nhạy trong `src/lab13.py`, kết quả tại `bang_chi_phi.md`. Nhiệm vụ C: phân loại 20 ca theo taxonomy và ghi biện pháp khắc phục tại `bang_loi.md`; đồng thuận độc lập chưa đo. Nhiệm vụ D: tính cỡ mẫu và điền `pilot_plan.yaml`. Nhiệm vụ E: đặc tả chỉ số/event/rủi ro tại `chi_so.md`, quyết định tại `ho_so_launch_v0.md`.

## 4. Kết quả

Kết quả chính: CPS 4.472 đ (simulated); scope nội địa + hàng nặng sau fixed cost 4.599 đ ở 45.000 yêu cầu/tháng (simulated). Làm lại là yếu tố nhạy nhất (+51,8%, simulated). Chỉ số mô tả trong mẫu thử: 82,83% đóng trong 24h không mở lại; reopen 4,25%. Đề xuất Go có điều kiện cho pilot giới hạn `noi_dia` + `hang_nang`, chấp nhận MDE 6 điểm (power ~0,64 nếu tác động thật chỉ 5 điểm). Chưa có kết quả hội đồng chấm chéo; phiếu chấm được để pending, không tự chấm hồ sơ của mình.

## 5. Khó khăn và cách xử lý

Môi trường ban đầu thiếu pandas; cài các phụ thuộc đã khai báo vào `src/.venv` (được gitignore). Đọc CSV requests với `keep_default_na=False`. Tự kiểm tra số bằng cách chạy `python lab13.py` và so với số đối chiếu trong hướng dẫn. Một thành viên không thể đáp ứng yêu cầu gắn nhãn độc lập hoặc duyệt chéo; cần báo giảng viên/coach về cách xử lý.

## 6. Tổng hợp đóng góp

Thành viên duy nhất: Bùi Quang Hiếu (2A202603639), phụ trách code, kiểm số, phân loại lỗi và hồ sơ. Email và URL repo cần bổ sung trước khi nộp. Không có đóng góp giả định của thành viên khác.

## 7. Hạn chế và hướng cải thiện

Hạn chế: thời gian nhân viên là cột simulated; chưa có đo thời gian thực, chưa có đối chứng trong đợt chạy thử, không thể tính đồng thuận giữa hai người, và chưa có peer review. Cần hoàn tất các điều kiện tại hồ sơ launch, cung cấp thông tin cá nhân, hỏi coach về quy định nhóm đơn, và chấm nhóm được chỉ định khi có hồ sơ thật.

## 8. Tài liệu tham khảo và công cụ

Nguồn: tài liệu lab trong `docs/`, hai CSV giả lập trong `src/`, cùng hướng dẫn Google PAIR và công thức trong repo. Công cụ AI: OpenCode assistant hỗ trợ triển khai code/soạn cấu trúc; tôi tự chạy script, đối chiếu kết quả với đáp án hướng dẫn và cần tự giải thích các công thức trước khi trình bày.
