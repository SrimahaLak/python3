import logging
logging.basicConfig(filename='E:\\python 3\\python3\\log_file.log',filemode='w',level=logging.DEBUG
,format='TIME:%(asctime)s - LEVEL_NAME:%(levelname)s -MESSAGE-%(message)s - LINE_NO: %(lineno)d')

print("enter the log level 1.DEBUG 2.INFO 3.WARNING 4.ERROR 5.CRITICAL")
level_name=input()
print("enter the log message to display")
msg=input()

validate={"DEBUG":logging.DEBUG,"INFO":logging.INFO,"WARNING":logging.WARNING,"ERROR":logging.ERROR,
          "CRITICAL":logging.CRITICAL}


if not level_name in validate:
    print("Invalid Log level")
    exit()

else:
    level=validate[level_name]
    logging.log(level,msg)

#%(lineno)d: The line number where the logging call was made.

