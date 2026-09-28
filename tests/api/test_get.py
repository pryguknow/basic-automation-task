
def test_get_user_data(api_session):
    url, session = api_session
    response = session.get(f'{url}/api/users/2')

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["id"] == 2
    assert data["first_name"] == "Janet"
    assert data["last_name"] == "Weaver"
    assert data["email"] == "janet.weaver@reqres.in"

