import time
import datetime
import board
import busio
import os
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt

#set-up sensor
i2c = busio.I2C(board.SCL, board.SDA)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ  # Set to a feasible refresh rate

#set-up plot
plt.ion()
fig, ax = plt.subplots(figsize=(8, 6))
therm1 = ax.imshow(np.zeros((24, 32)), vmin=20, vmax=30, interpolation='bilinear', cmap='inferno')
cbar = fig.colorbar(therm1)
cbar.set_label('Temperature [$^{\circ}$C]', fontsize=14)

#create folder for images
image_folder = "images"
os.makedirs(image_folder, exist_ok=True) #create folder only if it doesnt exist

frame = np.zeros((24*32,), dtype=np.float32)
previous_frame = np.zeros((24, 32), dtype=np.float32)
alpha = 0.9
t_array = []
max_retries = 5
timer = 0
framecount = 0

#main loop
while True:
    t1 = time.monotonic()
    last_exception = None
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            #read frame
            mlx.getFrame(frame)#read sensor
            new_frame = frame.reshape((24, 32))
            
            #smooth image for faster view
            smoothed_frame = alpha * new_frame + (1 - alpha) * previous_frame
            previous_frame = smoothed_frame.copy()
            
            #update image
            therm1.set_data(np.flipud(np.fliplr(smoothed_frame)))
            therm1.set_clim(vmin=np.min(smoothed_frame), vmax=np.max(smoothed_frame))
            fig.canvas.draw()  # Redraw the figure to update the plot and colorbar
            
            ###########################
            #save image
            ###########################
            timer += 1
            if timer >= 10: #save image every 10 frames
                timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                filename = os.path.join(image_folder, f"frame_{timestamp}.png")
                fig.savefig(filename)
                print(f"Saved frame: {filename}")
                framecount += 1;
                timer=0
                
            fig.canvas.flush_events()
            plt.pause(0.001)
            
            #update sample rate
            t_array.append(time.monotonic() - t1)
            print('Sample Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
            break
            
        except (ValueError, RuntimeError) as e:
            last_exception = e
            retry_count += 1
            time.sleep(0.05)
            
    else:
                print(f"Failed after {max_retries} retries with error: {last_exception}")
                
