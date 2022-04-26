import datetime

def is_now_even():
    now = datetime.datetime.now().second

    if now % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_now_even())