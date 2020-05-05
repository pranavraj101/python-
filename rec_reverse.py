Reverse=0
def Reverse_Integer(Number):
    global Reverse
    if(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Reverse_Integer(Number //10)
    return Reverse