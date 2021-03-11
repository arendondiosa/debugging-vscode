import json


def test_endpoint(app, client):
    response = client.get("/test")

    assert response.status_code == 200
    expected = {"hello": "world"}
    assert expected == json.loads(response.get_data(as_text=True))


def test_endpoint_test_with_param(app, client):
    new_param = "test_param"

    response = client.get("/test/{}".format(new_param))

    assert response.status_code == 200
    expected = {"hello": new_param}
    assert expected == json.loads(response.get_data(as_text=True))
