import MySQLdb
import subprocess

connection = MySQLdb.connect(db='desc', user='travis')
cursor = connection.cursor()
cursor.execute('create table ForcedSource if not exists (objectId BIGINT);')
cursor.execute('insert into ForcedSource values (1),(2),(3),(4),(5);')
cursor.close()
connection.commit()

subprocess.call("mysql -e 'select * from ForcedSource'", shell=True)
