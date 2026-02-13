import pytest
from get_code_from_markdown import get_code_from_markdown_filename


@pytest.fixture
def readme():
    """Provides readme using get methods while testing run methods"""
    return get_code_from_markdown_filename("README.md")
