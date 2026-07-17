# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
...
# To write a log record:
#logger.log(logging.INFO, "this string would be logged")

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"function: {func.__name__}")
        if args == ():
          logger.info("positional parameters: none")
        else:
          logger.info(f"positional parameters: {list(args)}")
        if kwargs == {}:
          logger.info("keyword parameters: none")
        else:
          logger.info(f"keyword parameters: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"return: {result}")
        return result
    return wrapper
    
@logger_decorator
def func1():
    print ("Hello World!")

func1()

@logger_decorator
def func2(*args):
    return True

func2(5,10,15)

@logger_decorator
def func3(**kwargs):
    return logger_decorator

func3( fruits = "apples", vegetables = "zucchini")


