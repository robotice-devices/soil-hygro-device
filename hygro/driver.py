#!/srv/robotice/bin/python

__version__ = "0.0.1a"

import sys
import time
from oslo.config import cfg
from oslo.config import types

common_opts = [
    cfg.StrOpt('arch',
                    short='a',
                    default='armv7l',
                    help="Architecture armv7l or armv6l"),
    cfg.StrOpt('port',
               short='p',
               help='Port for action.',
               required=True),
    cfg.StrOpt('type',
            short='t',
            default="do",
            help='Digital or Analog output',
            required=True),
]
CONF = cfg.CONF
CONF.register_cli_opts(common_opts)

CONF.__call__(
    project="Robotice",
    prog=' Hygro Driver',
    version=__version__)

CONF(sys.argv[1:])

if CONF.arch == "armv6l":
    import RPi.GPIO as GPIO

    if CONF.port.lower().startswith('bcm'):
        bcm = True
    else:
        bcm = False
        port_do = int(opts.do)
        port_ao = int(opts.ao)

    if bcm:
        GPIO.setmode(GPIO.BCM)
    else:
        GPIO.setmode(GPIO.BOARD)

    if CONF.type == "do":
        GPIO.setup(port, GPIO.IN)
        read = GPIO.input(port)
        print(read)
    elif CONF.type == "ao":
        reading = 0
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(port, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(port) == GPIO.LOW):
            reading += 1
        print(reading)

elif CONF.arch == "armv7l":
    import Adafruit_BBIO.ADC as ADC
    import Adafruit_BBIO.GPIO as GPIO

    # TODO validation analog ports
    if CONF.type == "ao":
        ADC.setup()
        reading = ADC.read(opts.ao)
        print reading
    if CONF.type == "do":
        GPIO.setup(opts.do, GPIO.IN)
        status = GPIO.input(opts.do)
else:
    raise Exception("Uncategeorized arguments %s " % CONF.items())