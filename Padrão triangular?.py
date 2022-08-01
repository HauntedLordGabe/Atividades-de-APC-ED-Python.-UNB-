s1, s2, s3 = input().split()
var1 = f'{s1+s2}  '*4
var2 = f'{s1}{s3}{s3}{s2}'*4

def parte1(): 
   for i in range(4):
       print(f' {var1}  \n{var2}')
parte1()
