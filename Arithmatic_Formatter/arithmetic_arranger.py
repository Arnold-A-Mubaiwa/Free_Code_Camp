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
        print()
    
def the_big_length(value,indx=3):
    big = 0
    for x in range(indx):
        for i in value:
            if len(i[x])>big:
                big=len(i[x])
        return big

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49444", "123 + 49444", "123 + 49444", "123 + 49444", "123 + 49444"])