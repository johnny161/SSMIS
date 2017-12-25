from control.data_layer_connector.private_method import *


field_sql = """
    INSERT INTO saas_field( dataType, fieldName, tableId, fieldNum, tenantId)
    VALUES ( '%s', '%s', %d, %d, %d);
"""

def add_field(tenantId, tableName, column_name, column_type):
    tableId = get_tableID(tenantId, tableName)
    count = get_fieldnum(tenantId, tableId) + 1
    table_para = (count,tableName,tenantId)
    tmp = (column_type,column_name,tableId,count,tenantId)
    sql = field_sql % tmp
    db_template(sql)

def delete_table(tenantId,tableName):
    tableID = get_tableID(tenantId, tableName)
    sql = "delete from saas_table where tenantId=" + str(tenantId) + " AND tableId=" + str(tableId) + " ;"
    sql += "delete from saas_field where tenantId=" + str(tenantId) + " AND tableId=" + str(tableId) + " ;"
    sql += "delete from saas_data where tenantId=" + str(tenantId) + " AND tableId=" + str(tableId) + " ;"
    db_template(sql)

def delete_field(tenantId, tableName, fieldName):
    tableId = get_tableID(tenantId, tableName)
    fieldNum = get_fieldID(tenantId, tableId, fieldName)
    sql = "delete from saas_field where tenantId=" + str(tenantId) + " AND tableId=" + str(tableId) + " AND field_num= " + str(fieldNum) + " ;"
    sql += "update saas_data set value" + str(fieldNum) + "=Null where tenantId=" + str(tenantId) + " AND tableId=" + str(tableId) + " ;"
    db_template(sql)

def add_field_new(tenantId, tableId, column_name, column_type):
    count = get_fieldnum(tenantId, tableId) + 1
    tmp = (column_type,column_name,tableId,count,tenantId)
    sql = field_sql % tmp
    db_template(sql)
