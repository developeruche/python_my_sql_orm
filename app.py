import mysql.connector
connobj = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'myfirstdatabase'
}

# Application util functions


def createIntField(*args, **kwargs):
    _null = 'NULL'
    _default = ''
    # Getting the users parameters
    # Available paramemter (field_name, field_type, _default, _null)
    ''' This is the available inputable field type for int
        small_int,
        mid_int,
        and big_int
    '''
    """ 
    This is how the integerfield id expecting an input
    fields = {
        'integer_field' : ['record_name', null = value(either True or False), default]
    }
    """
    # Validation: Field Name
    if 'field_name' in kwargs.keys():
        if len(kwargs['field_name']) <= 64:
            # first cheaking if the lenght of the string is more that 64bits
            if kwargs['field_name'] != "":
                field_name = str(kwargs['field_name'])
                field_name = field_name.strip().lower().replace('/', '').replace('.', '')
            else:
                return print('ERROR: Invaild input --- an empty string is not accepted')
        else:
            return print('ERROR: Lenght of field name must be less that 64bits')
    else:
        return print("ERROR: The name of the field is not inputed to this \n field_name='theinergername' ")

    # Validation: Field Type
    if 'field_type' in kwargs.keys():
        field_type_working = kwargs['field_type']
        if field_type_working == 'small_int':
            field_type = 'SMALLINT'
        elif field_type_working == 'mid_int':
            field_type = 'INT'
        elif field_type_working == 'big_int':
            field_type = 'BIGINT'
        else:
            field_type = 'INT'
    else:
        return print('error: Field type in emitted. ')

    # Validation: Null
    if '_null' in kwargs.keys() == True or kwargs['_null'] == False:
        if kwargs['_null'] == True:
            _null = 'NULL'
        elif kwargs['_null'] == False:
            _null = 'NOT NULL'
        else:
            return print('ERROR: The field _null recieved an invaild paramenter datatype.')
    else:
        print('WARNING: the parameter _null is not specified, it would be assigned a default of True')

    # Validation: Default
    if '_default' in kwargs.keys():
        if str(kwargs['_default']).isdigit():
            _default = kwargs['_default']
            _default = f"DEFAULT {_default}"
        else:
            return print('ERROR: default for an interger field must all be intergers')

    if field_type == 'SMALLINT':
        return (
            f"""
                {field_name} SMALLINT(5) {_null} {_default},
            """
        )
    elif field_type == 'INT':
        return (
            f"""
                {field_name} INT(50) {_null} {_default},
            """
        )
    elif field_type == 'BIGINT':
        return (
            f"""
                {field_name} BIGINT(5000) {_null} {_default},
            """
        )
    else:
        return (
            f"""
               An error occured during compilation 
            """
        )


