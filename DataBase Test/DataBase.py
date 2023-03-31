# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(
    host=,  # endpoint link
    port=,  # 3306
    user=,  # admin
    password=,  # adminadmin
    db=,  # test

)


# Table Creation
cursor=conn.cursor()
create_table="""
create table Details (name varchar(200),email varchar(200),comment varchar(200),gender varchar(20) )
"""
cursor.execute(create_table)

# insert data
def insert_details(name, email, comment, gender):
    cur = conn.cursor()
    cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name, email, comment, gender))
    conn.commit()

# read data
def get_details():
    cur = conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details