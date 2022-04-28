import datetime

class SecondHandler():
    def is_now_even(self):
        now = datetime.datetime.now().second

        if now % 2 == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    second_handler = SecondHandler()
    print(second_handler.is_now_even())