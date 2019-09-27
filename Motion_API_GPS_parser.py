USER_1 = '../data/text_files/'
USER_2 = '../data_2/text_files/'
USER_3 = '../data_3/text_files/'

def bagMotionParser(client):
    json_body = []
    f = open(USER_1+'Bag_Motion.txt', 'r')
    
    for line in f:
        ti, acX, acY, acZ, gyX, gyY, gyZ, mgX, mgY, mgZ, oriW, oriX, oriY, oriZ, gX, gY, gZ, linX, linY, linZ, pre, alt, temp = line.split(' ')
        