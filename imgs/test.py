
# _*_ coding:utf-8 _*_

import redis

class RedisBase(object):

	def __init__(self):
		self._conn = redis.Redis(host='120.77.213.65',password='test')
		self.pub = 'test'
		self.sub = 'test'

	# 发布
	def publish_msg(self, msg):

		self._conn.publish(self.pub, msg)

	# 订阅
	def subscribe_msg(self):

		pub = self._conn.pubsub()

		pub.subscribe(self.pub)
		pub.parse_response()
		return pub

