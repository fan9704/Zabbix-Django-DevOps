import redis
import json
import datetime
rc = redis.Redis(
    host="127.0.0.1",
    password="geekwolf",
    port=6379,
    db=0
    )
msg = {
    "警告主機":"web-server-node-1",
    "警告地址":"192.168.113.11",
    "警告時間":datetime.datetime.now(),
    "警告等級":"嚴重",
    "警告訊息":"Web Port 80 listen",
    "問題詳情":"80 port connect failed",
    "當前狀態":"Problem",
    "事件ID":"12345",
}
rc.publish("alarm",json.dumps(msg))