from db_connector import DatabaseConnection, config

class DBHelper():
    def __init__(self):
        self.connection = None

#Chat1
    # def execute(self, sql):
    #     try:
    #         with DatabaseConnection(config) as connection:
    #             cursor = connection.cursor()
    #             cursor.execute(sql)
    #             print(sql)
    #             result = list()
                
    #             #if cursor.rowcount == 0:
    #             #    return result
                
    #             for row in cursor.fetchall():
    #                 result.append(row)
                
    #             connection.commit()
    #             cursor.close()
    #             return result
    #     except Exception as e:
    #         # Trate exceções aqui, por exemplo, registre o erro ou faça algo apropriado
    #         print("Erro ao executar SQL:", e)  # Use 'print(e)' para a mensagem de erro
    #         return None  # Ou raise a exceção novamente, dependendo do comportamento desejado



    def execute(self, sql):
        with DatabaseConnection(config) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            if sql.split()[0].upper() =='SELECT':
                result = list()#ok
            #if cursor.rowcount == 0:
            #    return result            
                for row in cursor.fetchall():
                    result.append(row)
                connection.commit()
                cursor.close()
                return result
            else:
                connection.commit()
                cursor.close()
                return None
            
    
    
    
    def executeCUD(sql, params=None, fetch=False):
        with DatabaseConnection(config) as connection:            
            cursor = connection.cursor()
            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)

            if sql.strip().split()[0].upper() == 'SELECT':
                if fetch:
                    result = cursor.fetchall()
                else:
                    result = None
            else:
                connection.commit()
                result = None

            cursor.close()
            connection.close()
            return result

        

# Example usage:
# INSERT query
# sql_insert = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
# params_insert = ('value1', 'value2')
# execute_sql(sql_insert, params_insert)

# UPDATE query
# sql_update = "UPDATE your_table SET column1 = %s WHERE column2 = %s"
# params_update = ('new_value', 'target_value')
# execute_sql(sql_update, params_update)

# DELETE query
# sql_delete = "DELETE FROM your_table WHERE column = %s"
# params_delete = ('value_to_delete',)
# execute_sql(sql_delete)

# SELECT query
# sql_select = "SELECT * FROM your_table"
# result = execute_sql(sql_select, fetch=True)
# if result:
#     for row in result:
#         print(row)












    # def execute(self, sql):
    #     with DatabaseConnection(config) as connection:
    #         cursor = connection.cursor()
    #         cursor.execute(sql)
    #         result = list()
    #         #if cursor.rowcount == 0:
    #         #    return result            
    #         for row in cursor.fetchall():
    #             result.append(row)
    #         connection.commit()
    #         cursor.close()
    #         return result
