from data_layer_connector.create_db.mysql_connector import Connector

Table_sql = """
    DROP TABLE IF EXISTS Saas_Table;
    CREATE TABLE Saas_Table(
        tableId INTEGER PRIMARY KEY AUTO_INCREMENT,
        tableName VARCHAR(50),
        tenantId INTEGER
    );
"""

Field_sql = """
    DROP TABLE IF EXISTS Saas_Field;
    CREATE TABLE Saas_Field(
        fieldId INTEGER PRIMARY KEY AUTO_INCREMENT,
        dataType VARCHAR(50),
        fieldName VARCHAR(50),
        tableId INTEGER,
        fieldNum INTEGER,
        tenantId INTEGER,
        isIndexed BOOL
    );
"""

Data_sql = """
    DROP TABLE IF EXISTS Saas_Data;
    CREATE TABLE Saas_Data(
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