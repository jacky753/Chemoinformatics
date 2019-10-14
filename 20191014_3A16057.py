#your name
yourname = input("What's your name?") 
yoursex = int(input("What's your biological sex?Male=1, Female=0:"))

#white blood cell  count
wbcc = int(input("How many your white blood cells are?[/mm^3]:"))
#red blood cell count
rbcc = int(input("How many your red blood cells are?[x10^4/mm^3]:"))
#hemoglobin count
hmgc = int(input("How many your hemogrobins are?[g/dL]:"))
#hematocrit count
hmcc =  int(input("How many your hematocrit are?[%]:"))
#platelets count
pltc = int(input("How many your platelets are?[x10^4/μL]"))

if yoursex == 1:
    if wbcc < 3300 or wbcc > 9000:
        print("Abnormal")
    else:
        print("Normal")
    if rbcc < 430 or rbcc > 570:
        print("Abnormal")
    else:
        print("Normal")
    if hmgc < 13.5   or hmgc  > 17.5:
        print("Abnormal")
    else:
        print("Normal")
    if hmcc < 39.7 or hmcc > 52.4:
        print("Abnormal")
    else:
        print("Normal")
    if pltc < 14.0 or pltc  > 37.9:
        print("Abnormal")
    else:
        print("Normal")
else:
    if wbcc > 3300 or wbcc > 9000:
        print("Abnormal")
    else:
        print("Normal")
    if rbcc < 380 or rbcc > 500:
        print("Abnormal")
    else:
        print("Normal")
    if hmgc  < 11.5 or  hmgc >15.0:
        print("Abnormal")
    else:
        print("Normal")
    if hmcc < 34.8 or hmcc > 45.0:
        print("Abnormal")
    else:
        print("Normal")
    if pltc <  14.0 or pltc  > 37.9:
        print("Abnormal")
    else:
        print("Normal")
print("Value judgment is complete.")

