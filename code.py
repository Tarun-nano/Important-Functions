# getting start and end date by passing week number and year

def getDateRangeFromWeek(p_year,p_week):

    firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)
    return firstdayofweek, lastdayofweek


# converting seconds into HH:MM:SS format

def convert(seconds): 
    return time.strftime("%H:%M:%S", time.gmtime(seconds))  
    


# splitting a string column at specific character into two or more columns
data["column_new"]=data["column_old"].str.split("-").str[0]



