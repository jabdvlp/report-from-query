from pymysql import *
import openpyxl
import pandas.io.sql as sql
import os
import datetime
from dotenv import load_dotenv
import json

load_dotenv()
USR = os.getenv('USR')
HOST = os.getenv('HOST')
DB = os.getenv('DATABASE')
PASS = os.getenv('PASSWORD')


def reportCreator(query, type_report):
    time = datetime.datetime.now()
    date = time.strftime("%B%d")

    try:
        con = connect(user=USR, password=PASS, host=HOST, database=DB)
        print('Connection Successfull')

        df = sql.read_sql(query, con)
        print('Generating csv File')

        df.to_csv(f'reports/ReporteDocumentos{type_report}{date}.csv', index=False)

    except:
        print('Failed Connection')