def createTextField(*args, **kwargs):
    _null = 'NULL'
    _default = ''
    # Getting the users parameters
    # Available paramemter (field_name, field_type, _default, _null)
    ''' This is the available inputable field type for int
        varchar,
        mid_text,
        and large_text
    '''
    """ 
    This is how the integerfield id expecting an input
    fields = {
        'text_field' : ['record_name', nullvalue(either True or False), default, 'mid_text']
    }
    """
    # Validation: Field Name
    if 'field_name' in kwargs.keys():
        if len(kwargs['field_name']) <= 64:
            # first cheaking if the lenght of the string is more that 64bits
            if kwargs['field_name'] != "":
                field_name = str(kwargs['field_name'])
                field_name = field_name.strip().lower().replace('/', '').replace('.', '')
            else:
                return print('ERROR: Invaild input --- an empty string is not accepted')
        else:
            return print('ERROR: Lenght of field name must be less than 64bits')
    else:
        return print("ERROR: The name of the field is not inputed, do this \n field_name='thetextname' ")

    # Validation: Field Type
    if 'field_type' in kwargs.keys():
        field_type_working = kwargs['field_type']
        if field_type_working == 'varchar':
            field_type = 'VARCHAR'
        elif field_type_working == 'mid_text':
            field_type = 'TEXT'
        elif field_type_working == 'large_text':
            field_type = 'TEXT'
        else:
            field_type = 'VARCHAR'
    else:
        return print('error: Field type in emitted. ')

    # Validation: Null
    if '_null' in kwargs.keys() == True or kwargs['_null'] == False:
        if kwargs['_null'] == True:
            _null = 'NULL'
        elif kwargs['_null'] == False:
            _null = 'NOT NULL'
        else:
            return print('ERROR: The field _null recieved an invaild paramenter datatype.')
    else:
        print('WARNING: the parameter _null is not specified, it would be assigned a default of True')

    # Validation: Default
    if '_default' in kwargs.keys():
        if str(kwargs['_default']) != "":
            _default = kwargs['_default']
            _default = ""
        else:
            return print('ERROR: default for an Text field must not be an empty string.')

    if field_type == 'VARCHAR':
        return (
            f"""
                {field_name} VARCHAR(100) {_null} {_default},
            """
        )
    elif field_type == 'TEXT':
        return (
            f"""
                {field_name} TEXT(6000) {_null} {_default},
            """
        )
    else:
        return (
            f"""
               An error occured during compilation 
            """
        )


def createFloatField(*args, **kwargs):
    _null = 'NULL'
    _default = ''
    # Getting the users parameters
    # Available paramemter (field_name, field_type, _default, _null)
    ''' This is the available inputable field type for int
        float,
        decimal,
    '''
    """ 
    This is how the integerfield id expecting an input
    fields = {
        'float_field' : ['record_name', nullvalue(either True or False), default]
    }
    """
    # Validation: Field Name
    if 'field_name' in kwargs.keys():
        if len(kwargs['field_name']) <= 64:
            # first cheaking if the lenght of the string is more that 64bits
            if kwargs['field_name'] != "":
                field_name = str(kwargs['field_name'])
                field_name = field_name.strip().lower().replace('/', '').replace('.', '')
            else:
                return print('ERROR: Invaild input --- an empty string is not accepted')
        else:
            return print('ERROR: Lenght of field name must be less that 64bits')
    else:
        return print("ERROR: The name of the field is not inputed to this \n field_name='theinergername' ")

    # Validation: Field Type
    if 'field_type' in kwargs.keys():
        field_type_working = kwargs['field_type']
        if field_type_working == 'float':
            field_type = 'FLOAT'
        elif field_type_working == 'decimal':
            field_type = 'DOUBLE'
        else:
            field_type = 'FLOAT'
    else:
        return print('error: Field type in emitted. ')

    # Validation: Null
    if '_null' in kwargs.keys() == True or kwargs['_null'] == False:
        if kwargs['_null'] == True:
            _null = 'NULL'
        elif kwargs['_null'] == False:
            _null = 'NOT NULL'
        else:
            return print('ERROR: The field _null recieved an invaild paramenter datatype.')
    else:
        print('WARNING: the parameter _null is not specified, it would be assigned a default of True')

    # Validation: Default
    if '_default' in kwargs.keys():
        if str(kwargs['_default']) != "":
            _default = kwargs['_default']
            _default = f"DEFAULT {_default}"
        else:
            return print('ERROR: default for an Float field must not be an empty string.')

    if field_type == 'FLOAT':
        return (
            f"""
                {field_name} FLOAT(5) {_null} {_default},
            """
        )
    elif field_type == 'DOUBLE':
        return (
            f"""
                {field_name} DOUBLE(5) {_null} {_default},
            """
        )
    else:
        return (
            f"""
               An error occured during compilation 
            """
        )


