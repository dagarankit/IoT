phone_no=['+917641816981','+918132973620']


for i in range(len(phone_no)):
    print('AT+CMGS="{}"'.format(phone_no[i]))
