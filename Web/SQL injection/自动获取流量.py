import re

# 读取刚才导出的文件
with open('result.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

flag_map = {}

# 遍历每一行，寻找匹配的模式
for i in range(len(lines)):
    # 匹配 SQL 语句中的位置和 ASCII 码值
    # 例子: SELECT (ASCII(SUBSTR((...flag),1,1))=102)
    query_match = re.search(r"SUBSTR\(.*?,(\d+),1\)\)=(\d+)", lines[i])
    
    if query_match:
        pos = int(query_match.group(1)) # 获取位置
        ascii_val = int(query_match.group(2)) # 获取猜测的 ASCII 码
        
        # 检查下一行（结果行）是不是 '1' (代表猜对了)
        if i + 1 < len(lines) and lines[i+1].strip() == '1':
            flag_map[pos] = chr(ascii_val)

# 按位置排序并输出
flag = "".join([flag_map[i] for i in sorted(flag_map.keys())])
print(f"提取到的 Flag: {flag}")