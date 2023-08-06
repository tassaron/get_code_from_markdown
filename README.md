# get_code_from_markdown

Extract code from within triple-quotes (```) in markdown files (code blocks).

Run the extracted code using `exec()` or `subprocess.run`.

## Getting code blocks from markdown files

```python
from get_code_from_markdown import *

blocks = get_code_from_markdown(["# get_code_from_markdown", "```python", "print('hello world')", "```"])
# or
blocks = get_code_from_markdown_filename("README.md", language="python")
# or
with open("README.md", "r") as f:
    blocks = get_code_from_markdown_file(f, language="python")
```

The `language` parameter defaults to `python`

## Running code blocks from markdown files

You can use a subprocess or just exec the code to see if it works.

```python
from get_code_from_markdown import *
blocks = ["print('hello world')"]

# run function uses exec() by default
run_code_from_markdown_blocks(blocks)

# you can choose to use subprocess output instead
# this will use python3 by default
run_code_from_markdown_blocks(blocks, method=RunMethods.SUBPROCESS)

# give arguments to specify a different command
run_code_from_markdown_blocks(blocks, method=RunMethods.SUBPROCESS(["python3", "-c"]))
```

## Format of outputted code blocks

The format is a list of `\n`-delimited strings, each representing a block of code from the parsed markdown file. You can split the code blocks further into individual lines of code with `string.split("\n")`

## Legal

This is a derivative work of [Codeblocks](https://github.com/shamrin/codeblocks) which provides a simpler version with less dependencies. It is covered by the same Apache license (see `LICENSE` file in this git repo). Use Codeblocks for its CLI and automatic formatting features.
