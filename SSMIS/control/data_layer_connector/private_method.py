# -*- coding:utf-8 -*-
from control.data_layer_connector.connector1 import Connector
#from SSMIS.control.data_layer_connector.connector1 import Connector

def db_template(sql):
    conn = Connector()
    conn.connect()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print('load sql')
        print('e\t' + str(e))
    finally:
        cur.close()
        conn.close()

def db_template_return(sql):
    rows = []
    conn = Connector()
    conn.connect()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
    except Exception as e:
        print('load sql')
        print('e\t' + str(e))
    finally:
        cur.close()
        conn.close()
        return rows

def get_tablenum(tenantId):
    count = 0
    sql = "select max(tableID) from saas_table where tenantId = " + str(tenantId)
    rows = db_template_return(sql)
    for row in rows:
            if row[0] != None:
                count = row[0]
    return count 

def get_fieldnum(tenantId, tableID):
    count = 0
    sql = "select max(fieldNum) from saas_field where tenantId = " + str(tenantId) + " and tableID=" + str(tableID)
    rows = db_template_return(sql)
    for row in rows:
            if row[0] != None:
                count = row[0]
    return count 

def get_tableID(tenantId, tableName):
    ID = "Not Found"
    sql = "select tableId from saas_table where tenantId = \"" + str(tenantId) + "\" and tableName=\"" + str(tableName) + "\""
    rows = db_template_return(sql)
    for row in rows:
            ID = row[0]
    return ID
        
    
def get_fieldID(tenantId, tableID, FieldName): #大小写
    Num = "Not Found"
    sql = "select fieldNum from saas_field where tenantId = " + str(tenantId) + " and tableId=" + str(tableID) + " and fieldName=\"" + str(FieldName) + "\""
    rows = db_template_return(sql)
    for row in rows:
            Num = row[0]
    return Num

def get_tableIDs(tenantId):
    ID = "Not Found"
    sql = "select tableID from saas_table where tenantId = \"" + str(tenantId)  + "\""
    rows = db_template_return(sql)
    for row in rows:
            ID = row[0]
    return ID

def get_tablenum_new():
    count = 0
    sql = "select max(tableID) from saas_table "
    rows = db_template_return(sql)
    for row in rows:
            if row[0] != None:
                count = row[0]
    return count


