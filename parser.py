import sys
import csv
import logging
import sqlite3
import os
import datetime
import calendar
from sys import exit
from collections import namedtuple

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')


FinalReport = namedtuple('FinalReport', 'processed_rows inserted_rows error')


def build_table_name():
    now = datetime.datetime.now()
    tt = datetime.datetime.timetuple(now)
    table_name = "t_%s" % (calendar.timegm(tt) * 1000)
    return table_name


def parse(file):
    if not os.path.isfile(file):
        return FinalReport(processed_rows=0, inserted_rows=0,
            error="No such file `%s`" % file)
    with open(file) as csv_file:
        con = sqlite3.connect(":memory:")
        con.text_factory = lambda x: unicode(x, "utf-8", "ignore")
        cur = con.cursor()
        dialect = csv.Sniffer().sniff(csv_file.read(30))
        csv_file.seek(0)
        csv_reader = csv.reader(csv_file, delimiter=dialect.delimiter)
        headers = next(csv_reader, None)
        table_name = build_table_name()
        creational_statement = "CREATE TABLE %s (%s);" % (table_name, ','.join(headers))
        try:
            cur.execute(creational_statement)
        except Exception as err:
            return FinalReport(processed_rows=0, inserted_rows=0,
                error="Error creating DB table `%s`" % err)
        data = []
        processed_rows = 0
        for row in csv_reader:
            if len(row) == len(headers):
                data.append(row)
            processed_rows += 1
        insert_statement = "INSERT INTO " + table_name + " VALUES (" + ','.join(['?'] * len(headers)) + ");"
        try:
            cur.executemany(insert_statement, data)
        except Exception as err:
            return FinalReport(processed_rows=processed_rows, inserted_rows=0,
                error="Error storing data into DB `%s`" % err)
        con.commit()
        con.close()
        return FinalReport(processed_rows=processed_rows,
            inserted_rows=len(data), error=None)


def print_report(final_report):
    print "*******************OUTPUT RESULTS**********************************"
    if final_report.error:
        print "*** Upsss!!! Error processing file"
        print "*** Cause: %s" % final_report.error
    print "*** Rows processed %s" % final_report.processed_rows
    print "*** Rows Stored %s" % final_report.inserted_rows
    print "*******************************************************************"


def run_parser(args):
    if len(args) == 1:
        exit("=== You must indicate a csv to be parsed :-)")
    print_report(parse(args[1]))


if __name__ == '__main__':
    run_parser(sys.argv)
