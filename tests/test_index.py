import pytest
from src.visitor import index

def test_index():
    html = index.visit_digolds()
    assert html.status_code == 200