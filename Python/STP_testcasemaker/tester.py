import io
import os
import sys
os.makedirs("./answer",exist_ok=True)
judge=[]
for ans_file_num in range(10):
    #入出力のポインタを取得
    input_file=open(f"./testcase/{ans_file_num:04}_in.txt","r")
    output_file=open(f"./answer/{ans_file_num:04}_ans.txt","w")
    sys.stdin=input_file
    sys.stdout=output_file
    with open("submission2.py","r")as f:
        exec(f.read())
    input_file.close()
    output_file.close()

    with open(f"./answer/{ans_file_num:04}_ans.txt","r")as f1:
        with open(f"./testcase/{ans_file_num:04}_out.txt","r")as f2:
            ans=f1.readlines()
            fans=[out[:-1] for out in ans if len(out)>1 and out[0]!="#"]
            inp=f2.readlines()
            finp=[out[:-1] for out in inp if len(out)>1]

            sys.stdout=sys.__stdout__
    
            print(len(fans),len(finp))

            if len(fans)!=len(finp):
                judge.append("WA")
                continue
            for fan,fin in zip(fans,finp):
                if fan!=fin:
                    judge.append("WA")
                    break
            else:
                judge.append("AC")
            
     
sys.stdout=sys.__stdout__
print(judge)
            


