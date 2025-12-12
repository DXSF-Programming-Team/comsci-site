HOW TO INSTALL SITE LOCALLY

1. Create a folder that will store the codebase.
2. Open this folder in your IDE of choice. (IDE = integrated development environment; e.g. Visual Studio Code)
3. Open the terminal in your IDE and run the following command:

```bash
git clone https://github.com/DXSF-Programming-Team/parent-app.git
```

This clones the GitHub repository into your current directory.

(If this command fails, it is because you have not installed git yet. Follow the steps here: https://git-scm.com/install/)


Then create a virtual environment:

```bash
python venv -m venv
```

A virtual environment allows you to install the python packages the site needs to run without installing them globally.

(Likewise, if this command fails, it is because you have not installed python yet. Either run the command
```bash
brew install python
```
if you are on macOS, or you can find other installation options here: https://www.python.org/downloads/)


Install the necessary packages:

```bash
pip install -r requirements.txt
```

Then you can run the site locally with the following command:

```bash
flask --app flaskr run --debug
```