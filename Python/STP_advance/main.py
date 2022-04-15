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

class Cart:
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
            return "3つ目には価格を入れてください"
        if cmds[1] in self.item_names:
            return "既にその名前のアイテムが存在します"
        name=cmds[1]
        value=int(cmds[2])
        newItem=Item(name,value)
        self.item_names.append(name)
        self.items.append(newItem)
        return f"{value}円の{name}を登録しました"

    def CheckOut(self):
        for item in self.items:
            print(item.GetIntroTxt()+f"*{item.count}")
        return f"合計金額:{self.GetSum()}円"
    
    def Show(self):
        if len(self.items)==0:
            return "まだ何も登録していません"
        ret=""
        for i,item in enumerate(self.items):
            ret+= f"{i}:{item.GetIntroTxt()}\n"
        return ret

    def Buy(self,cmd):
        targetitem=self.SearchItem(cmd[1])
        if targetitem==-1:
            return "アイテムが見つかりませんでした"
        targetitem.Buy()
        return f"{targetitem.name}を一個購入しました"

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

            

def print_help():
    print("exit:このプログラムを終了する")
    print("add [name] [value]:新たな商品nameをvalue円で登録する")
    print("show:今までに登録した賞品の一覧を出力")
    print("buy [name/index]:指定した商品を購入、該当しない場合は何も起こらない")
    print("checkout:今まで購入した商品で会計を行い、合計金額などを出力")



mycart=Cart()
while True:
    cmd=input("STP>")
    cmds=cmd.split(" ")
    if cmds[0]=="exit":
        break
    elif cmds[0]=="help":
        print_help()
    elif cmds[0]=="add":
        print(mycart.AddItem(cmds))
    elif cmds[0]=="show":
        print(mycart.Show())
    elif cmds[0]=="buy":
        print(mycart.Buy(cmds))
    elif cmds[0]=="checkout":
        print(mycart.CheckOut())
    else:
        print("有効なコマンドを指定してください")
        print("コマンド一覧はhelpで確認できます")