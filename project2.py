
from collections import defaultdict
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import math


n=int(8)

def dfs (node,seen,matrix):
        seen[node]=True
        
        for i in range(n):
            if matrix[node][i]==1:
                if not seen[i]:
                    dfs(i,seen,matrix)



#network
class network:
         
    def connection_check(self,matrix):
        seen=[False for i in range(n) ]
        flag=True
        
        dfs(0,seen,matrix)    
        
        for ele in seen:
            if not ele:
                flag=False
        
        return flag


                                   
        
    #print(matrix)

#network reliability

class network_reliability:
    
    def cal_reliability(self,reliable_link,edge_reliable,matrix):
        nw_rel=0
        for i in range(256):
            nw=network()
            
            state=format(i, '08b')
            #state='00010011'
            
            for j in range(8):
               # print("in loop")
                if state[j]=='1':
                   # print("------",state,j,edge_reliable[j,0],edge_reliable[j,1])
                    matrix[int(edge_reliable[j,0])][int(edge_reliable[j,1])]=0
                    matrix[int(edge_reliable[j,1])][int(edge_reliable[j,0])]=0
                    #print("connnection check-----",nw.connection_check1(matrix,j))
                 #nw.connection_check(matrix)
                
            if nw.connection_check(matrix):
                #nw_rel+=self.state_reliability(matrix,edge_reliable)
                nw_rel+=self.state_reliability(state,reliable_link)
                # print(nw_rel,i)
        return nw_rel
    
    def state_reliability(self,state,link_reliable):
        val=1
        
        
        # for i in range(8):
        #     for j in range(8):
        #         edge_val=0
                
        #         if j>i :
        #             # for row in edge_reliable:
        #             #     if i==row[0] and j==row[1]:
        #             #         edge_val=row[2]
                            
        #             if adj_matrix[i][j]==1:
        #                 val*=link_reliable
        #             else:
        #                 val*=(1-link_reliable)  
                    
        for j in range(8):
            if state[j]==1:
                val*=(1-p)
            else:
                val*=p
        return val
            
if __name__ == "__main__":
    edges=15
    p=0.05
   # graph_nodes=[1,2,3,4,5,6,7,8]
   #adj matrix based on network topology          
    edge_reliable=np.zeros([15,3],dtype=float)
   #s print(edge_val)
    
   # link_reliable=np.zeros([15],dtype=float)
    link_r=p
    nw_reliable=network_reliability()
    
    res=[]
    p_vals=[]
    
    for itr in range(20):
        matrix=[[0,1,1,0,1,0,1,0],
           [1,0,1,0,0,1,0,0],
           [1,1,0,1,1,0,0,0],
           [0,0,1,0,0,1,1,0],
           [1,0,1,0,0,1,0,1],
           [0,1,0,1,1,0,1,1],
           [1,0,0,1,0,1,0,1],
           [0,0,0,0,1,1,1,0]
           ]
        #edge_val=random.sample(range(0, 15), 15)
        #print(edge_val)
       # for i in range(edges):
            #p_val=edge_val[i]/3
            #=int(math.ceil(p))
        #    link_reliable[i]=p
            #float(math.pow(p,x))
           # print(p_val,x)
       
       # print(link_reliable)   
        idx=0
        # for i in range(8):
        #     for j in range(8):            
        #         if j>i and matrix[i][j]==1:
        #            # print(i,j)
        #             edge_reliable[idx][0]=i
        #             edge_reliable[idx][1]=j
        #             edge_reliable[idx][2]=link_reliable[idx]
        #            # print("wallll",edge_reliable[idx][0],edge_reliable[idx][1],edge_reliable[idx][2])
        #             idx+=1
        #print(edge_reliable)
        #print("netrel=",nw_reliable.cal_reliability(link_reliable,edge_reliable,matrix))     
        #res.append(nw_reliable.cal_reliability(link_reliable,edge_reliable,matrix))
        
        res.append(nw_reliable.cal_reliability(link_r,edge_reliable,matrix))
        p_vals.append(p)
        
        print( "p_value=" + str(p_vals[itr])+", network reliability=" + str(res[itr]))
        
        p+=0.05 
        p=round(p,2)
        #print(p)     
   
  #  print(edge_reliable)  
    fig, ax = plt.subplots()
    ax.plot(p_vals,res)
   # ax.set_xlabel=("lr(p)")
    plt.xlabel("lr(p)")
    plt.ylabel("nr")
    plt.show()
    