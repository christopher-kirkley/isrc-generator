# isrc-generator

Generate ISRCs from the command line.

# Why?


# Usage

python isrc.py


# How it works

Default settings are stored in a JSON file. The only default settings currently saved are isrc issuer and country code, as these are unlikely to change after initial use.

Output is generated both as stdout as well as a CSV.

# Specifications

CSV is created using the pandas library
Tests are compiled with pytest


