import picamera 
import time 

path = '/home/pi/src4/06_multimedia' 

camera = picamera.PiCamera() 

def count_down(n):
    for i in range(n, 0):
        print(i)
        time.sleep(1)

try:
    camera.resolution = (640, 480) 
    camera.start_preview() 
    
    while True:
        selection = input('Photo : 1, Video : 2, Exit : 9 > ')

        if selection == '1':
            count_down(3)
            now_str = time.strftime('%Y%m%d_%H%M%S')

            camera.capture('%s/photo_%s.jpg' % (path, now_str))
            print('Photo has been captured.')

        elif selection == '2': 
            count_down(3)
            print('Recording start.')
            now_str = time.strftime('%Y%m%d_%H%M%S')

            camera.start_recording('%s/video_%s.h264' % (path, now_str))
            input('press enter to stop recording.')
            camera.stop_recording()
            print('Recording stopped.')

        elif selection == '9':
            print('exiting..')
            break

        else:
            print('incorrect command')

finally:
    camera.stop_preview()
