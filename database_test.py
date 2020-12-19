import importlib

app = importlib.import_module('app')

# importing module
Database = app.Database

connobj = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'myfirstdatabase'
}
total_fields = [
    'integer_field', 'text_field', 'float_field',  'date_field', 'datetime_field'
    'timestamp_field', 'time_field'
]
tablename = 'customers3'
fields = {
    # 'The fieldtype' : ['rowname', 'Boolean value for null', 'value of defualt || no default', 'specific_fieldtype']
    'integer_field': ['interger_naming', True, 'no_default', 'mid_int'],
    'text_field': ['text_naming', False, 'Testing of the default would work if it was not activated', 'mid_text'],
    'float_field': ['float_naming', True, 'no_default', 'float'],
    'date_field': ['date_naming', False, 'no_default', 'date'],
    'datetime_field': ['datetime_naming', False, 'no_default', 'datetime'],
    'timestamp_field': ['timestamp_naming', False, 'no_default', 'timestamp'],
    'time_field': ['time_naming', False, 'no_default', 'time'],
}
insertfields = {
    'text_naming': 'This is the description of the testing process, help on the insertrecords method. Now test two to make sure the id (the primary key is auto incrementing), Wow Thank God it worked, now let try muitple of of test with this stirng let see if we would encounter any error, you know it would not be well professional for your customer(user) to report a bug during productions stage... we have tested this countless of times now let test it two more times and go on to the next method in the list.',
    'float_naming': 12.3,
    'date_naming': '2020-12-02',
    'datetime_naming': '2020-12-03 13:12:25',
    'time_naming': '10:06:11'
}
''' 
Test for connection done and dusted
====================================
# Intianciating the Database Class and carrying out connections
db = Database(connection_object=connobj)
====================================
'''

''' 
Test for Creating tables done and dusted
====================================
# Testing Createing tables
db.createDBTable(db_table_name=tablename, db_fields=fields)

====================================
'''

''' 
Test for Inseting records done and dusted
====================================
# Testing insert into table
db.InsertRecord(table_name=tablename, fields=insertfields)

====================================
'''

''' 
Test for Querying all records done and dusted
====================================
# Testing Querryall into table
all_records = db.queryAll(table_name='customers2')
print(all_records)
print(all_records[0])
-----------Explanation--------------
The Query all returns all the record(meaning all the rows) from the database table and convert all
neccary convertino from SQL engine manageable variable to Python 3 Variables and method. Take this 
array for instance for a table having two records and 4 rows(id, first_name, last_name, age)
[
    (first_id, first_first_name, first_last_name, first_age),
    (second_id, second_first_name, second_last_name, second_age),
]
when the first index is indexed(all_records[0]) this would return the very first record
same as when indexed as all_records[0] this would return the second record
but when it is indexed as all_records[0][0] this would return the fisrt field('id') of the 
first record.

The key thing note here is the pattern and then you can print to the console your query and figure out a 
how to put those queried data into use.

Hope the doc is helpful.

====================================
'''

''' 
Test for querySingleRow done and dusted
====================================
# Testing querySingleRow method
all_records = db.querySingleRow(
    table_name='customers', record_name='text_naming')
print(all_records)

====================================
'''

''' 
Test for querySingleRow done and dusted
====================================
# Testing QueryRecordsByKeyword method
f = db.QueryRecordsByKeyword(
    table_name='customers', record_name='id', record_value=3)
print(f[0])


====================================
'''

''' 
Test for QueryContains done and dusted
====================================
# Testing QueryContains
q = db.QueryContains(table_name="customers",
                     record_name="text_naming", record_value="muitple")
print(q)


====================================
'''

''' 
Test for RawSQLquery done and dusted
====================================
# Testing RawSQLquery

var = db.RawSQLquery(query_string='SELECT * FROM customers')

print(var)


====================================
'''
