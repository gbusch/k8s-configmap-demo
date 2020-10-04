import requests
from behave import given, then, when


@then("he is greeted with")
def assert_greeting(context):
    expected = context.text
    actual = context.result.text
    assert actual == expected, f"Expected: {expected}, but got: {actual}"


@when("he requests a greeting")
def request_greeting(context):
    context.result = requests.get(f"http://localhost:8080?name={context.name}")


@given("no user name is given")
def set_no_name(context):
    context.name = ""


@given("the user's name is {name}")
def set_name(context, name):
    context.name = name
