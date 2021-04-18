# site of the REST WEBAPI : https://reqres.in/
# Then get the request : api/users?page=2
#  https://reqres.in/api/users?page=2


import allure
import pytest
import requests


# global response
# global url
# url = "https://reqres.in/api/users?page=2"


# print result of response
@pytest.fixture()
def TestSetup():
    global response
    response = requests.get("https://reqres.in/api/users?page=2")
    yield
    response.close()


@allure.description("Validate Gets")
@allure.severity(severity_level="CRITICAL")
def testGetContent(TestSetup):
    response = requests.get("https://reqres.in/api/users?page=2")
    print(response)

    # print response content

    print("\nAPI Content is :", response.content)
    print("\n")


@allure.description("Get headers")
@allure.severity(severity_level="CRITICAL")
def testGetHeader(TestSetup):
    response = requests.get("https://reqres.in/api/users?page=2")
    # print header of the response
    print("\n")
    print("\nAPI Header is :", response.headers)
    assert True


@allure.description("Get URL")
@allure.severity(severity_level="CRITICAL")
def testGetURL(TestSetup):
    response = requests.get("https://reqres.in/api/users?page=2")
    print("\n")
    print("\nAPI URL is :", response.url)
    assert True


# POST

payload = {
    "name": "Jojo Silvestre San Diego",
    "job": "Automation Tester"
}


# print(payload)


# PUT DATA CREATE

@allure.description("POST DATA")
@allure.severity(severity_level="CRITICAL")
def test_POST(TestSetup):
    resp = requests.put("https://reqres.in/api/users/2", data=payload)
    print(resp)
    print(resp.json)
    print(resp.headers.get("Content-Type"))
    assert resp.json()['job'] == 'Automation Tester', "Incorrect job"


# PATCH
@allure.description("PATCH DATA")
@allure.severity(severity_level="CRITICAL")
def test_PATCH(TestSetup):
    resp1 = requests.patch("https://reqres.in/api/users/2", data=payload)
    print(resp1)
    print(resp1.json)
    print(resp1.headers.get("Content-Type"))
    assert resp1.json()['job'] == 'Automation Tester', "Incorrect job"

# def test_DELETE(TestSetup):
#     resp3 = requests.delete("https://reqres.in/api/users/2")
#     print(resp3.status_code)
#     assert resp3.status_code ==204, "user deletion failed"
