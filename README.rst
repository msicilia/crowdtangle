===========
crowdtangle
===========


.. image:: https://img.shields.io/pypi/v/crowdtangle.svg
        :target: https://pypi.python.org/pypi/crowdtangle

.. image:: https://img.shields.io/travis/msicilia/crowdtangle.svg
        :target: https://travis-ci.com/msicilia/crowdtangle

.. image:: https://readthedocs.org/projects/crowdtangle/badge/?version=latest
        :target: https://crowdtangle.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A Facebook CrowdTangle SDK for Python. Under development at this moment, not to be used in production. 


* Free software: MIT license
* Documentation: https://crowdtangle.readthedocs.io.


Quick start
--------

First create a `Client` instance, with a token from a CrowdTangle Dashboard. 

.. code-block:: python

        import crowdtangle as ct
        with open("sample_keys.json", "r") as file:
                creds = json.load(file)
                client = ct.Client(creds['CROWDTANGLE_DASHBOARD_KEY'])


Then use the methods available for each of the endpoints of the API.

.. code-block:: python

        lsts = client.lists(types=['LIST'])
        for lst in lsts:
                for a in client.accounts(lst):
                        print(a.name)


The reference documentation for endpoints, parameters and limitations can be found here:
https://github.com/CrowdTangle/API

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
