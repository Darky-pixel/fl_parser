import db
from asyn_pars import main_pars
import draw

import sys

class api_db():
    def __init__(self):
        self.db = db.Main()
        

    def inset_data(self, projects):
        self.db.inset(projects)

    def f_draw(self):
        print(self.db.select_stats_all_prep())
        # draw(dict_data) #FIXME




if __name__ == "__main__":
    try:
        if sys.argv[1] == "-p":
            'pars without insert into DB'
            main_pars()
        elif sys.argv[1] == "-d":
            'only draw'
            #FIXME
            pass
    except IndexError:
        projects = main_pars()
        dbo = api_db()
        dbo.inset_data(projects)
        dbo.f_draw()
        
