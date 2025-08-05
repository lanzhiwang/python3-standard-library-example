# python 默认包管理工具 pip 和虚拟环境 venv

```bash
$ python -m venv .venv
$
$ ls -al
total 4
drwxr-xr-x   4 root root  128 Aug  5 08:13 .
drwxr-xr-x 127 root root 4064 Aug  5 08:11 ..
drwxr-xr-x   7 root root  224 Aug  5 08:13 .venv
-rw-r--r--   1 root root   40 Aug  5 08:11 README.md
$
$ source .venv/bin/activate
(.venv) $ pip freeze
(.venv) $
(.venv) $ deactivate
$

```

# pipenv

```bash
$ cd demo/
$ pwd
/python3-standard-library-example/source/40_pipenv/demo
$ ls -al
total 0
drwxr-xr-x 2 root root  64 Aug  5 08:16 .
drwxr-xr-x 4 root root 128 Aug  5 08:16 ..
$
$ pip install pipenv

# 进去虚拟环境
# 如果当前目录还没有虚拟环境，那么 pipenv shell 就会自动帮我们创建一个虚拟环境
$ pipenv shell
Creating a virtualenv for this project
Pipfile: /python3-standard-library-example/source/40_pipenv/demo/Pipfile
Using /usr/local/bin/python3.10.18 to create virtualenv...
⠋ Creating virtual environment...created virtual environment CPython3.10.18.final.0-64 in 713ms
  creator CPython3Posix(dest=/root/.local/share/virtualenvs/demo-QzF8r-Bm, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)
    added seed packages: pip==25.1.1, setuptools==80.9.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /root/.local/share/virtualenvs/demo-QzF8r-Bm
Creating a Pipfile for this project...
Launching subshell in virtual environment...
$  source /root/.local/share/virtualenvs/demo-QzF8r-Bm/bin/activate
(demo) $
(demo) $ ls -al
total 4
drwxr-xr-x 3 root root  96 Aug  5 08:20 .
drwxr-xr-x 4 root root 128 Aug  5 08:16 ..
-rw-r--r-- 1 root root 139 Aug  5 08:20 Pipfile
(demo) $
(demo) $

# 不一定要在虚拟环境中执行 pipenv install
# 只有当前目录有 Pipfile 文件，pipenv 就知道要操作那个虚拟环境
(demo) $ pipenv install flask
Pipfile.lock not found, creating...
Locking  dependencies...
Locking  dependencies...
Updated Pipfile.lock (fedbd2ab7afd84cf16f128af0619749267b62277b4cb6989ef16d4bef6e4eef2)!
Installing flask...
✔ Installation Succeeded
Installing dependencies from Pipfile.lock (e4eef2)...
All dependencies are now up-to-date!
Upgrading flask in  dependencies.
Building requirements...
Resolving dependencies...
✔ Success!
Installing dependencies from Pipfile.lock (81f117)...
All dependencies are now up-to-date!
Installing dependencies from Pipfile.lock (81f117)...
(demo) $ pipenv graph
Flask==3.1.1
├── blinker
├── click
├── itsdangerous
├── Jinja2
│   └── MarkupSafe
├── MarkupSafe
└── Werkzeug
    └── MarkupSafe
(demo) $ ls -al
total 16
drwxr-xr-x 4 root root  128 Aug  5 08:25 .
drwxr-xr-x 4 root root  128 Aug  5 08:16 ..
-rw-r--r-- 1 root root  151 Aug  5 08:25 Pipfile
-rw-r--r-- 1 root root 8206 Aug  5 08:25 Pipfile.lock
(demo) $

(demo) $ pipenv install black --dev
Installing black...
✔ Installation Succeeded
Installing dependencies from Pipfile.lock (81f117)...
All dependencies are now up-to-date!
Upgrading black in  dependencies.
Building requirements...
Resolving dependencies...
✔ Success!
Installing dependencies from Pipfile.lock (c80ffb)...
All dependencies are now up-to-date!
Installing dependencies from Pipfile.lock (c80ffb)...
Installing dependencies from Pipfile.lock (c80ffb)...
(demo) $
(demo) $ pipenv graph
black==25.1.0
├── click
├── mypy_extensions
├── packaging
├── pathspec
├── platformdirs
├── tomli
└── typing_extensions
Flask==3.1.1
├── blinker
├── click
├── itsdangerous
├── Jinja2
│   └── MarkupSafe
├── MarkupSafe
└── Werkzeug
    └── MarkupSafe
(demo) $

(demo) $ pipenv -h
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.
  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.
  --clear                         Clears caches (pipenv, pip).
  -q, --quiet                     Quiet mode.
  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check         Checks for PyUp Safety security vulnerabilities and against
                PEP 508 markers provided in Pipfile.
  clean         Uninstalls all packages not specified in Pipfile.lock.
  graph         Displays currently-installed dependency graph information.
  install       Installs provided packages and adds them to Pipfile, or (if no
                packages are given), installs all packages from Pipfile.
  lock          Generates Pipfile.lock.
  open          View a given module in your editor.
  requirements  Generate a requirements.txt from Pipfile.lock.
  run           Spawns a command installed into the virtualenv.
  scripts       Lists scripts in current environment config.
  shell         Spawns a shell within the virtualenv.
  sync          Installs all packages specified in Pipfile.lock.
  uninstall     Uninstalls a provided package and removes it from Pipfile.
  update        Runs lock, then sync.
  upgrade       Resolves provided packages and adds them to Pipfile, or (if no
                packages are given), merges results to Pipfile.lock
  verify        Verify the hash in Pipfile.lock is up-to-date.
(demo) $

```

