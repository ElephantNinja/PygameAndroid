#! /usr/bin/env python
#
# Python_subset_for_Android Test Program - draw on screen  
# Elephant Ninja for HacDC
# June 1 2011
#

import pygame

## Test if Pygame_for_Android
try:
    import android
except ImportError:
    android = None

def main():
	pygame.init()
	screen = pygame.display.set_mode()
		
	if android:	
		android.init()
		## setup the android exit button
		android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

	## Event constant.
	TIMEREVENT = pygame.USEREVENT
	FPS = 30
	pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

	while True:
	
		ev = pygame.event.wait()

		## Allows Android_OS to take control (ex. pause for phone call) 		
		if android:
			if android.check_pause():
				android.wait_for_resume()
		
		## refresh Screen
		if ev.type == TIMEREVENT:
			pygame.display.flip()
			
		## Draw a blue circle where the screen is touched
		pygame.draw.circle(screen, (0, 128, 255), pygame.mouse.get_pos(), 10)
		
		## Break the while loop to exit if android-back button pressed
		if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
			break
	    
if __name__ == "__main__":
	main()
