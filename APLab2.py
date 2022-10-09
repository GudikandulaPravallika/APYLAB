def possible_words(lt1,lt2):
    for i in lt1:
        c=0
        l=list(set(i.upper()))
        for x in l:
            if x in lt2:
                c+=1
            if c==len(i):
                print(i)
lt1=["Arun","Varun","Kent","Eat","Pot","Net","Peak","Peacock","Zebra","Nato","Toe","Poke", "Knife", "poet", "Venus", "Ant"]
lt2=["A",'K','E','P',"T",'N',"O"]
possible_words(lt1,lt2)