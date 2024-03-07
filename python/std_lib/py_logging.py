import sys
import os
import logging
from datetime import datetime
import time


LOG_FORMAT = '[%(asctime)s][%(levelname)s: File "%(filename)s", line %(lineno)s in %(funcName)s] %(message)s'

# 함수 안써
logging.basicConfig(
    # stdout으로 스트림 출력
    level=logging.INFO,
    format=LOG_FORMAT,
    # stream=sys.stdout
)
global_logger = logging.getLogger(__name__)

# 추가로 다른 파일로 로그를 출력하려면 파일 핸들러 사용
file_handler = logging.FileHandler(os.getcwd()+"/.log", encoding='utf-8')
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

global_logger.addHandler(file_handler)


# 함수 써
def create_logger(name):
    logger = logging.getLogger(name)
    # log level
    #   NOTSET  : 0
    #   DEBUG   : 10
    #   INFO    : 20
    #   WARNING : 30
    #   ERROR   : 40
    #   CRITICAL: 50
    logger.setLevel(logging.INFO)
    log_dir = os.getcwd()+"/log"

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    formatter = logging.Formatter(
        '[%(asctime)s][%(levelname)s: File "%(filename)s", line %(lineno)s in %(funcName)s] %(message)s'
        '\n'
        '\t%(process)s, %(processName)s / %(thread)s, %(threadName)s / [%(my_param)-10s][%(my_my)+10s]'
    )
    """ example
    [2024-03-07 17:07:29,464][INFO: File "py_logging.py", line 81 in logger_test] in fo m
	120660, MainProcess / 140104093372864, MainThread / [hello     ][       NNn]
    [2024-03-07 17:07:33,537][CRITICAL: File "py_logging.py", line 87 in logger_test] fafa
	120660, MainProcess / 140104093372864, MainThread / [hello     ][       NNn]
    """

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_dir + "/logging_test_" + datetime.now().strftime('%Y%m%d') + '.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


def logger_test():
    logger = create_logger("local_logger")
    print(f"local_logger: {logger}")
    d = {"my_param": "hello", "my_my": "NNn"}

    while 1:
        lv, *msg = input("로깅 입력:").split()
        msg = " ".join(msg)
        if lv == "0":
            break
        elif lv == "1":
            logger.debug(msg, extra=d)
        elif lv == "2":
            logger.info(msg, extra=d)
        elif lv == "3":
            logger.warning(msg, extra=d)
        elif lv == "4":
            logger.error(msg, extra=d)
        elif lv == "5":
            logger.critical(msg, extra=d)

    logger.info("프로그램 종료임", extra=d)


if __name__ == "__main__":
    print(f"global_logeer: {global_logger}")
    start_time = time.time()
    global_logger.info(f"start running at {str(datetime.now())}")

    logger_test()

    end_time = time.time()
    global_logger.info(f"end running at {str(datetime.now())}")
    global_logger.info(f"running time : {end_time-start_time:.05} seconds\n")