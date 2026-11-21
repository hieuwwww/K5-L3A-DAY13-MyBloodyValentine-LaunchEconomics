import pandas as pd
import unittest

from lab13 import (
    he_so_chi_phi_moi_viec_thanh_cong,
    mo_hinh,
    so_lan_chay_ky_vong,
    ti_le_thanh_cong,
)


class Lab13Tests(unittest.TestCase):
    def test_known_retry_values(self):
        self.assertAlmostEqual(so_lan_chay_ky_vong(0.8, 2), 1.2)
        self.assertAlmostEqual(so_lan_chay_ky_vong(0.8), 1.25)
        self.assertAlmostEqual(ti_le_thanh_cong(0.8, 3), 0.992)
        self.assertAlmostEqual(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), 1.25)

    def test_zero_successes_report_infinite_cost_and_keep_all_trace_costs(self):
        runs = pd.DataFrame([{
            "request_id": "r1", "attempt": 1, "tokens_in": 1000,
            "tokens_out": 1000, "tool_calls": 1,
        }])
        reqs = pd.DataFrame([{
            "request_id": "r1", "so_lan_chay": 1, "ket_qua": "chuyen_nhan_vien",
            "phut_xem_lai_simulated": 0, "phut_lam_lai_simulated": 0,
        }])
        result = mo_hinh(runs, reqs)
        self.assertAlmostEqual(result["token"], 156)
        self.assertAlmostEqual(result["tool"], 15)
        self.assertEqual(result["thanh_cong"], 0)
        self.assertEqual(result["cps"], float("inf"))

    def test_retry_cap_transfers_over_cap_request_and_excludes_later_run(self):
        runs = pd.DataFrame([
            {"request_id": "r1", "attempt": 1, "tokens_in": 1000, "tokens_out": 0, "tool_calls": 0},
            {"request_id": "r1", "attempt": 2, "tokens_in": 1000, "tokens_out": 0, "tool_calls": 0},
        ])
        reqs = pd.DataFrame([{
            "request_id": "r1", "so_lan_chay": 2, "ket_qua": "thanh_cong",
            "phut_xem_lai_simulated": 1, "phut_lam_lai_simulated": 1,
        }])
        result = mo_hinh(runs, reqs, max_lan_chay=1)
        self.assertAlmostEqual(result["token"], 26)
        self.assertEqual(result["thanh_cong"], 0)
        self.assertEqual(result["xem_lai"], 0)
        self.assertEqual(result["lam_lai"], 0)


if __name__ == "__main__":
    unittest.main()
