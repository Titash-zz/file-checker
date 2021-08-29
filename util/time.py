import datetime

def convert_time():
    my_date = datetime.datetime.today()
    year,month,day = my_date.year,my_date.month,my_date.day  

    splitted_time = "09:00".split(":")
    hh= int(splitted_time[0])
    mm= int(splitted_time[1])

    print(datetime.datetime.combine(datetime.date(year, month, day), 
                          datetime.time(hh, mm)))