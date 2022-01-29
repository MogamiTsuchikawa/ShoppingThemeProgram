using System;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        List<string> items = new List<string>();
        List<int> itemValues = new List<int>();
        List<int> itemCounts = new List<int>();
        while(true)
        {
            Console.Write("STP>");
            string cmd = Console.ReadLine();
            string[] cmds = cmd.Split(' ');
            switch(cmds[0])
            {
                case "exit":
                    return;
                case "add":
                    string name = cmds[1];
                    int value = int.Parse(cmds[2]);
                    items.Add(name);
                    itemValues.Add(value);
                    itemCounts.Add(0);
                    Console.WriteLine($"{value}円の{name}を登録しました");
                    break;
                case "show":
                    for (int i = 0; i < items.Count; i++)
                    {
                        Console.WriteLine($"{i}:{items[i]}:{itemValues[i]}円");
                    }
                    break;
                case "buy":
                    int targetIndex = int.Parse(cmds[1]);
                    Console.WriteLine($"{items[targetIndex]}を1個購入しました");
                    itemCounts[targetIndex]++;
                    break;
                case "checkout":
                    int sum = 0;
                    for (int i = 0; i < items.Count; i++)
                    {
                        sum += itemValues[i] * itemCounts[i];
                        Console.WriteLine($"{items[i]} {itemValues[i]}円 × {itemCounts[i]}");
                        itemCounts[i] = 0;
                    }
                    Console.WriteLine($"合計金額:{sum}円");
                    break;
            }
        }
    }
}