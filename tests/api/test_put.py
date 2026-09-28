


def test_update_user_data(api_session):
    NEW_USER_DATA = {
        "email": "g.prg2@reqres.in",
        "first_name": "GleP",
        "last_name": "Prygunof",
        "avatar": "https://i.pinimg.com/736x/39/d1/75/39d1751f2b414d3bf09a3be071f65e93.jpg"

    }

    url, session = api_session

    response = session.put(f"{url}/api/users/2", json=NEW_USER_DATA)

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == NEW_USER_DATA["email"]
    assert data["first_name"] == NEW_USER_DATA["first_name"]
    assert data["last_name"] == NEW_USER_DATA["last_name"]
    assert data["avatar"] == NEW_USER_DATA["avatar"]

