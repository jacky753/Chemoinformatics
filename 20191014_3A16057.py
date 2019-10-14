class PatientData():
    def __init__(self, n, s):
        self.name = n
        self.sex = s
    #function for input and judge data
    def patient_data(self):
        #white blood cell  count
        wbcc = int(input("How many {}'s white blood cells are?[/mm^3]:".format(self.name)))
        #red blood cell count
        rbcc = int(input("How many {}'s red blood cells are?[x10^4/mm^3]:".format(self.name)))
        #hemoglobin count
        hmgc = int(input("How many {}'s hemogrobins are?[g/dL]:".format(self.name)))
        #hematocrit count
        hmcc =  int(input("How many {}'s hematocrit are?[%]:".format(self.name)))
        #platelets count
        pltc = int(input("How many {}'s platelets are?[x10^4/μL or x10^4/mm^3]:".format(self.name)))

        if self.sex == 1:
            print("wbc:")
            if wbcc < 3300 or wbcc > 9000:
                print("Abnormal")
            else:
                print(" Normal")
            print("rbc:")
            if rbcc < 430 or rbcc > 570:
                print(" Abnormal")
            else:
                print(" Normal")
            print("hmg:")
            if hmgc < 13.5   or hmgc  > 17.5:
                print(" Abnormal")
            else:
                print(" Normal")
            print("hmc:")
            if hmcc < 39.7 or hmcc > 52.4:
                print(" Abnormal")
            else:
                print(" Normal")
            print("plt:")
            if pltc < 14.0 or pltc  > 37.9:
                print(" Abnormal")
            else:
                print(" Normal")
        else:
            print("wbc:")
            if wbcc > 3300 or wbcc > 9000:
                print(" Abnormal")
            else:
                print(" Normal")
            print("rbc:")
            if rbcc < 380 or rbcc > 500:
                print(" Abnormal")
            else:
                print(" Normal")
            print("hmg:")
            if hmgc  < 11.5 or  hmgc >15.0:
                print(" Abnormal")
            else:
                print(" Normal")
            print("hmc:")
            if hmcc < 34.8 or hmcc > 45.0:
                print(" Abnormal")
            else:
                print(" Normal")
            print("plt:")
            if pltc <  14.0 or pltc  > 37.9:
                print(" Abnormal")
            else:
                print(" Normal")
        print("Value judgment is complete.")


if __name__ == '__main__':
    #your name and sex
    yourname = input("What's your name?:") 
    yoursex = int(input("What's {}'s biological sex? Male=1, Female=0:".format(yourname)))

    patient1 = PatientData(yourname, yoursex) 
    patient1.patient_data()
