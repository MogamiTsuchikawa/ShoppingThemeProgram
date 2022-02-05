using System;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static List<Item> items = new List<Item>();
    static void Main(string[] args)
    {
        while (true)
        {
            Console.Write("STP>");
            string cmd = Console.ReadLine();
            string[] cmds = cmd.Split(' ');
            switch (cmds[0])
            {
                case "exit":
                    return;
                case "add":
                    AddItem(cmds);
                    break;
                case "show":
                    for (int i = 0; i < items.Count; i++)
                    {
                        Console.WriteLine($"{i}:{items[i].GetIntroTxt()}円");
                    }
                    break;
                case "buy":
                    int targetIndex = int.Parse(cmds[1]);
                    Console.WriteLine($"{items[targetIndex]}を1個購入しました");
                    items[targetIndex].Buy();
                    break;
                case "checkout":
                    Checkout();
                    break;
            }
        }
    }
    static void AddItem(string[] cmds)
    {
        string name = cmds[1];
        int value = int.Parse(cmds[2]);
        Item newItem = new Item(name, value);
        items.Add(newItem);
        Console.WriteLine($"{value}円の{name}を登録しました");
    }
    static void Checkout()
    {
        for (int i = 0; i < items.Count; i++)
        {
            Console.WriteLine($"{items[i]} {items[i].value}円 × {items[i].count}");
        }
        Console.WriteLine($"合計金額:{Item.GetSum(items)}円");
    }
}

class Item
{
    public string name;
    public int value;
    public int count = 0;
    public Item(string name, int value)
    {
        this.name = name;
        this.value = value;
    }
    // 購入数countの値を一つ増やすメソッド
    public void Buy()
    {
        count++;
    }
    // 一つの値段×個数を計算するメソッド。クラス外では利用しないのでprivate
    private int GetAmountOfMoney()
    {
        return value * count;
    }
    // 合計値を計算するメソッド
    public static int GetSum(List<Item> items)
    {
        int sum = 0;
        foreach (Item item in items)
        {
            sum += item.GetAmountOfMoney();
        }
        return sum;
    }
    // 商品名:商品値段　の文字を返すメソッド
    public string GetIntroTxt()
    {
        return $"{name}:{value}円";
    }
}