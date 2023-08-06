from get_code_from_markdown import *


def test_subprocess_readme():
    run_code_from_markdown_blocks(
        get_code_from_markdown_filename("README.md"), method=RunMethods.SUBPROCESS
    )


def test_exec_readme():
    run_code_from_markdown_blocks(get_code_from_markdown_filename("README.md"))


def test_readme_starts_with_import():
    blocks = get_code_from_markdown_filename("README.md")
    assert blocks[0].split("\n", 1)[0] == "from get_code_from_markdown import *"
