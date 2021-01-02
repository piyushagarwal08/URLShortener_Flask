import pytest
from urlshort import create_app

# fixtures helps fixing the testing situation
@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()