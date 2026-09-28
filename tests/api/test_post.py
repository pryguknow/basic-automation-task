


def test_create_user(api_session):
    USER_DATA = {
        "email": "g.prg@reqres.in",
        "first_name": "Gleb",
        "last_name": "Prygunov",
        "avatar": "https://i.pinimg.com/736x/39/d1/75/39d1751f2b414d3bf09a3be071f65e93.jpg"

    }
    url, session = api_session

    response = session.post(f"{url}/api/users", json=USER_DATA)
    data = response.json()

    assert response.status_code == 201
    assert int(data["id"]) > 0
    assert data["email"] == USER_DATA["email"]
    assert data["first_name"] == USER_DATA["first_name"]
    assert data["last_name"] == USER_DATA["last_name"]
    assert data["avatar"] == USER_DATA["avatar"]
