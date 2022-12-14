# Learning Python

## Prepare pyenv

```sh
PYTHON_VERSION="3.10.5"

brew install pyenv
pyenv install $PYTHON_VERSION
pyenv global $PYTHON_VERSION
```

Open your `.zshrc` file and add the lines below at the end of the file.

```sh
code ~/.zshrc
```

**or**, use `vi`

```sh
vi ~/.zshrc
```

Copy and paste the following lines:

```
# Python - pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

You should now close your terminal `exit` and re-open it.

Check python and pip

```sh
which python
which pip
```

## Some Utilities of pyenv

List of existing version installed on your mac:
```sh
pyenv versions
```

Set a new version of python on your mac:
```sh
pyenv global $PYTHON_VERSION
```

## Your First Python Program

Create a new file

```sh
code hello.py
```

Edit your file with visual studio and write this line:

```py
print("Hello World")
```

Run the script **hello.py** in your terminal

```sh
python hello.py
```
## Running 
![Screenshot](https://github.com/julioaranajr/01_Python_PyEnv_App/blob/main/hello-world-py.png)
