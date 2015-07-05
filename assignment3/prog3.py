#program to print key and values of dictionary ehile iterating over a list

l1=["flask","django","pyramid","spring","rails","cubic web"]
l2=[1,2,3,9,18,'hello']
d={1:"python",2:"java",3:"ruby"}


l1.insert(3,d)
l1.insert(5,l2)
print("List is :",l1)

for x in l1:

    if type(x) == dict:
        print("\n",d.keys())
        print("\n",d.values())