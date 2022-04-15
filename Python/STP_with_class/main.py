class Item:
    def __init__(self,name,value):
        self.name=name
        self.value=value
        self.count=0
    
    def Buy(self):
        self.count+=1
    
    def GetAmountOfMoney(self):
        return self.value*self.count

    def GetIntroTxt(self):
        return f"{self.name}:{self.value}円"

def GetSum():
    total=0
    for item in items:
        total+=item.GetAmountOfMoney()
    return total

def AddItem(cmds):
    name=cmds[1]
    value=int(cmds[2])
    newItem=Item(name,value)
    items.append(newItem)
    print(f"{value}円の{name}を登録しました")

def CheckOut():
    for item in items:
        print(item.GetIntroTxt()+f"*{item.count}")
    print(f"合計金額:{GetSum()}円")

items=[]

while True:
    cmd=input("STP>")
    cmds=cmd.split(" ")
    if cmds[0]=="exit":
        break
    elif cmds[0]=="add":
        AddItem(cmds)
    elif cmds[0]=="show":
        for i,item in enumerate(items):
            print(f"{i}:{item.GetIntroTxt()}")
    elif cmds[0]=="buy":
        targetindex=int(cmds[1])
        print(f"{items[targetindex].name}を一個購入しました")
        items[targetindex].Buy()
    elif "checkout":
        CheckOut()