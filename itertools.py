import itertools
 
def is_subset(B, A_len,A):
    out = False
    
    Subset_list = list(itertools.combinations(B, A_len))
    for subset in Subset_list :
        if subset == A:
            out = True
        else :
            out = False
    
    return out
    
if __name__=='__main__':
    count = int(input())
    for c in range(count):
        A_len=int(input())
        A_str=input()
        A_A=list(A_str.split(" "))
        A_lst=[]
        for i in A_A:
            A_lst.append(int(i))
        A=set(A_lst)
        B_len=int(input())
        B_str=input()
        B_B=list(B_str.split(" "))  
        B_lst=[]
        for j in B_B:
            B_lst.append(int(j))
        B=set(B_lst)          
        print(is_subset(B,A_len,A))
