using System;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        while(true)
        {
            Console.Write("STP>");
            string cmd = Console.ReadLine();
            string[] cmds = cmd.Split(' ');
            switch(cmd)
            {
                case "exit":
                    return;
            }
        }
    }
}