from PiBeam import IR_Transmitter,LED
import time,utime

led = LED()
led.off()

tx = IR_Transmitter
tx = tx.NEC()

data    = 80
address = 12288

for i in range(1,6):
    tx.transmit(address,data)
    led.on()
    time.sleep(0.08)
    led.off()
    time.sleep(0.08)
