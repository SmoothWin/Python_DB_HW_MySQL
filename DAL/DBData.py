import mysql.connector


class DBData:
    def __init__(self):
        try:
            self.config_file = "my.conf"
            self.connex = mysql.connector.connect(option_files=self.config_file)
        except mysql.connector.Error as err:
            print(err)
            self.close()

    def execute_select_query(self, table_name, params=None):
        return_Set = []
        cursor = self.connex.cursor(dictionary=True)
        try:

            if params is None:
                cursor.execute("SELECT * FROM {}".format(table_name))


            else:
                where_clause = "WHERE " + " AND ".join(['`' + k + '` = %s' for k in params.keys()])
                values = list(params.values())
                sql = "SELECT * FROM {} {}".format(table_name, where_clause)
                cursor.execute(sql, values)

            for row in cursor:
                return_Set.append(row)
            return return_Set
        except mysql.connector.Error as err:
            print(err)
            self.close()

    def execute_insert_query(self, table_name, params=None):
        cursor = self.connex.cursor(dictionary=True)
        try:
            sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name,
                                                           ", ".join(params.to_dict().keys()),
                                                           ", ".join(["%s" for i in range(len(params.to_dict()))]))
            print(params.to_dict())
            cursor.execute(sql, list(params.to_dict().values()))

            self.connex.commit()
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(err.msg())
            self.close()


    def close(self):
        self.connex.close()
