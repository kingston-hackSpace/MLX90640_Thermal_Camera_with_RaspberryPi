import time
import datetime
import board
import busio
import os
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
import cv2

#set-up sensor
i2c = busio.I2C(board.SCL, board.SDA)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ  # Set to a feasible refresh rate

#create a folder for videos
video_folder = "videos"
os.makedirs(video_folder, exit_ok=True)

#video filename
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
video_path = os.path.join(video_folder, f"thermal_{timestamp}.avi")
fps = 2
width, height = 32, 24
scale = 20
frame_size = (width * scale, height * scale)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out =cv2.VideoWriter(video_path, fourcc, fps, frame_size)

frame = np.zeros((24*32,), dtype=np.float32)

print(f"Recording video to: {video_path}")

#main loop
try:
    while True:
            #read frame
            mlx.getFrame(frame)#read sensor
            new_frame = frame.reshape((24, 32))
            
            #smooth image for faster view
            smoothed_frame = alpha * new_frame + (1 - alpha) * previous_frame
            previous_frame = smoothed_frame.copy()
            
            #normalize
            norm = cv2.normalize(smoothed, None, 0, 255, cv2.NORM_MINMAX)
            norm = np.uint8(norm)
            coloured = cv2.applyColorMap(cv2.resize(norm,frame_size), cv2.COLORMAP_INFERNO)
            
            #write video
            cv2.imshow("Thermal Camera", coloured)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        except Exception as e:
                print(f"Frame error {e}")
                time.sleep(0.1)
            
    
except KeyboardInterrup:
    print("stopping...")

finally:
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved to {video_path}")
                
