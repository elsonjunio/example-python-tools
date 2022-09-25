# example-python-tools
Helper tools for python development

### Poetry
Poetry is a tool for dependency management. [https://python-poetry.org/docs/](https://python-poetry.org/docs/).

```bash
# Install on Linux, Mac, Windows(WSL)
$ curl -sSL https://install.python-poetry.org | python3 -
```

### Pyenv
Pyenv lets you keep multiples versions of Python. [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

```bash
# Install on Mac
$ brew update
$ brew install pyenv
# Enviroment configurations
$ pyenv init
```

To install and use the Python 3.10.2 in the current project

```bash
$ pyenv install 3.10.2
$ pyenv local 3.10.2
$ python --version
Python 3.10.2
```

### Configuring a project

```bash
# Starting a project using poetry
$ poetry init

# Install Packages
$ poetry add <package> # Install packages
$ poetry add --dev <package> # Install packages to development environment

# Creating a virtual environment
$ poetry install

# or create a virtual environment for a specific python version
$ poetry env use python3.9

# Getting environment information
$ poetry env info

# Enabling the virtual environment
$ poetry shell

```

## Tools

- ### mypy
Mypy is a static type checker. [http://mypy-lang.org/](http://mypy-lang.org/)

```bash
$ mypy code/main.py

code/main.py:22: error: Incompatible types in assignment (expression has type "int", variable has type "str")
code/main.py:31: error: List item 0 has incompatible type "int"; expected "List[int]"
code/main.py:31: error: List item 1 has incompatible type "int"; expected "List[int]"
code/main.py:40: error: List item 1 has incompatible type "str"; expected "int"
code/main.py:50: error: Incompatible types in assignment (expression has type "float", variable has type "Union[str, int]")
code/main.py:66: error: Argument 2 to "mySum" has incompatible type "str"; expected "Union[int, float, None]"
code/main.py:88: error: Argument 1 to "execute" has incompatible type "Callable[[float, float], float]"; expected "Callable[[int, int], int]"
Found 7 errors in 1 file (checked 1 source file)
```
- ### blue
Blue is a code formatter. [https://blue.readthedocs.io/en/latest/](https://blue.readthedocs.io/en/latest/)

```bash
# To install a specific version of blue
$ poetry add --dev blue:0.9.0

# Usage
$ blue code/main.py
reformatted code/main.py
```

Using on VSCode: .vscode/settings.json
```json
{
    "python.languageServer": "Pylance",
    "python.analysis.autoSearchPaths": true,
    "python.analysis.autoImportCompletions": true,
    "code-runner.ignoreSelection": true,
    "code-runner.runInTerminal": true,
    "python.linting.mypyEnabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "blue",
    "python.testing.unittestEnabled": true,
    "code-runner.executorMap": {
        "python": "/Users/elsonsilva/Library/Caches/pypoetry/virtualenvs/example-python-tools-fuXY9vTO-py3.9/bin/python",
    },
    "editor.formatOnSave": true,
    "python.linting.flake8Args": [
        "--max-line-length=79"
    ],
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/Thumbs.db": true,
        "**/.classpath": true,
        "**/.project": true,
        "**/.settings": true,
        "**/.factorypath": true
    },
    "explorerExclude.backup": null,
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./test",
        "-p",
        "*_test.py"
    ],
    "python.testing.pytestEnabled": false
}
```

- ### isort
Isort is a utility to sort imports alphabetically. [https://github.com/PyCQA/isort](https://github.com/PyCQA/isort)

```bash
# Install isort
$ poetry add --dev isort

# Usage
$ isort .
Fixing /Users/elsonsilva/Workspace/Python/example-python-tools/code/main.py
Skipped 1 files
```

- ### mkdocs

```bash
$ mkdocs new .
$ mkdocs serve
```

- ### prospector

Prospector is a tool to analyze python code. 

```bash
$ poetry add --dev prospector
$ prospector
Messages
========

code/main.py
  Line: 53
    pylint: no-else-return / Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (col 4)
    pylint: consider-merging-isinstance / Consider merging these isinstance calls to isinstance(y, (float, int)) (col 7)



Check Information
=================
         Started: 2022-09-25 02:09:39.355931
        Finished: 2022-09-25 02:09:39.818453
      Time Taken: 0.46 seconds
       Formatter: grouped
        Profiles: default, no_doc_warnings, no_test_warnings, strictness_medium, strictness_high, strictness_veryhigh, no_member_warnings
      Strictness: None
  Libraries Used: 
       Tools Run: dodgy, mccabe, profile-validator, pycodestyle, pyflakes, pylint
  Messages Found: 2
 External Config: pylint: /Users/elsonsilva/Workspace/Python/example-python-tools/pyproject.toml

# Specific tool
$ prospector --with-tool pep257
Messages
========

.
  Line: None
    prospector: Deprecation / Tool pep257 has been renamed to pydocstyle. The old name pep257 is now deprecated and will be removed in Prospector 2.0. Please update your prospector configuration.

code/main.py
  Line: 54
    pylint: no-else-return / Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (col 4)
    pylint: consider-merging-isinstance / Consider merging these isinstance calls to isinstance(y, (float, int)) (col 7)



Check Information
=================
         Started: 2022-09-25 02:27:38.391864
        Finished: 2022-09-25 02:27:38.934279
      Time Taken: 0.54 seconds
       Formatter: grouped
        Profiles: default, no_doc_warnings, no_test_warnings, strictness_medium, strictness_high, strictness_veryhigh, no_member_warnings
      Strictness: None
  Libraries Used: 
       Tools Run: dodgy, mccabe, pydocstyle, profile-validator, pycodestyle, pyflakes, pylint
  Messages Found: 3
 External Config: pylint: /Users/elsonsilva/Workspace/Python/example-python-tools/pyproject.toml
```

- ### pip-audit
pip-audit is a tool to verify packages with known vulnerabilities.

```bash
$ poetry add --dev pip-audit
$ pip-audit
No known vulnerabilities found
```

- ### GNU Make
GNU Make is a tool generally used to automate the generations of executable, but that tool can be used to automate any process. [https://www.gnu.org/software/make/](https://www.gnu.org/software/make/)

Makefile
```Makefile
#Makefile
.PHONY: install format lint test sec

install:
	@poetry install
format:
	@blue .
	@isort .
lint:
	@blue --check .
	@isort --check .
	@prospector
test:
	@python test/first_test.py
	@coverage run --source ./ -m unittest discover -p "*_test.py" && coverage report
sec:
	@pip-audit
```

Usage:

```bash
# To install the project
$ make install

# To format the source code
$ make format

# To verify the format code
$ make lint

# To execute test
$ make test

```
