import pymysql
import redis
import sys


def con_mysql(sql):
	db = pymysql.connect(host='127.0.0.1',
		user='root',
		passwd='123456',
		port=3306,
		db='hr',
		charset='utf8')
	cursor = db.cursor()
	cursor.execute(sql)
	data = cursor.fetchall()
	return data

def con_redis(name, passwd):
	r = redis.Redis(host='120.77.213.65',password='test')
	r_name = r.hget('user', 'name')
	r_passwd = r.hget('user', 'passwd')
	print(type(name))
	print(type(r_name))
	print(type(r_passwd))
	r_name = r_name.decode('utf8')
	r_passwd = r_passwd.decode('utf8')
	print(type(name))
	print(type(r_name))
	if name==r_name and passwd == r_passwd:
		return True, '登录成功'
	else:
		return False, '登录失败'
	
	
	

if __name__ == '__main__':
	name = sys.argv[1]
	passwd = sys.argv[2]
	print(con_mysql('select * from user'))
	print(name)
	print(passwd)
	result = con_redis(name, passwd)
	if not result[0]:
		# 查询mysql数据库
		sql = '''select * from user where name="%s" and passwd="%s" ''' % (name, passwd)
		print(sql)
		data = con_mysql(sql)
		print(data)
		if data:
			r = redis.Redis(host='120.77.213.65',password='test')
			r.hset('user', 'name', name)
			r.hset('user', 'passwd', passwd)
			print( '刷新redis,登录成功')
		else:
			print('用户名和密码错误')
	else:
		print('redis中数据正确,登录成功')