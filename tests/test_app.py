import sys
import os
import pytest
from flask import Flask, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/webapp')))
from app import app as flask_app

@pytest.fixture
def app():
    return flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(client):
    """Test the index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<div>' in response.data  
