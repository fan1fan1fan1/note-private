# 1.创建数据库和表
import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

# 三个引号 ''' 是 python 的多行字符串。
# cur.execute 执行建表的 SQL 语句。
# 表名是log
cur.execute(''' CREATE TABLE IF NOT EXISTS log ( id INTEGER PRIMARY KEY AUTOINCREMENT, create_time TEXT, content TEXT ) ''')
conn.commit()
conn.close()


# 2.插入单条数据
# ?是占位符
cur.execute ("INSERT INTO log (create_time,content) VALUES (?,?)",("2026‑08‑22","测试第一条记录"))


# 3.批量插入数据
data_list = [ ("2026‑08‑22","日志 A"), ("2026‑08‑22","日志 B"), ("2026‑08‑22","日志 C") ]
cur.executemany ("INSERT INTO log (create_time,content) VALUES (?,?)",data_list)
conn.commit()
conn.close()


# 4.查询所有数据
cur.execute ("SELECT * FROM log")
rows = cur.fetchall()  # 只负责发送查询指令，不会直接把数据拿出来
for r in rows: print (r)
conn.close()


# 5.根据条件查询
# execute要求传参为元组 id 具体数据 所以2后有逗号
cur.execute("SELECT * FROM record WHERE id=?",(2,))
res = cur.fetchall()
print(res)

conn.close()


# 6.更新数据
cur.execute ("UPDATE log SET content=? WHERE id=?",("修改后的内容",1))
conn.commit()
conn.close ()


# 7.删除数据
cur.execute ("DELETE FROM log WHERE id=?",(1,))
conn.commit()
conn.close()


# 8.with 上下文管理，自动提交关闭连接
# with 处理需要 “打开，之后必须关闭” 的资源。 文件、数据库连接都属于这类。
with sqlite3.connect ("test.db") as conn:
    cur = conn.cursor () # 获取游标
    # 打开 test.db 数据库，赋值给 conn 变量。
    cur.execute ("INSERT INTO log (create_time,content) VALUES (?,?)",("2026‑08‑22","with 方式插入"))