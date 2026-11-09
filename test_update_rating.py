import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"

# Boundary values for an update: ทดสอบดาว 0, 1, 5, 6
@pytest.mark.parametrize("stars, expected_status", [
    (0, 400),
    (1, 200),
    (5, 200),
    (6, 400),
])
def test_update_rating_boundary(api, auth, rating, stars, expected_status):
    path = f"/api/ratings/{rating['id']}"
    
    # ส่งคำขออัปเดตจำนวนดาว
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_status
    
    # อ่านค่ากลับมาตรวจสอบ
    get_res = api.get(path, headers=auth)
    assert get_res.status_code == 200
    
    if expected_status == 200:
        # ถ้าสำเร็จ ดาวต้องเปลี่ยนเป็นค่าใหม่
        assert get_res.json()["stars"] == stars
    else:
        # ถ้าล้มเหลว (400) ดาวต้องคงเดิมจากค่าเริ่มต้นของ fixture (ซึ่งคือ 3 ดาว)
        assert get_res.json()["stars"] == 3