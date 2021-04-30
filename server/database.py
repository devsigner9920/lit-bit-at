import pymysql as mysql
import configparser


class db(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)

            config = configparser.ConfigParser()
            config.read('app.cfg')

            # db connection
            info = config['db_info']
            cls.db = mysql.connect(
                host=info['host'],
                user=info['user'],
                password=info['password'],
                db=info['db'],
                charset=info['charset']
            )

            cls.cursor = cls.db.cursor(mysql.cursors.DictCursor)

        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            print("__init__ is called\n")
            cls._init = True

    def get_cursor(self):
        return self.cursor

    def select(self, sql, fetch=True):
        if fetch:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        else:
            result = self.cursor.execute(sql)

        self.db.close()

        return result

    def insert(self, sql, commit=True):
        if commit:
            result = self.cursor.execute(sql)

            self.db.commit()
        else:
            result = self.cursor.execute(sql)

        self.db.close()

        return result

    def insert(self, sql, param=[], commit=True):
        if commit:
            result = self.cursor.execute(sql, param)

            self.db.commit()
        else:
            result = self.cursor.execute(sql, param)

        self.db.close()

        return result

    def update(self, sql, commit=True):
        if commit:
            result = self.cursor.execute(sql)

            self.db.commit()
        else:
            result = self.cursor.execute(sql)

        self.db.close()

        return result

    def update(self, sql, param=[], commit=True):
        if commit:
            result = self.cursor.execute(sql, param)

            self.db.commit()
        else:
            result = self.cursor.execute(sql, param)

        self.db.close()

        return result

    def delete(self, sql, commit=True):
        if commit:
            result = self.cursor.execute(sql)

            self.db.commit()
        else:
            result = self.cursor.execute(sql)

        self.db.close()

        return result

    def delete(self, sql, param=[], commit=True):
        if commit:
            result = self.cursor.execute(sql, param)

            self.db.commit()
        else:
            result = self.cursor.execute(sql, param)

        self.db.close()

        return result
