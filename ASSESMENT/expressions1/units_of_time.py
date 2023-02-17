def units_of_time():
    seconds = int(input())
    sec = seconds%60
    minutes = (seconds%3600)//60
    hrs = (seconds % 86400) // 3600
    days = (seconds % 2592000) // 86400
    print("{0:0=2d}".format(days), ":", "{0:0=2d}".format(hrs), ":", "{0:0=2d}".format(minutes), ":", "{0:0=2d}".format(sec))

units_of_time()