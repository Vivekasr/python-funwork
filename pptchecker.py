devices = ['keyboard','mouse','trackballs','scanner','barcode reader','digital camera','joystick','microphone','webcam','touchpad','stylus','touch screen','MIDI keyboard','ocr','omr','micr','monitor','printer','headphone','speakers','plotter','actuator','projector']
start_roll = 1124
ending_roll = 1231
left_roll = [1128,1135,1151,1170,1177,1229]
roll_no = int(input('Your roll no.: '))

rollist=[]
for i in range(start_roll,ending_roll+1):
    rollist.append(i)
newlst = [x for x in rollist if x not in left_roll]
for i, j in enumerate(newlst):
    if j == roll_no:
        c = i%len(devices)
yourproject = devices[c]
print('roll no. ',roll_no,' your project is: ', yourproject)
