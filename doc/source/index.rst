.. CurrencyExchangeApp documentation master file, created by
   sphinx-quickstart on Thu Jul  9 10:47:42 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CurrencyExchangeApp's documentation!
===============================================

* Project Info

**CurrencyExchangeApp** is a really simple and useful tool that can be used to compute the **buy amount** given the
**sell and buy currencies** and the **sell amount**. This app is also able to compute expression instead of amounts
entered by the user.

The second functionality is the **Log**. It keeps a track of every operation done by any user which
is displayed in the **logs page**.

* Technology

This is a Django based application (django version 1.4.10). Using django's template system and the default database
engine (sqlite).

* Authors

Ezequiel Rodríguez.

CurrencyApp
-----------

CurrencyApp module is the main application in this Django based project. It contains the **models**, **views**,
**forms**, and **urls** files for the the basic functionality.

.. toctree::
   :maxdepth: 3

   currencyapp/index

Utils
-----

This is a utils package for all the helper functions and classes such as **custom exceptions**, the **math parser**
and so on.

.. toctree::
   :maxdepth: 3

   utils/index

Testing
-------

This project test suite consists of **unit** and **integrations test** as well as few **end to end tests**.

.. toctree::
   :maxdepth: 3

   tests/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
