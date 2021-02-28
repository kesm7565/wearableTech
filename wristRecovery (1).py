from microbit import *
from neopixel import NeoPixel
 
num_pixels = 10

foreground = [0xC7, 0x50, 0x99]  # Hex color - red, green and blue
background = [0x10, 0x10, 0x10]
 
ring = NeoPixel(pin0, num_pixels)

wristMotion1 = [0]#initalizing arrays
wristMotion2 = [0]
lightsOff = [0]
 
while True:
    
    def lightUp():  
        
        num_pixels_whole = round(num_pixels, 0)#rounds the number of neopixels being lit up to the nearest whole number
        
        for i in range(0, num_pixels_whole):# lights neopixels up in whatever range the acceleromter allows
        
            ring[i] = foreground     # set pixel i to foreground
            ring.show()              # actually display it
            sleep(50)             # milliseconds
            ring[i] = background     # set pixel to background before moving on
            ring.show()
    
    x1 = accelerometer.get_x()#getting accelerometer x-axis data
    x = x1 + 1024 #making sure that data never goes to zero
    
    y1 = accelerometer.get_y()#getting accelerometer y-axis data
    y = y1 + 1024 #making sure that data never goes to zero
    
    z1 = accelerometer.get_z()#getting accelerometer z-axis data
    z = z1 + 1024 #making sure that data never goes to zero
    
    
    
    
    
    if button_a.is_pressed():#appending either 1 or 2 to the various arrays to trigger the users exercise
        wristMotion1.append(1)
        wristMotion2.append(2)
        lightsOff.append(2)
    
    if button_b.is_pressed():
        wristMotion2.append(1)
        wristMotion1.append(2)
        lightsOff.append(2)
    
    if button_a.is_pressed() and button_b.is_pressed():
        lightsOff.append(1)
        wristMotion2.append(2)
        wristMotion1.append(2)
        
    

    if wristMotion1[len(wristMotion1)-1] == 1:
        num_pixels = y/204 #max value accelerometer produces is 2048, but we are only going to be using half of that data in this case so 1024. 1024/5 = 204, which then
                       #allows the accelerometer data to light up a whole number of pixels
       
        lightUp()#calling function to light up lights
        
    
    if wristMotion2[len(wristMotion2)-1] == 1:
        num_pixels = x/409 #max value accelerometer produces is 2048. 2048/5 = 409(approx.), which then
                       #allows the accelerometer data to light up a whole number of pixels
        lightUp()
       
    
    if lightsOff[len(lightsOff)-1] == 1:
        num_pixels = 0
        lightUp()
    
    print(x)
    #print(wristMotion1)
    
    
        
        
   
    
      
   #print("x, y, z:", x, y, z)
    
    
    