def createDateField(*args, **kwargs):
    _null = 'NULL'
    _default = ''
    # Getting the users parameters
    # Available paramemter (field_name, field_type, _default, _null)
    ''' This is the available inputable field type for int
        date,
    '''
    """ 
    This is how the date is expecting an input
    fields = {
        'integer_field' : ['record_name', nullvalue(either True or False), default]
    }
    """
    # Validation: Field Name
    if 'field_name' in kwargs.keys():
        if len(kwargs['field_name']) <= 64:
            # first cheaking if the lenght of the string is more that 64bits
            if kwargs['field_name'] != "":
                field_name = str(kwargs['field_name'])
                field_name = field_name.strip().lower().replace('/', '').replace('.', '')
            else:
                return print('ERROR: Invaild input --- an empty string is not accepted')
        else:
            return print('ERROR: Lenght of field name must be less that 64bits')
    else:
        return print("ERROR: The name of the field is not inputed to this \n field_name='theinergername' ")

    # Validation: Field Type
    if 'field_type' in kwargs.keys():
        field_type_working = kwargs['field_type']
        if field_type_working == 'date':
            field_type = 'DATE'
        else:
            field_type = 'DATE'
    else:
        return print('error: Field type in emitted. ')

    # Validation: Null
    if '_null' in kwargs.keys() == True or kwargs['_null'] == False:
        if kwargs['_null'] == True:
            _null = 'NULL'
        elif kwargs['_null'] == False:
            _null = 'NOT NULL'
        else:
            return print('ERROR: The field _null recieved an invaild paramenter datatype.')
    else:
        print('WARNING: the parameter _null is not specified, it would be assigned a default of True')

    # Validation: Default
    if '_default' in kwargs.keys():
        if str(kwargs['_default']) != "":
            _default = kwargs['_default']
            _default = f"DEFAULT {_default}"
        else:
            return print('ERROR: default for an date field must not be  an empty string.')

    if field_type == 'DATE':
        return (
            f"""
                {field_name} DATE {_null} {_default},
            """
        )
    else:
        return (
            f"""
               An error occured during compilation 
            """
        )


def createDateTimeField(*args, **kwargs):
    _null = 'NULL'
    _default = ''
    # Getting the users parameters
    # Available paramemter (field_name, field_type, _default, _null)
    ''' This is the available inputable field type for int
        datetime,
    '''
    """ 
    This is how the datetime is expecting an input
    fields = {
        'integer_field' : ['record_name', nullvalue(either True or False), default]
    }
    """
    # Validation: Field Name
    if 'field_name' in kwargs.keys():
        if len(kwargs['field_name']) <= 64:
            # first cheaking if the lenght of the string is more that 64bits
            if kwargs['field_name'] != "":
                field_name = str(kwargs['field_name'])
                field_name = field_name.strip().lower().replace('/', '').replace('.', '')
            else:
                return print('ERROR: Invaild input --- an empty string is not accepted')
        else:
            return print('ERROR: Lenght of field name must be less that 64bits')
    else:
        return print("ERROR: The name of the field is not inputed to this \n field_name='theinergername' ")

    # Validation: Field Type
    if 'field_type' in kwargs.keys():
        field_type_working = kwargs['field_type']
        if field_type_working == 'datetime':
            field_type = 'DATETIME'
        else:
            field_type = 'DATETIME'
    else:
        return print('error: Field type in emitted. ')

    # Validation: Null
    if '_null' in kwargs.keys() == True or kwargs['_null'] == False:
        if kwargs['_null'] == True:
            _null = 'NULL'
        elif kwargs['_null'] == False:
            _null = 'NOT NULL'
        else:
            return print('ERROR: The field _null recieved an invaild paramenter datatype.')
    else:
        print('WARNING: the parameter _null is not specified, it would be assigned a default of True')

    # Validation: Default
    if '_default' in kwargs.keys():
        if str(kwargs['_default']) != "":
            _default = kwargs['_default']
            _default = f"DEFAULT {_default}"
        else:
            return print('ERROR: default for an DateTime field must not be an empty string.')

    if field_type == 'DATETIME':
        return (
            f"""
                {field_name} DATETIME {_null} {_default},
            """
        )
    else:
        return (
            f"""
               An error occured during compilation 
            """
        )


