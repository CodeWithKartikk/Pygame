''' Pygame Surface '''

# 1. The Pygame Surface is used to display any image. 
# 2. The Surface has predefined resolution and pixel format. 
# 3. Default Surface colour is Black
# 4. Alpha planes, color keys,source rectangle clipping
# 5. Its size is basically defined by passing the size argument

''' Pygame Clock '''

# 1. Times are represented in millisecond (1/1000 seconds) in pygame
# 2. Pygame clock is used to track the time
# 3. Time is very essential thing to create motion, play a sonud, or react to any event
# 4. In general we count time in milliseconds but the clock also provides various functions to us which helps
#    us in controlling the game's frame rate.

''' tick() Function '''
# 1. It is used to update the clock
# 2. This method should be called once per frame
# 3. It will calculate how many milliseconds have passed since the previous call
# 4. We have to pass one argument named framerate(it is optional to pass in the function)
# Synatx 
# Clock.tick(framerate = 0)

''' tick_busy_loop() '''
# 1. Its quiet same as tick().
# 2. By calling that clock.tick_busy_loop(20)
# 3. The above program will never run at more than 20 frames per second.
# Syntax
# tick_busy_loop()

''' get_time() function'''
# The get_time() is used to get the previous tick that you had created 
# The no. of milliseconds that passed b/w two calls in Clock.tick().

''' Pygame Blit '''
# Pygame Blit is the phenomena to render/provide the game object onto the surface, and its known as blitting.
# When we create the game object, we need to render it. 
# If you don't render the game objects and still run the program then it will give black window has an output.

# Blitting is the slowest operations in any game .
# You need to be very careful to not to blit much onto the screen in every frame.

# blit(source, dest, area=None, special_flags=0)