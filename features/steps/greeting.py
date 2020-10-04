import requests
from behave import given, then, when


@then("he is greeted with")
def assert_greeting(context):
    assert context.result.text == context.text


@when("he requests a greeting")
def request_greeting(context):
    context.result = requests.get(f"http://localhost:8080?name={context.name}")


@given("no user name is given")
def set_no_name(context):
    context.name = ""


@given("the user's name is {name}")
def set_name(context, name):
    context.name = name
