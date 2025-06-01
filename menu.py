from PiBeam import IR_Transmitter,LED
import time,utime

led = LED()
led.off()

tx = IR_Transmitter
tx = tx.NEC()

# menu button, just for testing really and less intense than turning on/off:
data    = 15
address = 12288

for i in range(1,90):
    tx.transmit(address,data)
    led.on()
    time.sleep(0.08)
    led.off()
    time.sleep(0.08)    
