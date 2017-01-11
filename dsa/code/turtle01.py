#import turtle as t

#for x in range(6):
# t.circle(50)
# t.circle(80)
# t.circle(100)
# t.right(6)

#for x in range(4):
#  t.forward(100)
# t.left(90)

#for x in range(4):
#  t.right(90)
#  t.forward(100)

data = [4,3 ,1 ,2 ,5]

def InsertionSort(A):
    for j in range (1 len(A)):
        key = A(j)
        i = j - 1
        while i > 0 and A[i] > key:
            A[i] = A[j]
            i = i - 1
            A[i+1] = key

print("Insetion Sort")
print("Input", data)
InserttionSort(data)
priint("Output", data)

        