def createTimestampField(*args, **kwargs):
    _null = 'NULL'
    _default = ''
    # Getting the users parameters
    # Available paramemter (field_name, field_type, _default, _null)
    ''' This is the available inputable field type for int
        timestamp,
    '''
    """ 
    This is how the integerfield id expecting an input
    fields = {
        'integer_field' : ['record_name', nullvalue(either True or False), default]
    }
    """
    # Validation: Field Name
    if 'field_name' in kwargs.keys():
        if len(kwargs['field_name']) <= 64:
            # first cheaking if the lenght of the string is more that 64bits
            if kwargs['field_name'] != "":
                field_name = str(kwargs['field_name'])
                field_name = field_name.strip().lower().replace('/', '').replace('.', '')
            else:
                return print('ERROR: Invaild input --- an empty string is not accepted')
        else:
            return print('ERROR: Lenght of field name must be less that 64bits')
    else:
        return print("ERROR: The name of the field is not inputed to this \n field_name='theinergername' ")

    # Validation: Field Type
    if 'field_type' in kwargs.keys():
        field_type_working = kwargs['field_type']
        if field_type_working == 'timestamp':
            field_type = 'TIMESTAMP'
        else:
            field_type = 'TIMESTAMP'
    else:
        return print('error: Field type in emitted. ')

    # Validation: Null
    if '_null' in kwargs.keys() == True or kwargs['_null'] == False:
        if kwargs['_null'] == True:
            _null = 'NULL'
        elif kwargs['_null'] == False:
            _null = 'NOT NULL'
        else:
            return print('ERROR: The field _null recieved an invaild paramenter datatype.')
    else:
        print('WARNING: the parameter _null is not specified, it would be assigned a default of True')

    # Validation: Default
    if '_default' in kwargs.keys():
        if str(kwargs['_default']) != "":
            _default = kwargs['_default']
            _default = f"DEFAULT {_default}"
        else:
            return print('ERROR: default for an interger field must all be intergers')
    else:
        _default = f"DEFAULT CURRENT_TIMESTAMP"

    if field_type == 'TIMESTAMP':
        return (
            f"""
                {field_name} TIMESTAMP {_null} {_default},
            """
        )
    else:
        return (
            f"""
               An error occured during compilation 
            """
        )


def createTimeField(*args, **kwargs):
    _null = 'NULL'
    _default = ''
    # Getting the users parameters
    # Available paramemter (field_name, field_type, _default, _null)
    ''' This is the available inputable field type for int
        time,
    '''
    """ 
    This is how the integerfield id expecting an input
    fields = {
        'integer_field' : ['record_name', nullvalue(either True or False), default]
    }
    """
    # Validation: Field Name
    if 'field_name' in kwargs.keys():
        if len(kwargs['field_name']) <= 64:
            # first cheaking if the lenght of the string is more that 64bits
            if kwargs['field_name'] != "":
                field_name = str(kwargs['field_name'])
                field_name = field_name.strip().lower().replace('/', '').replace('.', '')
            else:
                return print('ERROR: Invaild input --- an empty string is not accepted')
        else:
            return print('ERROR: Lenght of field name must be less that 64bits')
    else:
        return print("ERROR: The name of the field is not inputed to this \n field_name='theinergername' ")

    # Validation: Field Type
    if 'field_type' in kwargs.keys():
        field_type_working = kwargs['field_type']
        if field_type_working == 'time':
            field_type = 'TIME'
        else:
            field_type = 'TIME'
    else:
        return print('error: Field type in emitted. ')

    # Validation: Null
    if '_null' in kwargs.keys() == True or kwargs['_null'] == False:
        if kwargs['_null'] == True:
            _null = 'NULL'
        elif kwargs['_null'] == False:
            _null = 'NOT NULL'
        else:
            return print('ERROR: The field _null recieved an invaild paramenter datatype.')
    else:
        print('WARNING: the parameter _null is not specified, it would be assigned a default of True')

    # Validation: Default
    if '_default' in kwargs.keys():
        if str(kwargs['_default']) != "":
            _default = kwargs['_default']
            _default = f"DEFAULT {_default}"
        else:
            return print('ERROR: default for an interger field must all be intergers')

    if field_type == 'TIME':
        return (
            f"""
                {field_name} TIME {_null} {_default},
            """
        )
    else:
        return (
            f"""
               An error occured during compilation 
            """
        )


