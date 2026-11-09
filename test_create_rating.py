import pytest 
STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)" 
AUTH_ERROR = "authentication failed"

# Base choice: 3 stars as a whole number, a real pizza, the user's token. 
def test_base_choice_is_saved(api, auth, pizza_id): 
    new = {"pizza_id": pizza_id, "stars": 3} 
    res = api.post("/api/ratings", json=new, headers=auth) 
    assert res.status_code == 201 
    assert res.json()["stars"] == 3 
    assert res.json()["pizza_id"] == pizza_id 
    
# C1: a number of stars below 1 or above 5 is refused with a message. 
@pytest.mark.parametrize("stars", [0, 6]) 
def test_stars_out_of_range(api, auth, pizza_id, stars): 
    new = {"pizza_id": pizza_id, "stars": stars} 
    res = api.post("/api/ratings", json=new, headers=auth) 
    assert res.status_code == 400 
    assert res.json() == {"error": STARS_ERROR} 
    
# C2: start type: whole number (base), decimal, text, missing
def test_stars_decimal(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3.5}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400

def test_stars_text(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": "3"}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400

def test_stars_missing(api, auth, pizza_id):
    new = {"pizza_id": pizza_id}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
        
# C3: exists (base), does not exist 
def test_pizza_not_exist(api, auth):
    new = {"pizza_id": 999999999, "stars": 3}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
    
# C4: the user's own (base), none, wrong length 
def test_token_none(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new)
    assert res.status_code == 401
    assert res.json() == {"error": AUTH_ERROR}
    
def test_token_wrong_length(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    wrong_auth = {"Authorization": "token short"}
    res = api.post("/api/ratings", json=new, headers=wrong_auth)
    assert res.status_code == 401
    assert res.json() == {"error": AUTH_ERROR}