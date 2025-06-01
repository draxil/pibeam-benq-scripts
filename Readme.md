# What is this?

Do you happen to have a BenQ TK710 projector (or in my experience any other BenQ projector)? Do you happen to have a pibeam which you want to use to switch it on and off?

Well in here are the scripts to do that, in my experience easiest ran with the mpremote command. You'll need the pybeam library file to be on your pibeam. 

```sh
# turn the projector on!
mpremote run on.py 
```

See references:

https://github.com/sbcshop/PiBeam_Software
https://docs.micropython.org/en/latest/reference/mpremote.html

# Other users

If you've found this and you don't have my exact use-case, it's probably still a useful starting point. You can record the codes for whatever remote you have using some of the example code that's in the pibeam repo [receiver_demo.py](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/receiver_demo.py), and then produce your own scripts.

If you have some other IR device these codes might still be useful for other BenQ owners.
