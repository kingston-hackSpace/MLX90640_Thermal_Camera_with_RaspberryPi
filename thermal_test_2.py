import time
import board
import busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt

#set-up sensor
i2c = busio.I2C(board.SCL, board.SDA)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ  # Set to a feasible refresh rate
time.sleep(0.5)

#set-up plot
plt.ion()
fig, ax = plt.subplots(figsize=(8, 6))
therm1 = ax.imshow(np.zeros((24, 32)), vmin=20, vmax=30, interpolation='bilinear', cmap='inferno')
cbar = fig.colorbar(therm1)
cbar.set_label('Temperature [$^{\circ}$C]', fontsize=12)

frame = np.zeros((24*32,), dtype=np.float32)
previous_frame = np.zeros((24, 32), dtype=np.float32)
alpha = 0.9
t_array = []
max_retries = 5

#main loop
while True:
    t1 = time.monotonic()
    last_exception = None
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            #read frame
            mlx.getFrame(frame) #read sensor
            new_frame = frame.reshape((24, 32))
            
            #smooth image for faster view
            smoothed_frame = alpha * new_frame + (1 - alpha) * previous_frame
            previous_frame = smoothed_frame.copy()
            
            #update the image
            therm1.set_data(np.flipud(np.fliplr(smoothed_frame)))
            therm1.set_clim(vmin=np.min(smoothed_frame), vmax=np.max(smoothed_frame))
            fig.canvas.draw()  # Redraw the figure to update the plot and colorbar
            fig.canvas.flush_events()
            plt.pause(0.001)
            
            #update the sample rate
            t_array.append(time.monotonic() - t1)
            fps = len(t_array) / np.sum(t_array)
            print(f"Sample Rate: {fps: .1f} fps")
            break
            
        except (ValueError, RuntimeError) as e:
            last_exception = e
            retry_count += 1
            time.sleep(0.05)
            
    else:
                print(f"Failed after {max_retries} retries with error: {last_exception}")
                
