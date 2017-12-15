=================
BIGG DB Converter
=================

Thi script takes a Bigg DB json dump as an input and outputs a tab separated file (the input of the `insert_features` management command.

------
Usage:
------
Use Python 3 in virtual environment, install with :code:`pip install -r requirement.txt`.

Run :code:`python BIGG_converter.py "<species>" <input file path> <output file path>`.

Note: the script supports :code:`.gz` as output format, it guesses the proper output format based on the provided file path.
