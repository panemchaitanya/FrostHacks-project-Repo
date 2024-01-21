"""Gesture Robust Arduino Controller Equipment"""

'''Objective of the Project is to create a system which can controll any sort of Electronic Device Or Equipment using Arduino, Open CV and the concept of Leap Motion'''

#importing the required Python module to Connect to the Arduino
import pyfirmata

#declaring a variable for the COM port
comport='COM3' #Requires to enter the 'COM' number when connected with Arduino Board

#listing the particular board, here Arduino with the COM port
board = pyfirmata.Arduino(comport)

#initilasing the LED pin numbers with the code as connected to the Arduino to controll them
led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')

#defining the function 'led(total)' to to get9 the count of number of fingers open (connected directly to the main input Program)
def led(total):
     #signaling the ON/OFF of the LED's with the count of the number of fingers open
    if total==0:            # 0 fingers open so 0 LED's are ON
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(1)
    elif total==1:          # 1 fingers open so 1 LED is ON
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(1)
    elif total==2:          # 2 fingers open so 2 LED's are ON
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(1)
    elif total==3:          # 3 fingers open so 3 LED's are ON
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(1)
    elif total==4:          # 4 fingers open so 4 LED's are ON
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
    elif total==5:          # 5 fingers open so 5 LED's are ON
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)

    '''Since this 'Controller' code is directly connected to the 'main input Program' so this code ends dirctly there when the 'Terminal' of the 'main input Program' is deleted, due to the interlink of the programs.'''