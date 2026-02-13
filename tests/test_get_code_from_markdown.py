from get_code_from_markdown import get_code_from_markdown_filename


def test_getcode_readme_starts_with_import():
    blocks = get_code_from_markdown_filename("README.md")
    assert blocks[0].split("\n", 1)[0] == "from get_code_from_markdown import *"
