import os

dir_path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
ddir_path = os.path.dirname(dir_path)

# print(dir_path)
# print(ddir_path)

print("开始测试")

def test(cmd):
    print("测试命令：", cmd)
    os.system(cmd)
    print("")

test(f"node {dir_path}/crossnote.js {ddir_path}/testCase/离散数学复习重点.md")