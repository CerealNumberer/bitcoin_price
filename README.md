This python program is for the raspberry pi. It connects to Bitstamp to get the current price of bitcoin.

Once the program has the current price it waits the user set time, in seconds, to fetch the price again.

Once the program has two price points, it compares them.

If the price is higher than the last price, the green LED will light up.
If the price is the same as the last price, both LED's will light up.
If the price is lower than the last price, the red LED will light up.

The program will run until CTRL-C is pressed, and should exit cleanly.

Raspberry pi pin 11 is the green LED or GPIO 17
Raspberry pi pin 13 is the red LED or GPIO 23

Make sure to use BOARD pin layout. 
If you need to change to GPIO.BCM for forks this is important to note.

