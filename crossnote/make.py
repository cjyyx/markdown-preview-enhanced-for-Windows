import os

print("开始编译")
os.system("pkg . -t=node18-win-x64 --out-path=.")

print("开始测试")

def test(cmd):
    print("测试命令：", cmd)
    os.system(cmd)

test("crossnote.exe -h")
test("crossnote.exe README.md")
test("crossnote.exe README.md --open_in_brower")
test("crossnote.exe README.md --output_html D:\\test.html")