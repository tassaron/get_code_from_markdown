from . import readme
from get_code_from_markdown import run_code_from_markdown_blocks, RunMethods


def test_runmethod_subprocess_readme(readme):
    run_code_from_markdown_blocks(readme, method=RunMethods.SUBPROCESS)


def test_runmethod_default_readme(readme):
    run_code_from_markdown_blocks(readme)


def test_runmethod_custom_readme(readme):
    output = None

    def custom_run_method(block):
        nonlocal output
        output = block.split("\n", 1)[0]

    run_code_from_markdown_blocks(readme, method=custom_run_method)
    assert output == "from get_code_from_markdown import run_code_from_markdown_blocks"
