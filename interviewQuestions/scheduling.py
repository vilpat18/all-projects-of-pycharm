import schedule
import time

def greet():
    print('hello patil how are you')


schedule.every(1).minutes.do(greet)


while True:
    schedule.run_pending()
    time.sleep(1)