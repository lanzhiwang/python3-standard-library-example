.. -*- mode: rst -*-

===========================
 Python Module of the Week
===========================

PyMOTW-3 is a series of articles written by `Doug Hellmann
<http://doughellmann.com/>`_ to demonstrate how to use the modules of
the Python_ 3 standard library. It is based on the original PyMOTW_
series, which covered Python 2.7.

.. _Python: http://www.python.org/
.. _PyMOTW: http://pymotw.com/2/

:Project Home Page: http://pymotw.com/3/
:Issue Tracker and Source: http://www.bitbucket.org/dhellmann/pymotw-3/

Complete documentation for the standard library can be found on the
Python web site at https://docs.python.org/.

Subscribe
=========

As new articles are written, they are posted to `my blog
<http://blog.doughellmann.com/>`_.  Updates are available by `RSS
<http://feeds.feedburner.com/PyMOTW>`_ and `email
<http://www.feedburner.com/fb/a/emailverifySubmit?feedId=806224&amp;loc=en_US>`_.

Copyright and Licensing
=======================

All of the prose from the Python Module of the Week is licensed under
a `Creative Commons Attribution, Non-commercial, Share-alike 3.0
<http://creativecommons.org/licenses/by-nc-sa/3.0/us/>`_ license.  You
are free to share and create derivative works from it.  If you post
the material online, you must give attribution and link to the PyMOTW
home page (http://pymotw.com/).  You may not use this work for
commercial purposes.  If you alter, transform, or build upon this
work, you may distribute the resulting work only under the same or
similar license to this one.

The source code included here is copyright Doug Hellmann and licensed
under the BSD license.

```bash
docker run -ti --rm --name python3-standard-library-example \
-v ~/work/code/py_code/python3-standard-library-example:/python3-standard-library-example \
-w /python3-standard-library-example \
python:3.12.1-bullseye \
bash

docker run -ti --rm --name python3-standard-library-example \
-v ~/work/code/py_code/python3-standard-library-example:/python3-standard-library-example \
-w /python3-standard-library-example \
python:3.10-bullseye \
bash

pip install "black[jupyter]" mypy

find . -name "*.py" -exec black {} \;

find . -name "*.ipynb" -exec black {} \;

find . -name __pycache__ -exec rm -rf {} \;

```
