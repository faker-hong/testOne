import redis
import threading


# 创建连接池
pool = redis.ConnectionPool()
# 初始化
r = redis.StrictRedis(connection_pool=pool)

key = "ticket_count"
def sell(i):
    # redis事务封装在pipeline中
    p = r.pipeline()
    while True:
        try:
            # 监督车票
            p.watch(key)
            # 获取票数
            c = int(p.get(key))
            if c>0:
                # 开启事务
                p.multi()
                c = c-1
                p.set(key, c)
                p.execute()
                print("用户{}抢票成功，还剩{}".format(i, c))
                break
            else:
                print("用户{}抢票失败，无票".format(i))
                break
        except Exception as e:
            print("用户{}抢票失败，请重试".format(i))
            continue
        finally:
            p.unwatch()


if __name__ == '__main__':
    r.set(key, 5)
    for i in range(10):
        t = threading.Thread(target=sell, args=(i,))
        t.start()