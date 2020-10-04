Feature: Greeting
    As a user
    I want to be greeted with name
    so that I feel valued.

    Scenario: Hello with name.
        Given the user's name is Gerold
        When he requests a greeting
        Then he is greeted with
            """
            Hi Gerold.
            """

    Scenario: Hello without name.
        Given no user name is given
        When he requests a greeting
        Then he is greeted with
            """
            Hi World.
            """
