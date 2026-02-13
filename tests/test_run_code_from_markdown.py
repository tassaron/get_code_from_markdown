from . import readme
from get_code_from_markdown import run_code_from_markdown_blocks, RunMethods


def test_runmethod_subprocess_readme(readme):
    run_code_from_markdown_blocks(readme, method=RunMethods.SUBPROCESS)


def test_runmethod_default_readme(readme):
    run_code_from_markdown_blocks(readme)
