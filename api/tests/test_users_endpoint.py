import pytest


def test_user_list_status_code(reqres_client):
    response = reqres_client.get_users(page=1)
    assert response.status == 200


def test_user_data_structure(reqres_client):
    response = reqres_client.get_users(page=1)
    data = response.json()

    assert len(data["data"]) > 0

    user = data["data"][0]
    expected_fields = ["id", "email", "first_name", "last_name", "avatar"]

    for field in expected_fields:
        assert field in user


def test_user_data_types_and_logic(reqres_client):

    response = reqres_client.get_users(page=1)
    user = response.json()["data"][0]
    actual_id = user["id"]
    actual_first_name = user["first_name"]
    actual_email = user["email"]

    assert isinstance(user["id"], int), f"Az ID típusa {type(actual_id)}"
    assert isinstance(user["first_name"], str), f"A First Name típusa {type(actual_first_name)}"
    assert "@" in user["email"], f"Az aktuális email {user[actual_email]}"