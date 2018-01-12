from control.data_layer_connector.private_method import *
#from SSMIS.control.data_layer_connector.private_method import *

table_sql = """
    INSERT INTO saas_table(tableId, tableName, tenantId)
    VALUES (%d, '%s', %d);
"""

field_sql = """
    INSERT INTO saas_field( dataType, fieldName, tableId, fieldNum, tenantId, isIndexed)
    VALUES ( '%s', '%s', %d, %d, %d, %s);
"""

# dataType, fieldName, tableId, fieldNum, tenantId, isIndexed
def create_table(tenantId, tableName):
    count = get_tablenum_new() + 1
    table_para = (count,tableName,tenantId)
    sql = table_sql % table_para #创建表
    db_template(sql)

def insert_data(tenantId, tableName, columns, values):
    tableID = get_tableID(tenantId, tableName)
    sql = "insert into saas_data (tableID, tenantId,"
    for i in columns: 
        num = get_fieldID(tenantId, tableID, i)
        sql += "value" + str(num) + ","
    sql = sql[:-1]
    sql += ") values (" + str(tableID) + "," + str(tenantId) + ","
    for i in values: 
        sql += "\"" + str(i) + "\","
    sql = sql[:-1]
    sql += ")"    
    db_template(sql)

def insert_data_n(tenantId, tableID, number, values):
    sql = "insert into saas_data (tableID, tenantId,"
    for i in range(number):
        sql += "value" + str(i) + ","
    sql = sql[:-1]
    sql += ") values (" + str(tableID) + "," + str(tenantId) + ","
    for i in values:
        sql += "\"" + str(i) + "\","
    sql = sql[:-1]
    sql += ")"
    db_template(sql)

def delete_data(tenantId, tableName, columns, conditions, condition_num):
    tableID = get_tableID(tenantId, tableName)
    sql = "delete from saas_data where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    for i in range(0,condition_num):
        num = get_fieldID(tenantId, tableID, columns[i])
        sql += " and value" + str(num) + " =\"" + str(conditions[i]) +"\""
    db_template(sql)

def select_data_all(tenantId, tableName):
    tableID = get_tableID(tenantId, tableName)
    rows = []

    sql = "select fieldNum from saas_field where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    field_rows = db_template_return(sql)

    sql = "select "
    for i in field_rows.fetchall():
        sql += " value" + str(i[0]) + ","
    sql = sql[:-1]
    sql += " from saas_data where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    rows = db_template_return(sql)
    return rows


def select_data_condition(tenantId, tableName, columns, num_of_columns, conditions_columns, conditions_operators, conditions, condition_num):
    tableID = get_tableID(tenantId, tableName)
    rows = []
    sql = "select "
    for i in range(num_of_columns):
        num = get_fieldID(tenantId,tableID,columns[i])
        sql += " value" + str(num) + " ,"
    sql = sql[:-1]
    sql += " from saas_data where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    for i in range(0,condition_num):
        num = get_fieldID(tenantId, tableID, conditions_columns[i])
        sql += " and value" + str(num) + conditions_operators[i] + "\"" + str(conditions[i]) + "\""
    rows = db_template_return(sql)
    return rows

def update(tenantId, tableName, columns, values, num_of_columns, conditions_columns, conditions_operators, conditions, condition_num):
    tableID = get_tableID(tenantId, tableName)
    sql = "update saas_data set"
    for i in range(num_of_columns):
        num = get_fieldID(tenantId,tableID,columns[i])
        sql += " value" + str(num) + " = \"" + str(values[i]) + "\","
    sql = sql[:-1]
    sql += "where tenantId= " + str(tenantId) + " and tableID= " + str(tableID)
    for i in range(0,condition_num):
        num = get_fieldID(tenantId, tableID, conditions_columns[i])
        sql += " and value" + str(num) + conditions_operators[i] + "\"" + str(conditions[i]) + "\""
    db_template(sql)
