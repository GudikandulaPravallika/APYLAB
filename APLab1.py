x=set(input("enter any sentence:"))
v="aeiou"
c=0
for i in x:
    if i.lower() in v:
        c+=1
if c==5:
    print("All vowels are present in the sentence")
else:
    print("Not all vowels are present in the sentence")
    