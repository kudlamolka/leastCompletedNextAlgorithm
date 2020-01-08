class Process:
	def __init__(self,Sl,name,AT,BT,CT,TAT,WTAT):
		self.Sl = Sl;
		self.name = name;
		self.AT = AT;
		self.BT = BT;
		self.CT = CT;
		self.TAT = TAT;
		self.WTAT = WTAT;
		self.LT = BT;
	
	def BTnow(val):
		return Pros[val].LT;
	
	
	def time_reduce(self,time_slice,time):
		dec = 0;
		for i in range(time_slice):
			self.LT = self.LT - 1;
			dec = dec+1;	
			if(self.LT==0):
				self.CT = time+dec;
				break;
		return dec;
	def T_A_T(self):
		self.TAT = self.CT - self.AT;
		return self.TAT;
	
	def W_T_A_T(self):
		self.WTAT = self.TAT/self.BT;
		return self.WTAT;  



def display_processes(Pros,N):
	print(" Process \t Arrival Time \t Service Time \t Completion Time       T.A.T           W.T.A.T ");
	print("="*9+"\t"+"="*14+"\t"+"="*14+"\t"+"="*17+"     "+"="*7+"\t      "+"="*9);
	for i in range(N):
		print("P"+str(i),\
		"\t\t\t",Pros[i].AT,\
		"\t\t",Pros[i].BT, \
		"\t\t",Pros[i].CT, \
		"\t\t",Pros[i].TAT, \
		"\t\t",round(Pros[i].WTAT,2));


def sumUp(Pros,N):
	TotalTime = 0;
	for i in range(N):
		TotalTime = TotalTime+Pros[i].BT
	return TotalTime;

def CheckArrival(Pros,N):
	arrived = [];
	for k in range(N):
		if(time>=Pros[k].AT):
			arrived.append(k);
	return arrived;
	

print("How many process do we have?");
N = int(input("Enter Here:"));
Pros = [];
for i in range(N):
	Pros.append("P"+str(i));
for i in range(N):
	AT = int(input("Arrival Time of P"+str(i)+":"));
	BT = int(input("Service Time of P"+str(i)+":"));
	Pros[i] = Process(i,Pros[i],AT,BT,0,0,0);
display_processes(Pros,N);
time_slice = int(input("\n\nEnter the Time Slice:"));
TotalTime = sumUp(Pros,N);
time=0;

while(time<=TotalTime):
	dec = 0;
	QUEUE = 0;
	arrived = CheckArrival(Pros,len(Pros));
	print("\n\nAT Time = ",time);
	arrived.sort(key = lambda x: Pros[x].LT,reverse=True);
	print("PROCESSES NOW Waiting");
	for k in arrived:
		if(Pros[k].LT!=0):
			print(Pros[k].name, end=" ");
			QUEUE = 1;
	if(len(arrived) != 0):
		in_process = arrived[0];
		dec = Pros[in_process].time_reduce(time_slice,time)
		TotalTime-dec;
		time=time+dec;
		
	if(QUEUE == 0):
		print("\n************\nNO Processes waiting\n************");
		break;
	

for j in range(N):
	Pros[j].T_A_T();
	Pros[j].W_T_A_T();
	
display_processes(Pros,N);	

	

		
