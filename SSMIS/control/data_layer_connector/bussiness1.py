from control.data_layer_connector.private_method import *
#from SSMIS.control.data_layer_connector.private_method import *
#from SSMIS.control.data_layer_connector.saas_method import *
#from control.data_layer_connector.saas_method import *
#from control.data_layer_connector.base_method import *

data_sql = """
    INSERT INTO saas_data (tableId,tenantId,value0,value1,value2,value3,value4,value5,value6,value7,value8,value9)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
"""

def get_table_list(tenantId):
    ID = "Not Found"
    sql = "select tableName from saas_table where tenantId = \"" + str(tenantId) + "\""
    rows = db_template_return(sql)
    list = []
    for row in rows:
        list.append(row[0])
    return list

def get_table_list_new(tenantId):
    ID = "Not Found"
    sql = "select tableId,tableName from saas_table where tenantId = \"" + str(tenantId) + "\""
    rows = db_template_return(sql)
    list = []
    for row in rows:
        list.append(row)
    return list

def get_field_list(tableId,tenantId):
    ID="Not Found"
    sql="select fieldId,dataType,fieldName,fieldNum from saas_field where tenantId = \"" + str(tenantId) +"\"" + " AND tableId=" + str(tableId)
    rows = db_template_return(sql)
    list = []
    for row in rows:
        list.append(row)
    return list

def get_data_list(tableId,tenantId):
    ID = "Not Found"
    sql = "select value0,value1,value2,value3,value4,value5,value6,value7,value8,value9 from saas_data where tenantId = \"" + str(
        tenantId) + "\"" + " AND tableId=" + str(tableId)
    rows = db_template_return(sql)
    list = []
    for row in rows:
        list.append(row)
    return list

def get_field_name_list(tableId,tenantId):
    ID="Not Found"
    sql="select fieldName from saas_field where tenantId = \"" + str(tenantId) +"\"" + " AND tableId=" + str(tableId)
    rows = db_template_return(sql)
    list = []
    for row in rows:
        list.append(row[0])
    return list

#有些问题，暂用下个函数代替
def insert_data(tableId, tenantId, v0=None, v1=None, v2=None, v3=None, v4=None, v5=None, v6=None, v7=None, v8=None, v9=None):
    tmp = (tableId, tenantId, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9)
    sql = data_sql % tmp
    db_template(sql)

#
def insert_data_new(table_id,tenant_id,v0=None,v1=None,v2=None,v3=None,v4=None,v5=None,v6=None,v7=None,v8=None,v9=None):
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='14349024', db='ssmis_test1', charset='utf8')
    except:
        print(u'连接mysql数据库失败')
    else:
        cur = conn.cursor()
        sql = (
        'INSERT INTO saas_data (tableId,tenantId,value0,value1,value2,value3,value4,value5,value6,value7,value8,value9) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
        params = (table_id,tenant_id,v0,v1,v2,v3,v4,v5,v6,v7,v8,v9)
        cur.execute(sql, params)
        conn.commit()
    finally:
        cur.close()
        conn.close()

def get_table_name(tableId,tenantId):
    ID = "Not Found"
    sql = "select tableName from saas_table where tenantId = \"" + str(tenantId) + "\"" + " AND tableId=" + str(tableId)
    rows = db_template_return(sql)
    for row in rows:
        ID = row[0]
    return ID

#get_table_list_new(2)
#print (get_table_list_new(2)[1][0])
#insert_data_new('18','2','11','22','33')
#v0=None, v1=None, v2=None, v3=None, v4=None, v5=None, v6=None, v7=None, v8=None, v9=None
#insert_data('5','2','11','22','11','22','11','22','11','22','11','22')