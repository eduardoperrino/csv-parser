# csv-parser
[![Build Status](https://travis-ci.org/eduardoperrino/csv-parser.svg?branch=master)](https://travis-ci.org/eduardoperrino/csv-parser)

## Introduction
This project contains an example for a python command-line application which processes a given csv file and insert its rows into a SQLite database. By default, the application uses the in-memory driver for the database to avoid generated files into your machine disk.

## Prerquisites
* [Pip](https://pypi.org/project/pip/) installed

## Build application
```
chmod +x build.sh
./build.sh
```

## Running application

```
./dist/parser users_data.txt
```

## Test application

```
python test.py
```
