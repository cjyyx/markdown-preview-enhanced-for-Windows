import os

dir_path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')

print("开始编译")
os.system("pkg . -t=node18-win-x64 --out-path=./dist")

print("开始测试")

def test(cmd):
    print("测试命令：", cmd)
    os.system(cmd)

test(f"dist\crossnote.exe {dir_path}/testCase/离散数学复习重点.md")
