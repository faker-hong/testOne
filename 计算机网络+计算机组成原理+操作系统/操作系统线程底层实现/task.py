import threading
import uuid


class Task:

    def __init__(self, func, *args, **kwargs):
        # 任务具体的逻辑，通过函数引用传递进来
        self.callable = func
        self.id = uuid.uuid4()
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return "Task Id = " + str(self.id)


class AsyncTask(Task):
    def __init__(self, func, *args, **kwargs):
        self.result = None
        self.condition = threading.Condition()
        super().__init__(func, *args, **kwargs)

    # 设置运行结果
    def set_result(self, result):
        self.condition.acquire()
        self.result = result
        self.condition.notify()
        self.condition.release()

    # 获取任务结果
    def get_result(self):
        self.condition.acquire()
        if not self.result:
            self.condition.wait()
        result = self.result
        self.condition.release()
        return result


def my_func():
    print("this is a task test.")


if __name__ == '__main__':
    task = Task(func=my_func)
    print(task)