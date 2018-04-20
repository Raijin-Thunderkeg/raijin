
# _*_ coding:utf-8 _*_

from test import RedisBase

obj = RedisBase()
msg = 'hello world'
obj.publish_msg(msg)