def formatDBTable(kw, v):
    """ 
    total_fields = [
        'integer_field', 'text_field', 'float_field',  'date_field', 'datetime_field'
        'timestamp_field', 'time_field'
    ]
    This is how the integerfield id expecting an input
    fields = {
        'integer_field' : ['record_name', null = value(either True or False), default, record_type]
    }
    """
    execList = []
    index = 0
    for x in kw:
        if x == 'integer_field':
            # Then we create an interger field
            if v[index][2] == 'no_default':
                exec_q = createIntField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1])
                execList.append(exec_q)
            else:
                exec_q = createIntField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1], _default=v[index][2])
                execList.append(exec_q)

        elif x == 'text_field':
            # Then we create a text felid with eh defined function
            if v[index][2] == 'no_default':
                exec_q = createTextField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1])
                execList.append(exec_q)
            else:
                exec_q = createTextField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1], _default=v[index][2])
                execList.append(exec_q)

        elif x == 'float_field':
            # Then we create a text felid with eh defined function
            if v[index][2] == 'no_default':
                exec_q = createFloatField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1])
                execList.append(exec_q)
            else:
                exec_q = createFloatField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1], _default=v[index][2])
                execList.append(exec_q)

        elif x == 'date_field':
            # Then we create a text felid with eh defined function
            if v[index][2] == 'no_default':
                exec_q = createDateField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1])
                execList.append(exec_q)
            else:
                exec_q = createDateField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1], _default=v[index][2])
                execList.append(exec_q)

        elif x == 'datetime_field':
            # Then we create a text felid with eh defined function
            if v[index][2] == 'no_default':
                exec_q = createDateTimeField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1])
                execList.append(exec_q)
            else:
                exec_q = createDateTimeField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1], _default=v[index][2])
                execList.append(exec_q)

        elif x == 'timestamp_field':
            # Then we create a text felid with eh defined function
            if v[index][2] == 'no_default':
                exec_q = createTimestampField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1])
                execList.append(exec_q)
            else:
                exec_q = createTimestampField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1], _default=v[index][2])
                execList.append(exec_q)

        elif x == 'time_field':
            # Then we create a text felid with eh defined function
            if v[index][2] == 'no_default':
                exec_q = createTimeField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1])
                execList.append(exec_q)
            else:
                exec_q = createTimeField(
                    field_name=v[index][0], field_type=v[index][-1], _null=v[index][1], _default=v[index][2])
                execList.append(exec_q)
        else:
            return print('ERROR: An error occured while try to excute the create table command.')

        index += 1
    return execList


