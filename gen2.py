import numpy as np
####################
class algorithm():
    def __init__(self):
        self.startprices=[119,47,130,164,293,224,104,402,281,93]
        self.timeperunit=[2.95,3,3.875,4.7,7.56,4.25,1.63,10.5,6.3,3.3]
        self.factor=0.1
        self.janArray=np.array([self.startprices,[self.januaryscreenrepairdemand,self.januarykeyboarddemand,self.januarypsudemand,self.januaryharddiskdemand,self.januarymotherboarddemand,self.januaryvirusremovaldemand,self.januaryfirewallsetupdemand,self.januarydatarecoverydemand,self.januarynetworktroubleshootdemand,self.januarymaintenancedemand],[243,210,196,174,110,131,229,78,133,187],self.timeperunit])
        self.febArray=np.array([self.startprices,[self.februaryscreenrepairdemand,self.februarykeyboarddemand,self.februarypsudemand,self.februaryharddiskdemand,self.februarymotherboarddemand,self.februaryvirusremovaldemand,self.februaryfirewallsetupdemand,self.februarydatarecoverydemand,self.februarynetworktroubleshootdemand,self.februarymaintenancedemand],[193,187,195,168,100,101,197,66,130,194],self.timeperunit])
        self.marArray=np.array([self.startprices,[self.marchscreenrepairdemand,self.marchkeyboarddemand,self.marchpsudemand,self.marchharddiskdemand,self.marchmotherboarddemand,self.marchvirusremovaldemand,self.marchfirewallsetupdemand,self.marchdatarecoverydemand,self.marchnetworktroubleshootdemand,self.marchmaintenancedemand],[205,214,218,183,112,123,216,79,130,209],self.timeperunit])
    def returnArray(self,str):
        """
        returns the array object given the months abbrievated name(jan,feb, or march)
        """
        if str=='jan':return self.janArray
        elif str=='feb':return self.febArray
        elif str=='mar':return self.marArray
        else: print('invalid month')
    def adjdemandall(self,prodtype,adj):
        self.adjdemand('jan',prodtype,adj)
        self.adjdemand('feb',prodtype,adj)
        self.adjdemand('mar',prodtype,adj)
    def adjdemand(self,monthname,prodtype,adj):
        """
        changed prices by amount (adj) to increase or decrease demand. positive adj increases and negative decreases
        also must specify product type with hardware or software as a string.
        """
        if adj<0:absadj=adj*-1; adj=-1
        elif adj>0:absadj=adj*1; adj=1
        array=self.returnArray(monthname)
        if prodtype=='hardware':
            for i in range(absadj):
                if 0<array[1,0](array[0,0]-adj)<array[2,0]:array[0,0]-=adj
                elif 0<array[1,1](array[0,1]-adj)<array[2,1]:array[0,1]-=adj
                elif 0<array[1,2](array[0,2]-adj)<array[2,2]:array[0,2]-=adj
                elif 0<array[1,3](array[0,3]-adj)<array[2,3]:array[0,3]-=adj
                elif 0<array[1,4](array[0,4]-adj)<array[2,4]:array[0,4]-=adj
                else: print('demand has reached a limit')
        elif prodtype=='software':
            for i in range(absadj):
                if 0<array[1,5](array[0,5]-adj)<array[2,5]:array[0,5]-=adj
                elif 0<array[1,6](array[0,6]-adj)<array[2,6]:array[0,6]-=adj
                elif 0<array[1,7](array[0,7]-adj)<array[2,7]:array[0,7]-=adj
                elif 0<array[1,8](array[0,8]-adj)<array[2,8]:array[0,8]-=adj
                elif 0<array[1,9](array[0,9]-adj)<array[2,9]:array[0,9]-=adj
                else: print('demand has reached a limit')
    def januaryscreenrepairdemand(self,price):
        return -5.19*price+630
    def februaryscreenrepairdemand(self,price):
        return -4.31*price+525
    def marchscreenrepairdemand(self,price):
        return -4.66*price+572
    def januarykeyboarddemand(self,price):
        return -12.1*price+581
    def februarykeyboarddemand(self,price):
        return -12.7*price+608
    def marchkeyboarddemand(self,price):
        return -12.1*price+590
    def januarypsudemand(self,price):
        return -3.74*price+507
    def februarypsudemand(self,price):
        return -4.25*price+561
    def marchpsudemand(self,price):
        return -4.48*price+603
    def januaryharddiskdemand(self,price):
        return -3.46*price+629
    def februaryharddiskdemand(self,price):
        return -3.07*price+555
    def marchharddiskdemand(self,price):
        return -3.46*price+625
    def januarymotherboarddemand(self,price):
        return -1.73*price+586
    def februarymotherboarddemand(self,price):
        return -1.75*price+586
    def marchmotherboarddemand(self,price):
        return -1.9*price+629
    def januaryvirusremovaldemand(self,price):
        return -1.31*price+396
    def februaryvirusremovaldemand(self,price):
        return -1.04*price+318
    def marchvirusremovaldemand(self,price):
        return -1.23*price+374
    def januaryfirewallsetupdemand(self,price):
        return -3.85*price+573
    def februaryfirewallsetupdemand(self,price):
        return -3.35*price+494
    def marchfirewallsetupdemand(self,price):
        return -3.79*price+557
    def januarydatarecoverydemand(self,price):
        return -.543*price+236
    def februarydatarecoverydemand(self,price):
        return -.527*price+231
    def marchdatarecoverydemand(self,price):
        return -.594*price+258
    def januarynetworktroubleshootdemand(self,price):
        return -1.72*price+499
    def februarynetworktroubleshootdemand(self,price):
        return -1.65*price+475
    def marchnetworktroubleshootdemand(self,price):
        return -1.6*price+467
    def januarymaintenancedemand(self,price):
        return -5.53*price+530
    def februarymaintenancedemand(self,price):
        return -4.7*price+454
    def marchmaintenancedemand(self,price):
        return -6.5*price+631
    def getDelta(self,eqn1,eqn2,t1,t2,unit=1):
        """
        returns the change in one variable given one unit change in another
        the change is the variable in unit two. unit defaults to $1
        """
        factor1=eqn1(1)-eqn1(0)
        factor2=eqn2(1)-eqn2(0)
        return (unit*factor1*t1)/(factor2*t2)
    def profit(self,eqn1,price1,eqn2,price2):
        return price1*eqn1(price1)+price2*eqn2(price2)
    def improve(self,arrayname,idx1,idx2):
        array=self.returnArray(arrayname)
        comparisonList=[self.profit(array[1,idx1],array[0,idx1],array[1,idx2],array[0,idx2]),self.profit(array[1,idx1],array[0,idx1]+self.factor,array[1,idx2],array[0,idx2]-self.factor*self.getDelta(array[1,idx1],array[1,idx2],array[3,idx1],array[3,idx2])),self.profit(array[1,idx1],array[0,idx1]-self.factor,array[1,idx2],array[0,idx2]+self.factor*self.getDelta(array[1,idx1],array[1,idx2],array[3,idx1],array[3,idx2]))]
        case=np.argmax(comparisonList)
        if case == 0:
            print('unchanged')
        if case == 1:
            if 0<array[1,idx1](array[0,idx1]+self.factor)<array[2,idx1] and 0<array[1,idx2](array[0,idx2]-self.factor*self.getDelta(array[1,idx1],array[1,idx2],array[3,idx1],array[3,idx2]))<array[2,idx2]:
                print('adjusted')
                array[0,idx1]+=self.factor
                array[0,idx2]-=self.factor*self.getDelta(array[1,idx1],array[1,idx2],array[3,idx1],array[3,idx2])
            else:
                print('unchanged bec bounds have been reached')
        if case == 2:
            if 0<array[1,idx1](array[0,idx1]-self.factor)<array[2,idx1] and 0<array[1,idx2](array[0,idx2]+self.factor*self.getDelta(array[1,idx1],array[1,idx2],array[3,idx1],array[3,idx2]))<array[2,idx2]:
                print('adjusted')
                array[0,idx1]-=self.factor
                array[0,idx2]+=self.factor*self.getDelta(array[1,idx1],array[1,idx2],array[3,idx1],array[3,idx2])
            else:
                print('unchanged bec bounds have been reached')
    def train(self,monthname,iterations):
        for i in range(iterations):
            self.improve(monthname,np.random.randint(0,5),np.random.randint(0,5))
            self.improve(monthname,np.random.randint(5,10),np.random.randint(5,10))
    def trainall(self,iterations):
        self.train('jan',iterations)
        self.train('feb',iterations)
        self.train('mar',iterations)
    def roundlist(self,list):
        roundedlist=[]
        for i in list:
            roundedlist.append(round(i))
        return roundedlist
    def setPrices(self,moname,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):
        array = self.returnArray(moname)
        array[0]=[p6,p7,p8,p9,p10,p1,p2,p3,p4,p5]
    def outputprices(self,arrayname):
        array=self.returnArray(arrayname)
        print(arrayname+'prices:')
        print(str(self.roundlist(np.array_split(array[0],2)[1])))
        print(str(self.roundlist(np.array_split(array[0],2)[0])))
        
    