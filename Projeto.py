import psycopg2
import sys
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

ENDPOINT=os.environ.get("ENDPOINT")
PORT=os.environ.get("PORT")
USER=os.environ.get("USER")
TOKEN=os.environ.get("TOKEN")
REGION=os.environ.get("REGION")
DBNAME=os.environ.get("DBNAME")

print(ENDPOINT)

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds')

try:
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USER, password=TOKEN, sslrootcert="SSLCERTIFICATE")
    cur = conn.cursor()
    #cur.execute("""INSERT INTO dummy_table values (2, 'TESTE_2', 'TESTE')""")
    cur.execute("""SELECT * from dummy_table""")
    query_results = cur.fetchall()
    print(query_results)

    conn.commit()
except Exception as e:
    print("Database connection failed due to {}".format(e))     
    if conn:
        conn.rollback()     