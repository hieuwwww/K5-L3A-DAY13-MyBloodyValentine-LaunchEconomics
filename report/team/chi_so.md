# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83% (994/1.200)**; mô tả đợt chạy thử |
| Dùng | Tỉ lệ bỏ qua hoặc sửa gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12% (48/177)** |
| An toàn | Tỉ lệ mở lại trong 7 ngày | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25% (51/1.200)** |
| Dùng | Tỉ lệ yêu cầu nhóm can thiệp được mở bằng trợ lý | số request có event `agent_suggestion_shown` / số request thuộc arm can thiệp | Chưa đo được từ mẫu hiện tại |
| An toàn | Tỉ lệ đơn hoàn sai tiền trong audit mẫu tuần | audit sai số tiền / số đơn được audit | Chưa đo được từ mẫu hiện tại |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi |
| `agent_run_completed` | Agent | attempt, tokens_in/out, tool_calls, status, trace_id | Mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | giu/sua/bo, phut_xem_lai đo thật, trace_id | Khi quyết định |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng ticket |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `ticket_closed` nối `ticket_reopened` theo request_id/trace_id và timestamp. Chỉ số dùng: `staff_review_decision` hoặc `agent_suggestion_shown`. An toàn: `ticket_reopened`; sai tiền cần `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

Các ngưỡng trong cột dấu hiệu theo dõi là ngưỡng vận hành **đề xuất cho pilot**, chưa được chủ vai trò xác nhận và không phải ngưỡng suy ra từ độ nhạy thống kê.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS tăng 51,8% lên 6.787 đ (simulated) | Tỉ lệ làm lại theo tuần >7%; đợt thử trong scope 4,9% (simulated) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Xem lại 100% kéo dài | 11.743 đ = 0,98×; nếu làm lại 15,3 phút thì 12.415 đ = 1,03× (simulated) | Tỉ lệ xem lại >50% ở cuối rollout 0.25 | Hạ xem lại theo bậc chỉ khi sửa+bỏ dưới 15%, giữ audit an toàn | Trưởng nhóm CSKH |
| Khối lượng chỉ còn một nửa | Fixed cost tăng từ 1.185 đ lên 2.370 đ/việc; CPS tổng 5.784 đ (simulated) | Thành công theo tuần <50% kế hoạch | Không mở rollout tiếp; xem lại giả định chi phí cố định | PM trợ lý hoàn phí |
