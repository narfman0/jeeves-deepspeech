jasper-deepspeech
=================

WIP

.. image:: https://badge.fury.io/py/jasper-deepspeech.png
    :target: https://badge.fury.io/py/jasper-deepspeech

.. image:: https://travis-ci.org/narfman0/jasper-deepspeech.png?branch=master
    :target: https://travis-ci.org/narfman0/jasper-deepspeech

DeepSpeech STT plugin for Jasper

Installation
------------

Install via pip::

    pip install jasper-deepspeech

Development
-----------

Install all the testing requirements::

    pip install -r requirements_test.txt

Run tox to ensure everything works::

    make test

You may also invoke `tox` directly if you wish.

Release
-------

To publish your plugin to pypi, sdist and wheels are (registered,) created and uploaded with::

    make release

License
-------

Copyright (c) 2018 Jon Robison

See LICENSE for details
