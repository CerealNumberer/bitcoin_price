This python program is for the raspberry pi. It connects to Bitstamp to get the current price of bitcoin.

Once the program has the current price it waits the user set time, in seconds, to fetch the price again.

Once the program has two price points, it compares them.

If the price is higher than the last price, the green LED will light up.
If the price is the same as the last price, both LED's will light up.
If the price is lower than the last price, the red LED will light up.

The program will run until CTRL-C is pressed, and should exit cleanly.
