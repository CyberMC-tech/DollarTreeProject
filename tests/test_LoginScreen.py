from requests.cookies import MockResponse

from ui.updated_first_screen import LoginScreen


# Generated by CodiumAI

# Dependencies:
# pip install pytest-mock


class TestLoginScreen:

    #  Login with valid username and password
    def test_valid_login(self, mocker):
        # Mock the requests.post method to return a 200 response
        mocker.patch(
            "requests.post",
            return_value=MockResponse(200, {"username": "test", "password": "test"}),
        )

        # Create an instance of LoginScreen
        login_screen = LoginScreen()

        # Set the username and password
        login_screen.username.text = "test"
        login_screen.password.text = "test"

        # Call the login method
        login_screen.login()

        # Assert that the employee info is set correctly
        assert (
            login_screen.manager.get_screen("home_screen").employee.first_name == "test"
        )
        assert (
            login_screen.manager.get_screen("home_screen").employee.last_name == "test"
        )
        assert (
            login_screen.manager.get_screen("home_screen").employee.full_name == "test"
        )

    #  Login with invalid username and password
    def test_invalid_login(self, mocker):
        # Mock the requests.post method to return a non-200 response
        mocker.patch("requests.post", return_value=MockResponse(401, {}))

        # Create an instance of LoginScreen
        login_screen = LoginScreen()

        # Set the username and password
        login_screen.username.text = "test"
        login_screen.password.text = "test"

        # Call the login method
        login_screen.login()

        # Assert that the toast message is displayed
        assert login_screen.manager.get_screen("home_screen").employee is None
        assert toast.called

    #  Network request succeeds with 200 status code
    def test_network_request_success(self, mocker):
        # Mock the requests.post method to return a 200 response
        mocker.patch(
            "requests.post",
            return_value=MockResponse(200, {"username": "test", "password": "test"}),
        )

        # Create an instance of LoginScreen
        login_screen = LoginScreen()

        # Set the username and password
        login_screen.username.text = "test"
        login_screen.password.text = "test"

        # Call the perform_login method directly
        login_screen.perform_login()

        # Assert that the employee info is set correctly
        assert (
            login_screen.manager.get_screen("home_screen").employee.first_name == "test"
        )
        assert (
            login_screen.manager.get_screen("home_screen").employee.last_name == "test"
        )
        assert (
            login_screen.manager.get_screen("home_screen").employee.full_name == "test"
        )

    #  Login with empty username and password
    def test_empty_login(self, mocker):
        # Create an instance of LoginScreen
        login_screen = LoginScreen()

        # Set the username and password to empty strings
        login_screen.username.text = ""
        login_screen.password.text = ""

        # Call the login method
        login_screen.login()

        # Assert that the toast message is displayed
        assert login_screen.manager.get_screen("home_screen").employee is None
        assert toast.called

    #  Login with whitespace-only username and password
    def test_whitespace_login(self, mocker):
        # Create an instance of LoginScreen
        login_screen = LoginScreen()

        # Set the username and password to whitespace-only strings
        login_screen.username.text = "   "
        login_screen.password.text = "   "

        # Call the login method
        login_screen.login()

        # Assert that the toast message is displayed
        assert login_screen.manager.get_screen("home_screen").employee is None
        assert toast.called

    #  Login with special characters in username and password
    def test_special_characters_login(self, mocker):
        # Create an instance of LoginScreen
        login_screen = LoginScreen()

        # Set the username and password to strings with special characters
        login_screen.username.text = "!@#$%^&*"
        login_screen.password.text = "!@#$%^&*"

        # Call the login method
        login_screen.login()

        # Assert that the toast message is displayed
        assert login_screen.manager.get_screen("home_screen").employee is None
        assert toast.called
