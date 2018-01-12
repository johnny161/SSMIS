from data_layer_connector.create_db.mysql_connector import Connector

table_sql = """
    DROP TABLE IF EXISTS saas_table;
    CREATE TABLE saas_table(
        tableId INTEGER PRIMARY KEY AUTO_INCREMENT,
        tableName VARCHAR(50),
        tenantId INTEGER
    );
"""

field_sql = """
    DROP TABLE IF EXISTS saas_field;
    CREATE TABLE saas_field(
        fieldId INTEGER PRIMARY KEY AUTO_INCREMENT,
        dataType VARCHAR(50),
        fieldName VARCHAR(50),
        tableId INTEGER,
        fieldNum INTEGER,
        tenantId INTEGER,
        isIndexed BOOL
    );
"""

data_sql = """
    DROP TABLE IF EXISTS saas_data;
    CREATE TABLE saas_data(
        Id INTEGER  AUTO_INCREMENT,
        tableId INTEGER,
        tenantId INTEGER,
        naturalName VARCHAR(50),"""

for i in range(51):
    Data_sql += """
        value%d VARCHAR(50),""" % i
Data_sql += """
        PRIMARY KEY(Id)
    );"""



def create_saas_db():
    conn = Connector()
    conn.connect()

    conn.execute(Table_sql)
    conn.execute(Field_sql)
    conn.execute(Data_sql)

    conn.close()

#create_saas_db()