# Assignment  part-1 9th february submitted by 
# Muhammad arshad PIAIC67442
pi=3.14
def calcArea(r):
    return r*r*pi  
print(calcArea(8.7))


# Assignment  part-2 9th february submitted by 
# Muhammad arshad PIAIC67442
piaic=['python', 'r', 'java', 'pascal', 'c', 'javascript', 'assembley', 'html','c++']

def func1(piaic):
    for i in piaic:
        if i=="python":
            print("the value of python is available")
        elif i=="html":
            print("the value of html is available")
        elif i=="c++":
            print("the value of C++ is available")
        else:
            print(" none of the value is available")
    
func1(piaic)    

# Assignment  part-3 9th february submitted by 
# Muhammad arshad PIAIC67442
data = ["python", "r", "java", "pascal", "c", "javascript", "assembley", "html", "c++"]
rotate_num = 2
def rightRotate(data, num): 
    output_data = [] 
      
    # Will add values from n to the new list 
    for item in range(len(data) - num, len(data)): 
        output_data.append(data[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, len(data) - num):  
        output_data.append(data[item]) 
          
    return output_data 

print(rightRotate(data, rotate_num)) 
  
# Assignment  part-4 9th february submitted by 
# Muhammad arshad PIAIC67442
from math import pi
while True:
    r= input('please enter an integer( 0 to exit):\n')
    r=float(r)
    if r==0:
        print("loop is breaked or exited")
        break
    print("the arae of the circle is ",str(pi*r**2))

# Assignment  part-5 9th february submitted by 
# Muhammad arshad PIAIC67442
def print_showdetails(args,*kwargs):
    print("hello Ali \n","Here is your result for class of AI\n","Your score card is as follows")
    for k, v in kwargs.items():
        print(f'{k} : {v}')
    print("the total marks are")
    print(sum(kwargs.values()))
   
print_showdetails(math = 50, physics = 80, biology= 90, computer =67)
