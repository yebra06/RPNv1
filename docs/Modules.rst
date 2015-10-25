RPNv1 Modules
#############

..  include::   /references.inc

This is a small project divided into 3 modules.

* ``main.py`` - This is just the driver for the ``rpn.py`` module. It defines a dict of arithmetic operations
   to be done on values read from a file.
* ``rpn.py`` - This module processes tokens in the file and determines if the token is an operand or operator.
   It operates the values from the file to produce a final result.
