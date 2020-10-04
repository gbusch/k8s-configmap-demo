Feature: Stage
    As a user
    I want to be able to retrieve the stage
    so that I know to which stage I am connected

    Scenario: Get stage.
        When I request the stage
        Then it is «local»