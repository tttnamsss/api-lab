import uuid 

def test_name_already_taken(api): 
    name = "lab-" + uuid.uuid4().hex[:12] 
    user = {"username": name, "password": "Pizza-2026"} 
    res = api.post("/api/users", json=user) 
    assert res.status_code == 201 
    
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}
    
def test_login_wrong_pass(api):
    name = "lab-" + uuid.uuid4().hex[:12] 
    user = {"username": name, "password": "Pizza-2026"} 
    res = api.post("/api/users", json=user) 
    assert res.status_code == 201 
    
    res = api.post("/api/users/token/login", json={"username": name, "password": "Pizza"}) 
    assert res.status_code == 401 
    assert res.json() ==  {"error": "authentication failed"}    
    
def test_empty_name(api):
    user = {"username": "", "password": "Pizza-2026"} 
    res = api.post("/api/users", json=user) 
    assert res.status_code == 400 
    assert res.json() ==  {"error": "username field is empty"} 
    