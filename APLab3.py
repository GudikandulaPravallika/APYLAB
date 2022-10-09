class Employee:
    def __init__(self,n,id, salary,exp):
        self.id=id
        self.name=n
        self.basicsalary=salary
        self.yoe=exp
    def display(self):
        HRA=0.2*self.basicsalary
        DA=0.5*self.basicsalary
        TA=0.11*self.basicsalary
        bonus=0.15*self.basicsalary
        if self.yoe>=2:
            bonus=bonus
        else:bonus=0
        grosssalary=self.basicsalary+(HRA+DA+TA+bonus)
        netsalary=grosssalary-(HRA+DA+TA+bonus)

        print("Name:",self.name,"net salary :",grosssalary-(HRA+DA+TA+bonus))
e1=Employee("Sita",23456,250000,6)
e1.display()
e2=Employee("Ram",42250,150000,5)
e2.display()
e3=Employee("Krishna",4221,100000,4)
e3.display()
e4=Employee("Karna",4225,90000,3)
e4.display()
e5=Employee("Arjun",4250,25000,1)
e5.display()
dict={}
dict[e1.name]=e1.basicsalary
dict[e2.name]=e2.basicsalary
dict[e3.name]=e3.basicsalary
dict[e4.name]=e4.basicsalary
dict[e5.name]=e5.basicsalary
print(dict)
print("Highest:",max(dict, key=dict.get))
print("Lowest:",min(dict, key=dict.get))
average=sum(dict.values())/len(dict)
print("Average is:",average)

    
    



        
        




        
        


    
    



        
        




        
        