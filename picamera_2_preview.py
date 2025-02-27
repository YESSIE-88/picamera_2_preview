from pprint import *
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
# See each camera mode option (res, fps, color depth etc)
#print('\n\n\n\n\n')
#pprint (pican2. sensor_modes)
#print('\n\n\n\n\n')

camera_config = picam2.create_preview_configuration (main={"size": (2028, 1074)}) # 50 fps, 1920, 1080 preview, with best cam resolution available picam2.configure(camera_config)

picam2.start_preview (Preview.QTGL, width=1920, height=1880)
picam2.start()

time.sleep(86400) #One Day