# csv-parser
[![Build Status](https://travis-ci.org/eduardoperrino/csv-parser.svg?branch=master)](https://travis-ci.org/eduardoperrino/csv-parser)

## Introduction
This project contains an example for a python command-line application which processes a given csv file and insert its rows into a SQLite database. By default, the application uses the in-memory driver for the database to avoid generated files into your machine disk.

## Running script

```
chmod +x parser.py
./parser.py <csv file to parse>
```

## Test script

```
python test.py
```
