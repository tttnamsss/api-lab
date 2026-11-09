# A other user cannot read the rating of another user.
def test_other_user_cannot_read_rating(api, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.get(path, headers=other_auth)
    print(res.status_code)
    assert 400 <= res.status_code < 500

# A other user cannot update the rating of another user.
def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 5}, headers=other_auth)
    print(res.status_code)
    assert 400 <= res.status_code < 500
    
    # ตรวจสอบว่าเรตติ้งของเจ้าของเดิมไม่ถูกเปลี่ยน
    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200
    assert owner_res.json()["stars"] == rating["stars"]

# A other user cannot delete the rating of another user.
def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    print(res.status_code)
    assert 400 <= res.status_code < 500
    
    # ตรวจสอบว่าเรตติ้งยังคงอยู่ (เจ้าของเดิมยังอ่านเจอ)
    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200