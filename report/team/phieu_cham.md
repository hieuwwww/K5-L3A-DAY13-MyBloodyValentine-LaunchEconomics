# Phiếu chấm hội đồng Gate 2a

**Trạng thái: Đã chấm theo hồ sơ và ghi nhận câu trả lời phản biện do nhóm được chấm cung cấp.** Đây là đánh giá của Bùi Quang Hiếu đối với nhóm HAHAHA, không phải điểm nhóm khác chấm bài của Bùi Quang Hiếu. Hồ sơ đối chiếu tại commit [`5b017aa`](https://github.com/Ein05/K5-L3A-DAY13-HAHAHA-LaunchEconomics/tree/5b017aa53c93140121523a8e2501c48aa34ba560).

- Nhóm chấm (hội đồng): MyBloodyValentine — Bùi Quang Hiếu (chấm cá nhân).
- Nhóm được chấm: HAHAHA.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | [Hồ sơ launch](https://github.com/Ein05/K5-L3A-DAY13-HAHAHA-LaunchEconomics/blob/5b017aa53c93140121523a8e2501c48aa34ba560/report/team/ho_so_launch_v0.md) đề xuất Go có điều kiện, loại `quoc_te` (22.515 đ/việc = 1,88× mức nhân viên tự làm); nêu kịch bản xem lại 100% có thể lên 12.414 đ/việc (1,03×) và điều kiện giảm xem lại. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 5 | Phạm vi `noi_dia` + `hang_nang` có lý do bằng số; nhiều khoản đã ghi `simulated`. Tuy nhiên, các giá trị 4.723 đ và 4.346 đ ở [bảng B1](https://github.com/Ein05/K5-L3A-DAY13-HAHAHA-LaunchEconomics/blob/5b017aa53c93140121523a8e2501c48aa34ba560/report/team/bang_chi_phi.md) vẫn bao gồm chi phí thời gian giả lập nhưng không có nhãn tại dòng, nên chưa đạt mức 10 về nhãn ở mọi số giả lập. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | [Pilot plan](https://github.com/Ein05/K5-L3A-DAY13-HAHAHA-LaunchEconomics/blob/5b017aa53c93140121523a8e2501c48aa34ba560/report/team/pilot_plan.yaml) chia ngẫu nhiên theo nhân viên, phân tầng depot, đối chứng đồng thời; 20 nhân viên/nhánh, MDE 6 điểm, giả định ít nhất 299 yêu cầu/nhân viên. Ba luật dừng nêu ngưỡng, thời hạn và vai trò hành động; câu trả lời phản biện bên dưới làm rõ cách xử lý khi chưa đủ khối lượng. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của người chấm:** Go có điều kiện cho kế hoạch pilot trong phạm vi đã nêu; không phải phê duyệt triển khai chính thức.

**Lý do:** Đề xuất tính đến chi phí và rủi ro bất lợi, pilot có đối chứng và luật dừng; cần bổ sung nhãn cho một số kết quả còn dùng thời gian giả lập.

**Một câu hỏi cho đội trình:** Kế hoạch cần ít nhất 299 yêu cầu/nhân viên và 20 nhân viên mỗi nhánh để đạt MDE 6 điểm. Nếu đến ngày quyết định chưa đủ số yêu cầu này, nhóm sẽ kéo dài pilot hay thay đổi tiêu chí ra quyết định? Ai phê duyệt thay đổi đó?

**Câu trả lời của đội trình (do người chấm chuyển lại, chưa kiểm chứng việc thực thi):** “Nếu đến ngày quyết định chưa đủ 5.980 yêu cầu mỗi nhánh (20 nhân viên × 299 yêu cầu), Giám đốc vận hành phê duyệt gia hạn pilot, giữ nguyên MDE và các ngưỡng đã đăng ký trước. Nếu hết thời hạn gia hạn vẫn thiếu mẫu, kết luận chưa đủ bằng chứng và không mở rộng pilot; mọi thay đổi tiêu chí phải được Giám đốc vận hành phê duyệt trước khi xem dữ liệu tiếp theo.”
