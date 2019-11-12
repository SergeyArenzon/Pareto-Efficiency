
'''
Sergey Arenzon
321211286
    
    Faild to print the way you asked, but the result is equal.
    
'''



import cvxpy
from cvxpy import log

def pareto(mat):
    
    for k in range(len(mat[0])):
        val = []    
        res = []
        for i in range(len(mat)):
            temp = 0        

            for j in range(len(mat[0])):            
                if(j==k):
                    r = cvxpy.Variable()
                    res.append(r)
                    temp += r*mat[i][j]
                else:
                    temp += mat[i][j]


            val.append(log(temp))

        obj = 0
        for i in val:
            obj += i   
        obj = cvxpy.Maximize(obj)


        cons = []
        temp_cons = 0

        for i in res:
            cons.append(0<=i)
            cons.append(i<=1)
            temp_cons += i

        cons.append(temp_cons == 1)    
        prob = cvxpy.Problem(obj,cons)
        prob.solve()





        count = 0
        for i in res:
            print("Agent#{} gets {} of resource# {}".format(count,i.value,k))
            count += 1



mat = [[19, 0, 0, 81],
        [0, 20, 0, 80],
        [0, 0, 40, 60]]
      


pareto(mat)

