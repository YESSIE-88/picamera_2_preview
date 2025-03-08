from picamera2 import Picamera2, Preview
import time

# Initialize the camera
picam2 = Picamera2()

# Configure camera resolution and preview size
camera_config = picam2.create_preview_configuration(main={"size": (1920, 1080)})
picam2.configure(camera_config)

# Start the camera preview with hardware acceleration
picam2.start_preview(Preview.QTGL)  # Uses Qt OpenGL for HW acceleration
picam2.start()

try:
    while True:
        time.sleep(1)  # Keep running while preview is active
except KeyboardInterrupt:
    print("\nStopping camera preview...")
    picam2.stop_preview()
    picam2.close()
