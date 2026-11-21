"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải thuộc (0, 1]')
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 <= p <= 1:
        raise ValueError('p phải thuộc [0, 1]')
    return 1.0 if k is None and p > 0 else (0.0 if k is None else 1 - (1 - p) ** k)


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    if thanh_cong == 0:
        raise ValueError('Không có xác suất thành công với các tham số đã cho')
    return so_lan_chay_ky_vong(p, k) / thanh_cong


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'].astype(int) > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].astype(float).sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].astype(float).sum() * luong_phut * he_so_lam_lai
    token, tool = float(tien_token.sum()), float(tien_tool.sum())
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong else math.inf
    return dict(token=token, tool=tool,
                chay_lai=float((tien_token + tien_tool)[runs['attempt'] > 1].sum()),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=cps,
                hoa_don_moi_yc=(token + tool) / len(reqs) if len(reqs) else math.nan)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Chi phí từ trace (các phút simulated)')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print('\nA3 · Theo loại; chi phí CPS dựa trên phút simulated')
    for loai, subset in reqs.groupby('loai'):
        res = mo_hinh(runs, subset)
        print(f"{loai:12s} n={len(subset):4d} success={res['thanh_cong']/len(subset):.1%} "
              f"runs/request={subset['so_lan_chay'].astype(int).mean():.2f} "
              f"CPS={res['cps']:,.0f} đ ({res['cps']/BASELINE:.2f}x)")
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    print('Tỷ lệ status=ok theo attempt:')
    print(merged.assign(ok=(merged.status == 'ok').astype(float))
          .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').to_string())

    scope = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    scope_res = mo_hinh(runs, scope)
    # A4 uses the lab's stated 900/1,200 scoped success fraction.
    success_rate = scope_res['thanh_cong'] / len(reqs)
    for monthly_volume in (45000, 22500):
        monthly_success = monthly_volume * success_rate
        fixed_per_success = 40_000_000 / monthly_success
        variable_cps = scope_res['tong'] / scope_res['thanh_cong']
        print(f'A4 {monthly_volume:,}/tháng: success={monthly_success:,.0f}, '
              f'fixed={fixed_per_success:,.0f}, CPS+fixed={variable_cps+fixed_per_success:,.0f} đ')

    print('\nB1 · Độ nhạy (CPS dùng simulated minutes)')
    base = ket_qua['cps']
    scenarios = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    for name, kwargs in scenarios.items():
        value = mo_hinh(runs, reqs, **kwargs)['cps']
        print(f'{name:25s} {value:9,.0f} đ {(value/base-1):+7.1%}')
    combo = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f'B2 token x2 + xem lại x2: {combo["cps"]:,.0f} đ ({combo["cps"]/base-1:+.1%})')

    print('\nB3 · Tổng chi phí hệ thống; staff fallback 12,000 đ/request')
    for cap in (1, 2, 3):
        res = mo_hinh(runs, reqs, max_lan_chay=cap)
        failed = len(reqs) - res['thanh_cong']
        print(f'{cap} lần: assistant={res["tong"]:,.0f}, failed={failed}, '
              f'system={res["tong"]+failed*BASELINE:,.0f}, CPS={res["cps"]:,.0f}')

    print('\nB4 · Xem lại 100% scope noi_dia + hang_nang')
    successful_trace_ids = set(runs.loc[(runs.status == 'ok') & runs.request_id.isin(scope.request_id), 'request_id'])
    review_count = len(successful_trace_ids)
    rework_count = (scope.ket_qua == 'lam_lai').sum()
    for minutes in (9, reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].astype(float).mean()):
        labor_review = review_count * 5 * LUONG_PHUT
        labor_rework = rework_count * minutes * LUONG_PHUT
        total = scope_res['token'] + scope_res['tool'] + labor_review + labor_rework
        print(f'lam_lai={minutes:.1f} min: CPS={total/scope_res["thanh_cong"]:,.0f} '
              f'({total/scope_res["thanh_cong"]/BASELINE:.2f}x) simulated')

    print('\nD1 · Cỡ mẫu và cụm')
    from statistics import NormalDist
    def co_mau(p1, p2, alpha=.05, power=.8):
        za = NormalDist().inv_cdf(1-alpha/2)
        zb = NormalDist().inv_cdf(power)
        pb = (p1+p2)/2
        return math.ceil((za*math.sqrt(2*pb*(1-pb)) + zb*math.sqrt(p1*(1-p1)+p2*(1-p2)))**2/(p2-p1)**2)
    n5, n6 = co_mau(.70, .75), co_mau(.70, .76)
    de75 = 1 + 74*.02
    m6 = math.ceil((n6*.98)/(20 - n6*.02))
    print(f'5 điểm: {n5:,}/arm; m=75 DE={de75:.2f}, n={math.ceil(n5*de75):,}/arm')
    print(f'20 staff/arm hiệu dụng max={20/.02:,.0f}; 6 depot/arm max={6/.02:,.0f}')
    print(f'6 điểm: {n6:,}/arm; 20 staff/arm cần tối thiểu {m6} yêu cầu/staff (DE={1+(m6-1)*.02:.2f})')

    print('\nE1 · Chỉ số hiện tại (descriptive, không suy luận tác động)')
    primary = ((reqs.dong_trong_24h.astype(int) == 1) & (reqs.mo_lai_trong_7_ngay.astype(int) == 0)).mean()
    reviewed = reqs[reqs.duoc_xem_lai.astype(int) == 1]
    ignored = reviewed.quyet_dinh_xem_lai.isin(['sua', 'bo']).mean()
    reopened = reqs.mo_lai_trong_7_ngay.astype(int).mean()
    print(f'primary={primary:.2%}; reviewed ignored/edited={ignored:.2%}; reopened_7d={reopened:.2%}')
