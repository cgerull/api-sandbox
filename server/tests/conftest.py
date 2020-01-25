"""Setup and fixtures for pytest"""
import pytest
from app import app

@pytest.fixture(scope='module')
def test_app():
    app.config['TESTING'] = True
    my_test_app = app

    ctx = app.app_context()
    ctx.push()

    yield my_test_app

    ctx.pop()

    
@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    my_test_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield my_test_client

    ctx.pop()

# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = create_app('flask_test.cfg')
 
#     # Flask provides a way to test your application by exposing the Werkzeug test Client
#     # and handling the context locals for you.
#     testing_client = flask_app.test_client()
 
#     # Establish an application context before running the tests.
#     ctx = flask_app.app_context()
#     ctx.push()
 
#     yield testing_client  # this is where the testing happens!
 
#     ctx.pop()