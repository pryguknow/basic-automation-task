

def test_delete_user(api_session):
    url, session = api_session

    response = session.delete(f"{url}/api/users/2")
    assert response.status_code == 204
