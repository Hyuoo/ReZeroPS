import sys
import os
import logging
from datetime import datetime


LOG_FORMAT = '[%(asctime)s][%(levelname)s: File "%(filename)s", line %(lineno)s in %(funcName)s] %(message)s'

# # 함수 안써
# logging.basicConfig(
#     # stdout으로 스트림 출력
#     level=logging.INFO,
#     format=LOG_FORMAT,
#     stream=sys.stdout
# )
# logger = logging.getLogger(__name__)
# 
# 추가로 다른 파일로 로그를 출력하려면 파일 핸들러 사용
# file_handler = logging.FileHandler(".log", encoding='utf-8')
# file_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s: File "%(filename)s", line %(lineno)s in %(funcName)s] %(message)s'))
# logger.addHandler(file_handler)

# logger.info(msg)
# logger.debug(msg)
# logger.error(msg)


# 함수 써
def create_logger():
    logger = logging.getLogger(__name__)
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

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_dir + "/logging_test_" + datetime.now().strftime('%Y%m%d') + '.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    print(sys.argv)
    logger = create_logger()
    print(logger)
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
