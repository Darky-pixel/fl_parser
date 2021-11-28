import sqlite3
import datetime
import abc




class Core(abc.ABC):
    def __init__(self, path_db):
        self.__base = sqlite3.connect(path_db)
        self.__cursor = self.__base.cursor()
        self.__cursor.execute("PRAGMA foreign_keys = ON")
        # https://stackoverflow.com/questions/7985645/on-delete-cascade-not-working-in-sqlite

    def __insert_state(self, id_count):
        self.__cursor.execute("INSERT INTO stats (date, id_count) VALUES (?, ?)", (datetime.date.today(), id_count))
   
    @abc.abstractmethod
    def inset(self, stat):
        stat = stat.items()
        stat_keys = tuple(map(lambda x: x[0], stat))
        stat_value = tuple(map(lambda x: x[1], stat))
        self.__cursor.execute(f"INSERT INTO count {stat_keys} VALUES {stat_value}")
        current_id = self.__cursor.execute("SELECT MAX(id) FROM count").fetchall()
        self.__insert_state(current_id[0][0])

    def _select_stats_last(self):
        return self.__cursor.execute("""SELECT date, django, flask, telegram_bot, instagram_bot, vk_bot, sql
                                        FROM stats s JOIN count c ON s.id_count = c.id 
                                        WHERE s.id = (SELECT MAX(id) FROM stats)""").fetchall()

    def _select_stats_all(self):
        return self.__cursor.execute("""SELECT date, django, flask, telegram_bot, instagram_bot, vk_bot, sql
                                        FROM stats s JOIN count c ON s.id_count = c.id""").fetchall()

    def del_all_data(self):
        print('del all data')
        self.__cursor.execute("DELETE FROM count")

    def __del__(self):
        print("commit db")
        self.__base.commit()



class Main(Core):
    def __init__(self, path_db="db.db"):
        super().__init__(path_db=path_db)

    def inset(self, stat):
        super().inset(stat)
    
    def select_stats_all_prep(self, last=False):

        """{'2021-11-23': [10.0, 3.0, 2.0, 1.0, 4.0, 9.0]}"""

        def avg(dict_data, data_prep):
            """if the date is the same"""

            dict_data = list(dict_data)
            len1 = len(dict_data)
            for i in range(len1):
                dict_data[i] = (dict_data[i] + data_prep[i]) / 2
            return tuple(dict_data)

        if last:
            date_data = self._select_stats_last()
        else:
            date_data = self._select_stats_all()

        res = dict()
        for i in date_data:
            date = i[0]
            data = i[1:]

            if date in res.keys():
                data = avg(res[date], data)

            res[date] = data
        return res

    def del_all_data(self):
        super().del_all_data()



if __name__ == "__main__":
    term = Main(path_db="db_for_test.db")
    term.del_all_data() 
