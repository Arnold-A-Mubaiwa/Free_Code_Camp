def arithmetic_arranger(problems,viewAnswer = False):
    v=[]
    
    for problem in problems:
        v.insert(len(v),problem.split())
    big_v = the_big_length(v)+3
    
    for x in range(3):
        for i in v:
            if x==0:
                print(" "*(big_v-len(i[x])),i[x],end='   ')
            elif x==1:
                continue
            else:
                print(i[x-1]," "*(big_v-len(i[x])-2),i[x],end='   ')
        print("")
        
    for i in v:
        print("-"*(big_v+1), end='   ')
    print()
    
    for i in sum(v):
        if viewAnswer==True:
            print(" "*(big_v-len(str(i))),i,end='   ')
    print()

def the_big_length(value,indx=3):
    big = 0
    for x in range(indx):
        for i in value:
            if len(i[x])>big:
                big=len(i[x])
        return big
    
def sum(value):
    count = []
    for x in range(len(value)):
        for y in value[x]:
            if y=='+':
               count.insert(len(count),(int(value[x][0]))+int(value[x][2]))
            elif y=='-':
               count.insert(len(count),(int(value[x][0]))-int(value[x][2]))
    return count       

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49444", "123 + 49444", "123 + 49444", "123 + 49444"],True)