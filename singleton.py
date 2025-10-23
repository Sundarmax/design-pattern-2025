import threading

class LazySingleton:
    _instance = None

    def __init__(self):
        if LazySingleton._instance is not None:
            raise Exception("Use get_instance() instead")

    @staticmethod
    def get_instance():
        if LazySingleton._instance is None:
            LazySingleton._instance = LazySingleton()
        return  LazySingleton._instance


class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ThreadSafeSingleton._instance is not None:
            raise  Exception("Use get_instance() method")

    @staticmethod
    def get_instance():
        with ThreadSafeSingleton._lock:
            if ThreadSafeSingleton._instance is not None:
                ThreadSafeSingleton._instance = ThreadSafeSingleton()
            return ThreadSafeSingleton._instance

class EagerSingleton:
    '''
    It is one of the simplest and inheritly thread-safe without needing explicit synchronization.

    '''
    _instance = None

    def __init__(self):
        if EagerSingleton._instance is not None:
            raise Exception("use get_instance method")

    @staticmethod
    def get_instance():
        return  EagerSingleton.get_instance()


# singleton1 = LazySingleton.get_instance()
# singleton2 = LazySingleton.get_instance()
#
# print(singleton1 is singleton2)
#
# try:
#     new_ins = LazySingleton()
# except Exception as e:
#     print(e)

# multi threading
#
# def get_singleton_instance():
#     instance = ThreadSafeSingleton.get_instance()
#     print(f"Instance ID from thread {threading.current_thread().name}: {id(instance)}")
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=get_singleton_instance, name=f"Thread - {i+1}")
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
