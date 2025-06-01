from PiBeam import IR_Transmitter,LED
import time,utime

led = LED()
led.off()

tx = IR_Transmitter
tx = tx.NEC()

data    = 78
address = 12288

for i in range(1,3):
    tx.transmit(address,data)
    led.on()
    time.sleep(0.08)
    led.off()
    # off needs a double pulse, with a decent gap, as the UI gets you to confirm
    time.sleep(0.9)
