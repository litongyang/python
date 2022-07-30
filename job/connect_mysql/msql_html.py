# -*- coding: utf-8 -*-
from flask import Flask
import pymysql
import pandas as pd
app= Flask("mysql 展示")

conn = pymysql.connect(
    host='localhost',
    port=3306,
    password='1234',
    user='root',
    db='test',
    charset='utf8'
)

@app.route("/")
def index():
    sql ="""
        select
        *
        from
        test1
    """
    df = pd.read_sql(sql, con=conn)
    return df.to_html()
app.run()