class Database:
    def __init__(self, *args, **kwargs):
        # When this class is init connection is first created
        if 'connection_object' in kwargs.keys():
            self.connection_obj = kwargs['connection_object']
            # Beginning connection process
            self.conn = mysql.connector.connect(
                host=self.connection_obj['host'],
                port=self.connection_obj['port'],
                user=self.connection_obj['user'],
                password=self.connection_obj['password'],
                database=self.connection_obj['database']
            )
            # Creating the coursor( this  the most important tool as it would be the tool passing our insturtions to the db directly)
            self.cursor = self.conn.cursor()
        else:
            return print('ERROR: Print Database connection FAILED.')

        # Defining a method which would create db table
    def createDBTable(self, *args, **kwargs):
        # Obtaining the fields input from the uses and try to make some classifications
        ''' 
        This how is plan on calling the createDBTable
        mydb = Datebase(db_table_name='customers', db_fields=field_dictonary)
        mydb.createDBTable()
        '''
        if 'db_fields' in kwargs.keys() and 'db_table_name' in kwargs.keys():
            if 'db_fields' in kwargs.keys():
                database_fields = kwargs['db_fields']
                # This would return a dict...
            else:
                return print('VALUE_ERROR: The fieldname should not be an empty field')
            if kwargs['db_table_name'] != "":
                db_table_name = kwargs['db_table_name']
            else:
                return print('VALUE_ERROR: The fieldname should not be an empty field')
        else:
            return print('PARAMETER ERROR: The field database_fields or db_table_name is missing.')
        # getting and array of the keys of the dictionary,
        # the dictionanry would come in this way
        """
        db_fields = {
            'text_field' : ['customer-name', True, 'defualt value', 'TEXT'],
            'date_field' : ['date-of-ordering', True, 'defualt value'],
            'integer_field' ['----------------'],
            'float_field' : ['----------------']
            and soon
        }
        fields = {
        'integer_field' : ['record_name', null = value(either True or False), default, record_type]
        }
        """
        # Validating the input to see if the fields the user input is part of our avilable fields
        total_fields = [
            'integer_field', 'text_field', 'float_field',  'date_field', 'datetime_field', 'timestamp_field', 'time_field'
        ]
        database_fields_keys = [i for i in database_fields.keys()]
        # Now also retriving the values for it is necceary also
        database_fields_values = [i for i in database_fields.values()]
        count = 0
        for field in database_fields_keys:
            database_fields_keys_len = len(database_fields_keys)
            if field in total_fields:
                pass
            else:
                count += 1
        # Incase you dont understand, here if the use input a field
        # not part of the avaliable field the count would be greater than 0
        # so we can make use of that for our validation comparism
        # Stringfigying the list making it something like this ['key1', 'key2']
        if count > 0:
            return print('ERROR: The field input does not match any database field.')
        else:
            pass

        database_fields_keys_stringified = list(database_fields.keys())

        ''' 
            The concept here how id in this system work is that
            at creation a random interger value ia assigned and 
            the db is then set to auto increment the id on insection of values
        '''
        records_list = formatDBTable(
            database_fields_keys_stringified, database_fields_values)

        records_list_stringified = " ".join(records_list)
        print(records_list_stringified)
        tableid = createIntField(
            field_name='id', field_type='mid_int', _null=False)

        tableid = tableid.replace(',', "")
        tableid = tableid + 'AUTO_INCREMENT ,'

        self.cursor.execute(f"""CREATE TABLE {db_table_name}
        (
        {tableid}
        {records_list_stringified}
        PRIMARY KEY (id)
        )
        """)
        # In other to save the change you made it has to be commited
        self.conn.commit()
        # In other to reduce waste computation the connection is closed after early commiunication
        self.conn.close()

    def InsertRecord(self, *args, **kwargs):
        ''' 
        This function would be accessed this way after intanciating the class
        db.InsertRecord(table_name="", fields={
            'first_name' : 'Uche',
            'second_name' : 'David',
            'course' : 'computer_eng',
            'others' : 'Others'
        })
        '''
        # Retriving the table name
        if 'table_name' in kwargs.keys():
            if kwargs['table_name'] != "":
                table_name = kwargs['table_name']
            else:
                return print('ERROR: Table name cannot be an empty string.')
        else:
            return print("ERROR: The field 'table_name' is required.")

        # Retriving the record_names and their values from the kwargs parameter
        if 'fields' in kwargs.keys():
            record_names = [i for i in kwargs['fields'].keys()]
            record_values = [i for i in kwargs['fields'].values()]
        else:
            return print('ERROR: The dictonary of the fields are required.')
        record_names_stringified = ', '.join(record_names)

        # Here is where the action is been carried out
        # self.cursor.execute("INSERT INTO names (id, name) VALUES(1, 'Uchenna');")
        # I am not sure this would work (i guess the excute function is expecting a raw string)
        ''' 
        Trying to develop an algorithm that would return the raw string of the recod values dinamically
        by first convert each string in the list to a raw string using the for loop
        '''
        raw_string_list = []
        for x in record_values:
            raw_string_list.append(f"'{x}'")

        # Here the raw string value is obtained to meet SQL engines requirement now it can be stringified and returned
        record_values_stringified = ', '.join(raw_string_list)
        self.cursor.execute(
            f"INSERT INTO {table_name} (id, {record_names_stringified}) VALUES(DEFAULT, {record_values_stringified});")
        # Here a commit is been made to make sure the change is implemented in the database
        self.conn.commit()
        # Here the connection is close to reduce waste of computation
        self.conn.close()

    def queryAll(self, *args, **kwargs):
        ''' 
        This function is more like the object.all() in the django orm
        the keyword parameter we are expecting are
        table_name = String
        '''
        # Extracting the table_name from the **kwargs parameter and validating it to
        try:
            table_name = kwargs['table_name']
        except Exception as e:
            print(e)
            return print('ERROR: The parameter table_name cannot be access, it is either invalid or it is not stated... paramenter must be a valid string data type.')

        # Validation (if it is an empty string)
        if table_name == "":
            return print('ERROR: The parameter table_name cannot be an empty string.')
        else:
            pass
        # performing the selection query string (This is the string our cursor would be sending to the SQL engine)
        q = f"SELECT * FROM {table_name}"

        # Now excuting the query
        self.cursor.execute(q)
        records = self.cursor.fetchall()

        # Returning the results
        print(
            f'number of records count in this query is {self.cursor.rowcount}')

        return records

        # Closing the cursor to prevent complications in the next query
        self.cursor.close()
        # Here the connection is close to reduce waste of computation
        self.conn.close()

    def querySingleRow(self, *args, **kwargs):
        ''' 
            In a row would be fetched from the database
            the parameter we are expecting is the 1. table_name 2. record_name
        '''
        # Extracting the parameter table_name and record_name fron the kwargs parameter
        try:
            table_name = kwargs['table_name']
            record_name = kwargs['record_name']
        except Exception as e:
            print(e)
            return print('ERROR: Incompelete keyword parameter, either table_name or record_name is invaild')

        # Validation (if it is an empty string)
        if table_name == "":
            return print('ERROR: The parameter table_name cannot be an empty string.')
        else:
            pass
        if record_name == "":
            return print('ERROR: The parameter record_name must not be an empty string.')
        else:
            pass

        # Creating the query string which would be sent to the SQL engine be the cursor
        q = f"SELECT {record_name} FROM {table_name}"

        # Now excuting the query
        self.cursor.execute(q)
        records = self.cursor.fetchall()

        return records

        # Closing the cursor to prevent complications in the next query
        self.cursor.close()
        # Here the connection is close to reduce waste of computation
        self.conn.close()

    def QueryRecordsByKeyword(self, *args, **kwargs):
        ''' 
        This Function is expecting the table name and the record name and the record value
        '''
        # Extracting the field_name, record_name, and record_value from the kwargs agurment
        try:
            table_name = kwargs['table_name']
            record_name = kwargs['record_name']
            record_value = kwargs['record_value']
        except:
            return print('ERROR: One or more paramenters(table_name, record_name, record_value) is invaild.')

        # Now the parameter if extracted we have to working on it and validate them
        if 'table_name' in kwargs.keys() and 'record_name' in kwargs.keys() and 'record_value' in kwargs.keys():
            # Validate table name
            if kwargs['table_name'] != "":
                pass
            else:
                return print('ERROR: The parameter table_name must not be an empty string.')

            # Validate Record name
            if kwargs['record_name'] != "":
                pass
            else:
                return print('ERROR: The parameter record_name must not be an empty string.')

            # Validate record value
            if kwargs['record_value'] != "":
                pass
            else:
                return print('ERROR: The parameter record_value must not be an empty string.')

        else:
            return print('ERROR: One or more paramenters(table_name, record_name, field_name) is invaild.')

        # Now going into the main  logic
        q = f"SELECT * FROM {table_name} WHERE {record_name}='{record_value}'"

        # Now excuting the query
        self.cursor.execute(q)
        records = self.cursor.fetchall()

        return records

        # Closing the cursor to prevent complications in the next query
        self.cursor.close()
        # Here the connection is close to reduce waste of computation
        self.conn.close()

    def QueryContains(self, *args, **kwargs):
        ''' 
        This function is expecting this parameters.
        1. table_name
        2. record_name
        3. record_value
        '''

        # Extracting the field_name, record_name, and record_value from the kwargs agurment
        try:
            table_name = kwargs['table_name']
            record_name = kwargs['record_name']
            record_value = kwargs['record_value']
        except:
            return print('ERROR: One or more paramenters(table_name, record_name, field_name) is invaild.')

        # Now the parameter if extracted we have to working on it and validate them
        if 'table_name' in kwargs.keys() and 'record_name' in kwargs.keys() and 'record_value' in kwargs.keys():
            # Validate table name
            if kwargs['table_name'] != "":
                pass
            else:
                return print('ERROR: The parameter table_name must not be an empty string.')

            # Validate Record name
            if kwargs['record_name'] != "":
                pass
            else:
                return print('ERROR: The parameter record_name must not be an empty string.')

            # Validate record value
            if kwargs['record_value'] != "":
                pass
            else:
                return print('ERROR: The parameter record_value must not be an empty string.')

        else:
            return print('ERROR: One or more paramenters(table_name, record_name, field_name) is invaild.')

        # Starting the main Logic
        q = f"SELECT * FROM {table_name} WHERE {record_name} LIKE '%{record_value}%'"

        # Now excuting the query
        self.cursor.execute(q)
        records = self.cursor.fetchall()

        return records

        # Closing the cursor to prevent complications in the next query
        self.cursor.close()
        # Here the connection is close to reduce waste of computation
        self.conn.close()

    def RawSQLquery(self, *args, **kwargs):
        ''' 
        The parameter the function is expecting is just the querystring
        '''
        # Extracting the parameter
        if 'query_string' in kwargs.keys():
            query_string = kwargs['query_string']
        else:
            return print('ERROR: The parameter query_string is required.')

        # Now that we have the query string the next this is to execute the function
        self.cursor.execute(query_string)

        records = self.cursor.fetchall()

        return records


# Functions a sytaxs i learnt from building this application
# 1. comparing list
# def ComparingList():
#     x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
#     y = ['a', 'a', 'd', 'b', 'y']
#     count = 0
#     for te in y:
#         y_length = len(y)
#         if te in x:
#             pass
#         else:
#             count += 1
#     print(count)
# testforloop()
# tester = Database(connection_object=connobj)
''' def testing(*args, **kwargs):
    field1 = kwargs['testing_var']
    field1_arr = [i for i in zip(field1.keys())]
    print(field1_arr)


testing_var = {
    'name': 'uche',
    'class': '100lv',
    'first_name': 'david',
    'class2': 'dfghy8',
    'name3': 'uchenna',
    'class3': '100lv2000',
    'classname': 'comenng',
    'classtest': 'test100lv',
    'nametest': 'testuche',
    'classwaw': '100lvwaw',
}

testing(testing_var=testing_var) '''
# # Setting up for querying database
