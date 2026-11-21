# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | trace + phút nhân viên | simulated (có thành phần simulated) |
| Số việc thành công | 978 | `ket_qua` | đo từ mẫu |
| Chi phí mỗi việc thành công | 4.472 | tổng / số thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (token + tool) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn chia số yêu cầu. Khoản làm lại lớn nhất: **51,8%** tổng chi phí (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× |

- `quoc_te` không phù hợp: CPS 22.515 đ (1,88×) và chỉ thành công 27,3% (simulated). Tỉ lệ ok theo attempt giảm 30,0% → 11,4% → 2,2%, nên chạy lại không khắc phục đủ.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× |

- Không đổi kết luận ở 45.000 yêu cầu/tháng (4.599 đ < 12.000 đ); khi khối lượng còn một nửa, tăng lên 5.784 đ nhưng vẫn thấp hơn chi phí nhân viên tự làm (simulated).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)**.
- Xếp hạng ba yếu tố: **1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated) | 4.111 đ (simulated) |
| 2 lần | 4.093.220 đ (simulated) | 234 | 6.901.220 đ (simulated) | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- Giới hạn 2 lần rẻ nhất cho công ty (**6.901.220 đ**); không trùng với CPS thấp nhất là 1 lần (**4.111 đ**), vì 1 lần chuyển thêm 85 ca sang nhân viên.

## B4 · Nếu phải xem lại tất cả

- Xem lại 100%: **11.743 đ = 0,98×** 12.000 đ với 9 phút làm lại; dùng thời lượng làm lại trung bình 15,3 phút (simulated), **12.415 đ = 1,03×**. Phần token/tool và thời gian đều theo scope.
- Pilot cần xác định mức xem lại tối an toàn và thời gian thực tế; nếu xem lại kéo dài 100%, tiết kiệm gần như biến mất (simulated).
