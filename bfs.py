import sys
class BFI:
	def __init__(self):
		self.p=self.a=[]
		for i in range(3000):self.a.append(0)
		self.m=self.i=0
	def M(self, d):
		if d=='<' and self.i!=0:self.i-=1
		if d=='>' and self.i!=2999:self.i+=1
	def R(self, n):
		try:
			with open(n,'r') as f:
				self.p=filter(lambda x:x in['>','<','+','-','.',',',']','['],list(f.read()))
				self.p.append('E')
		except:
			exit()
	def I(self):
		if self.a[self.i]<=127:self.a[self.i]+=1
	def D(self):
		if self.a[self.i]>0:self.a[self.i]-=1
	def B(self):
		z=0
		while 1:
			self.m-=1
			if self.p[self.m]==']':z+=1
			if self.p[self.m]=='[' and z!=0:z-=1
			if self.p[self.m]=='[' and z==0:break
	def F(self):
		z=0
                while 1:
                        self.m+=1
                        if self.p[self.m]=='[':z+=1
                        if self.p[self.m]==']' and z!=0:z-=1
                        if self.p[self.m]==']' and z==0:break
	def P(self):sys.stdout.write(chr(self.a[self.i]))
	def q(self):self.a[self.i]=ord(sys.stdin.read(1)[0])
if __name__ == '__main__':
	h = BFI()
	h.R(sys.argv[1])
	while h.p[h.m] != 'E':
		d=h.p[h.m]
		if d in ['>','<']:h.M(d)
		elif d=='+':h.I()
		elif d=='-':h.D() 
		elif d=='.':h.P()
		elif d==',':h.q()
		if d=='[' and h.a[h.i]==0:h.F()
		if d==']' and h.a[h.i]!=0:h.B()	
		h.m+=1
