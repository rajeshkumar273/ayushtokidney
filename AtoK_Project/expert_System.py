from experta import *
class Loads(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(Problem="AtoK")
        print(" An Expert System for Chronic Kidney disease".center(80, "*"))
        print(" Chronic Kidney disease problems with Water Fluoride".center(80, "*"))
        print(" Programmed by Eng:Mothukuri RajeshKumar".center(80, "*"))
        print("".center(80, "*"))
        print("".center(80, "*"))
    #Rule 1
    @Rule(Fact(Problem='AtoK'), NOT(Fact(Q1=W())))
    def ask_id(self):
        self.declare(Fact(Q1=input("Q1: Do you have Chronic Kidney disease or Symtopys?Please type Yes/No: ")))
    #Rule 2
    @Rule(Fact(Problem='AtoK'),(Fact(Q1='yes')))
    def ask_1(self):
        self.declare(Fact(Q2=float(input("Q2:How much you have Specify Gravity 1.000 to 1.025: "))))
    #Rule 3
    @Rule(Fact(Problem='AtoK'),(AND(Fact(Q1='yes'),(Fact(Q2=1.000)))))
    def ask_2(self):
        self.declare(Fact(Q3=int(input("Q3: Hypertension Yes=1 or No=0: "))))
    #Rule 4
    @Rule(Fact(Problem='AtoK'), (AND(Fact(Q1='yes'),Fact(Q2=1.000), Fact(Q3=1))))
    def ask_3(self):
        self.declare(Fact(Q4=float(input("Q4: Please Specify Hemoglobin in grms:"))))    
    #Rule 5
    @Rule(Fact(Problem='AtoK'), (AND(Fact(Q1='yes'),Fact(Q2=1.000), Fact(Q3=1),Fact(Q4=15.4))))
    def ask_4(self):
        self.declare(Fact(Q5=int(input("Q5: Do you have Daibetes Mellitus Yes=1 or No=0:")))) 
    #Rule 6
    @Rule(Fact(Problem='AtoK'), (AND(Fact(Q1='yes'),Fact(Q2=1.000), Fact(Q3=1),Fact(Q4=15.4),Fact(Q5=1))))
    def ask_5(self):
        self.declare(Fact(Q6=int(input("Q6: Please select Albumin range(0,1,2,3,5):")))) 
    #Rule 7
    @Rule(Fact(Problem='AtoK'), (AND(Fact(Q1='yes'),Fact(Q2=1.000), Fact(Q3=1),Fact(Q4=15.4),Fact(Q5=1),Fact(Q6=1))))
    def ask_6(self):
        self.declare(Fact(Q7=int(input("Q7: Appetite if Good=1,Poor=0:")))) 
    #Rule 8
    @Rule(Fact(Problem='AtoK'), (AND(Fact(Q1='yes'),Fact(Q2=1.000), Fact(Q3=1),Fact(Q4=15.4),Fact(Q5=1),Fact(Q6=1),Fact(Q7=0))))
    def ask_7(self):
        self.declare(Fact(Q8=int(input("Q9: Pus Cell Normal=0, Abnormal=1:")))) 
    #Rule 9
    @Rule(Fact(Problem='AtoK'), (AND(Fact(Q1='yes'),Fact(Q2=1.000), Fact(Q3=1),Fact(Q4=15.4),Fact(Q5=1),Fact(Q6=1),Fact(Q7=0),Fact(Q8=1))))
    def ask_8(self):
        self.declare(Fact(Q9=float(input("Q10: Fluoride in drinking water(0.5 to 1 ppm): ")))) 
    #Rule 10
    @Rule(Fact(Problem='AtoK'), (AND(Fact(Q1='yes'),Fact(Q2=1.000), Fact(Q3=1),Fact(Q4=15.4),Fact(Q5=1),Fact(Q6=1),Fact(Q7=0),Fact(Q8=1),Fact(Q9=1.1))))
    def diagnosis_1(self):
        print("")
        print("You may have Kidney Disease.")
        print("SELF CARE".center(20, "*"))
        print("See your doctor.")
    #Rule 11
    @Rule(Fact(problem='AtoK'),(AND(Fact(Q1='no'),Fact(Q2=1.020),Fact(Q3=0),Fact(Q4=15.8),Fact(Q5=3),Fact(Q6=1),Fact(Q7=1),Fact(Q8=0.7))))
    def diagnosis_2(self):
        print("")
        print("Congrations")

"""if __name__ == "__main__":
	engine = Loads()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Would you like exit?")
		if input() == "yes":
			exit()
		#print(engine.facts)"""



engine=Loads()
engine.reset()
engine.run()
input('press enter to exit')

    
    


    