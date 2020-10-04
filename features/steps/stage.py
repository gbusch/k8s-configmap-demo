import requests
from behave import then, when


@then("it is «{expected}»")
def assert_stage(context, expected):
    actual = context.result.text
    assert actual == expected, f"Expected: {expected}, got {actual}"


@when("I request the stage")
def request_stage(context):
    context.result = requests.get(f"http://localhost:8080/stage")