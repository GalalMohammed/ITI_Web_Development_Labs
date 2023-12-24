import json


class Queue:

    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def pop(self):
        if self.queue:
            front = self.queue[0]
            del self.queue[0]
            return front
        else:
            print("The queue is empty.")

    def is_empty(self):
        return len(self.queue) == 0


class QueueOutOfRange(Exception):
    pass


class QueuePro(Queue):

    __queues = {}

    def __init__(self, name, size, *args, **kwargs):
        self.name = name
        self.size = size
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            super().__init__()
            QueuePro.__queues[name] = self

    def insert(self, value):
        if len(self.queue) < self.size:
            super().insert(value)
        else:
            raise QueueOutOfRange()

    @classmethod
    def get_queue(cls, name):
        return cls.__queues.get(name)

    @classmethod
    def save(cls):
        QueuePro.load()
        with open("queue.json", 'w') as file:
            file.write(json.dumps(dict([(k, obj.__dict__) for k, obj in cls.__queues.items()])))

    @classmethod
    def load(cls):
        try:
            with open("queue.json") as file:
                dict_dict = json.loads(file.read())
        except FileNotFoundError:
            dict_dict = {}
        for k, v in dict_dict.copy().items():
            cls.__queues[k] = cls(**v)
