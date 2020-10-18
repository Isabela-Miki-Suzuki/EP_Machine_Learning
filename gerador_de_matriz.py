import math
def main():
	numLin = 64
	numCol = 3
	for i in range(numLin):
		for j in range(numCol):

#			if i==j:
#				print(2,end=" ")
#			if abs(i-j)==1:
#				print(1,end=" ")
#			if abs(i-j) > 1:
#				print(0,end=" ")

#			if abs(i-j)<=4:
#				print(1./(i+1+j+1-1.), end=" ")
#			else:
#				print(0, end=" ")
			
			if j==0:
				print(1, end=" ")
			if j==1:
				print(i+1, end=" ")
			if j==2:
				print(2*(i+1)-1)
		#print("")
if __name__ == "__main__":
    main()