
# _*_ coding:utf-8 _*_

from test import RedisBase


obj = RedisBase()
redis_sub = obj.subscribe_msg()

while True:
	msga = redis_sub.parse_response()
	for msg in msga:
		msg.decode('utf8')
		print('msg: %s' % msg.decode('utf8'))
