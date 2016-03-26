import unittest
import MySQLdb

def get_db_info():
    """
    Try to connect to Travis CI MySQL services or the user's via
    ~/.my.cnf and return the connection info.  Otherwise, return
    an empty dict, which should skip the tests.
    """
    db_info = {}
    try:
        try:
            # User's configuration:
            my_db_info = dict(read_default_file='~/.my.cnf')
            test = MySQLdb.connect(**my_db_info)
        except Exception, eobj:
            print eobj
            # Travis CI usage:
            my_db_info = dict(db='myapp_test', user='travis')
            test = MySQLdb.connect(**my_db_info)
        test.close()
        db_info = my_db_info
    except Exception, eobj:
        print eobj
        pass
    return db_info

_db_info = get_db_info()

@unittest.skipUnless(_db_info, "MySQL database not available")
class MySQL_TestCase(unittest.TestCase):
    "Class to test MySQL database access in Travis CI."

    def setUp(self):
        "Create a database connection."
        global _db_info
        self.connection = MySQLdb.connect(**_db_info)
        self.table_name = 'test_table'

    def tearDown(self):
        "Drop the test table and close the connection."
        cursor = self.connection.cursor()
        cursor.execute('drop table if exists %s' % self.table_name)
        cursor.close()
        self.connection.commit()
        self.connection.close()

    def test_create_insert_and_select(self):
        "Test table creation, and row insertion and selection."
        cursor = self.connection.cursor()
        cursor.execute('create table %s (objectId BIGINT)' % self.table_name)
        cursor.execute('insert into %s values (1),(2),(3),(4),(5)'
                       % self.table_name)
        cursor.close()
        self.connection.commit()
        cursor = self.connection.cursor()
        cursor.execute('select * from %s order by objectId asc'
                       % self.table_name)
        results = [x[0] for x in cursor]
        cursor.close()
        self.assertEqual(results, range(1, 6))
