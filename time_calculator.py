DEBUG=False

def add_time(start, duration, inputday=None):
    #Variable definition
    hour=None
    addhour=str()
    minute=None
    daylapse=0
    #Denotes AM
    morning=True
    #dictionary for day
    inputdaydict = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7
    }
    outputdaydict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        0: "Sunday",
    }  

    #Retrive optional input day 
    if inputday!=None:
        day=inputdaydict[inputday.casefold()]

    #Find the length of the starting time
    startlen=len(start)
    #Obtain last 2 char of input to find AM/PM
    morning=start[startlen-2]+start[startlen-1]
    #Find the minute in the starting time
    if start[startlen-5]==0:
        minute=int(start[startlen-4])
    else:
        minute=int(start[startlen-5]+start[startlen-4])
    #Find the hour in the starting time
    if startlen-8==0:
        hour=int(start[startlen-8]+start[startlen-7])
    else:
        hour=int(start[startlen-7])
    if morning=="PM":
        hour=hour+12
    

    #Find the length of the additional duration
    durationlen=len(duration)
    #Add minutes
    minute=minute+int(duration[durationlen-2]+duration[durationlen-1])
    #Find hours to be added. Special case if hours start with 0
    if durationlen-5==0 and duration[durationlen-5]==0:
        addhour=int(duration[durationlen-4])
    else:
        i=0
        while duration[i]!=":":
            addhour=addhour+duration[i]
            i=i+1
        addhour=int(addhour)

    #Add hours
    hour=hour+addhour
    hour=hour+minute//60
    minute=minute%60
    if minute<10:
        minute=str("0"+str(minute))
    daylapse=hour//24
    if DEBUG:
        print(day) 
    if inputday!=None:
        day=day+daylapse
        day=day%7
    if DEBUG:
        print(day) 
    if DEBUG:
        print(daylapse)    
    hour=hour%24
    if hour>11:
        hour=hour-12
        morning = "PM"
    else:
        morning = "AM"

    if hour==0:
        hour=12
    
    new_time=str(hour)+":"+str(minute)+" "+morning
    
    if inputday!=None:
        new_time=new_time+", "+outputdaydict[day]
    if daylapse>0:
        if daylapse==1:
            new_time=new_time+" (next day)"
        else:
            new_time=new_time+" ("+str(daylapse)+" days later)"

    return new_time