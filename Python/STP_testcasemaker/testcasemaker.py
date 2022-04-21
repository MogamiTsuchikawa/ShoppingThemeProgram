import os
import random

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
        return f"{self.name} {self.value}yen"

class Cart:
    def __len__(self):
        return len(self.items)
    def __init__(self):
        self.items=[]
        self.item_names=[]
        
    def GetSum(self):
        total=0
        for item in self.items:
            total+=item.GetAmountOfMoney()
        return total

    def AddItem(self,cmds):
        if not cmds[2].isdecimal():
            return "include the price in third argument"
        if cmds[1] in self.item_names:
            return "item with that name already exists"
        name=cmds[1]
        value=int(cmds[2])
        newItem=Item(name,value)
        self.item_names.append(name)
        self.items.append(newItem)
        return f"added!:{name} {value}"

    def CheckOut(self):
        ret=""
        for i,item in enumerate(self.items):
            ret+=f"{i}:{item.GetIntroTxt()}*{item.count}\n"
        ret+=f"total:{self.GetSum()}yen"
        for item in self.items:
            item.count=0
        return ret
    
    def Show(self):
        if len(self.items)==0:
            return "item list is empty"
        ret=""
        for i,item in enumerate(self.items):
            ret+= f"{i}:{item.GetIntroTxt()}\n"
        return ret

    def Buy(self,cmd):
        targetitem=self.SearchItem(cmd[1])
        if targetitem==-1:
            return "item not found"
        targetitem.Buy()
        return f"bought one {targetitem.name}"

    def SearchItem(self,cmd):
        for item in self.items:
            if item.name==cmd:
                return item
        if cmd.isdecimal():
            index=int(cmd)
            if 0<=index<len(self.items):
                return self.items[index]
            else:
                return -1
        return -1


item_name_box=[
    "Python",
    "C",
    "CSharp",
    "CPlusPlus",
    "D",
    "Swift",
    "Kotlin",
    "FORTRAN",
    "Ruby",
    "Rust",
    "Go",
    "Haskell",
    "Java",
    "JavaScript",
    "Perl",
    "PHP",
    "Scratch",
    "TypeScript"
]




def GetNewItem():
    newitem=random.randrange(len(item_name_box))
    number=str(cnt[newitem])
    if number=="1":number=""
    cnt[newitem]+=1
    return item_name_box[newitem]+number

os.makedirs("./testcase",exist_ok=True)

for SEED in range(50):
    random.seed(SEED)
    cmd=[]
    ans=[]
    cnt=[1]*len(item_name_box)
    first_item_num=random.randrange(len(item_name_box))
    first_item=item_name_box[first_item_num]
    first_item_value=str(random.randint(500,1500))
    cnt[first_item_num]+=1

    mycart=Cart()
    mycart.AddItem([0,first_item,first_item_value])
    cmd.append(f"add {first_item} {first_item_value}")
    i=1
    while i!=998:
        rnd=random.randint(1,10)
        if rnd==1:#add
            item_name=GetNewItem()
            item_value=str(random.randint(500,1500))
            cmd.append(f"add {item_name} {item_value}")
            mycart.AddItem([0,item_name,item_value])
        elif rnd==2:#show
            if cmd[-1]=="show":
                continue
            cmd.append("show")
            ans.append(mycart.Show())
        elif rnd==3:#checkout
            if cmd[-1]=="checkout" or i==998:
                continue
            cmd.append("checkout")
            ans.append(mycart.CheckOut())
        elif 4<=rnd:#buy
            buy_item=str(random.randrange(len(mycart)))
            cmd.append(f"buy {buy_item}")
            mycart.Buy([0,buy_item])
        
        i+=1

    cmd.append("checkout")
    ans.append(mycart.CheckOut())
    cmd.append("exit")


    with open(f"./testcase/{SEED:04}_in.txt","w")as f:
        for i in cmd:
            f.write(i+["\n",""][i[-1]=="\n"])

    with open(f"./testcase/{SEED:04}_out.txt","w")as f:
        for i in ans:
            f.write(i+["\n",""][i[-1]=="\n"])
