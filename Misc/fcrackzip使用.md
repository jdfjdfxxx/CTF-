-----------------fcrackzip（简单zip）
破解4-6位纯数字密码
fcrackzip -b -c 1 -l 4-6 -u flag.zip
#-b: 暴力破解模式。
#-c 1: 指定字符集为数字 (1代表数字，a代表小写字母，A代表大写字母，!代表特殊符号)。
#-l 4-6: 指定密码长度为 4 到 6 位。
#-u: 尝试解压并排除掉错误的密码

破解小写字母与数字混合密码
fcrackzip -b -c a1 -l 1-4 -u flag.zip

使用字典rockyou.txt
fcrackzip -D -p /usr/share/wordlists/rockyou.txt -u flag.zip



-----------------john（破加密）
1提取哈希 (X2john)
根据压缩包类型选择对应的提取工具（Kali 自带）：
ZIP: zip2john flag.zip > hash.txt
RAR: rar2john flag.rar > hash.txt
7z: 7z2john.pl flag.7z > hash.txt

2拿到hash开始破解
john hash.txt   或者使用字典 ：john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

3成功后查看密码
john --show hash.txt


