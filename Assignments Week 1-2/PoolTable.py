from datetime import datetime
pool_tables = []

class PoolTable:
    def __init__(self,index):
        self.table_no          = index
        self.availability      = True
        self.start_time        = 0
        self.end_time          = 0
        self.total_time_played = 0

    def check_out():
        display_all_tables()
        user_input = int(input("Which table would you like to check out?"))
        print("Processesing")
        checkoutnumber = pool_tables[user_input -1]
        pool_table.availability = False
        start_time = time.time()


    def check_in():
        display_all_tables()
        user_input = int(input("Which table were you using?"))
        print("Processesing")
        check_in_number = pool_tables[user_input -1]
        pool_table.availability = True
        end timer = time.time()
        total_time = end_time - start_time



def display_all_tables():
    print(f"Table:--Availability:")
    for index in range(0,len(pool_tables)):
        table = pool_tables[index]
    print(f"{pool_table.table_no} --------{pool_table.availability}")
    if pool_table.availability == False:
        print("Occupied")

for index in range(1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)
view_all_tables()
