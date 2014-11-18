
Soil Hygrometer Detection Module Soil Moisture Sensor
=====

Soil moisture module is most sensitive to the ambient humidity is generally used to detect the moisture content of the soil.

Example use
-----

.. code-block:: bash

    python driver.py -a armv7l -p P9_40 -t ao

.. code-block:: bash

	python service.py -a armv6l -p bcm25 -t do


Instructions for use
------

* Module to reach the threshold value is set in the soil moisture, DO port output high, when the soil humidity exceeds a set threshold value, the module D0 output low;
* The digital output D0 can be connected directly with the microcontroller to detect high and low by the microcontroller to detect soil moisture;
* The digital outputs DO shop relay module can directly drive the buzzer module, which can form a soil moisture alarm equipment
* Analog output AO and AD module connected through the AD converter, you can get more precise values of soil moisture

TODO
-----

* analog read

Read more
-----

* http://www.ebay.com/itm/Soil-Hygrometer-Detection-Module-Soil-Moisture-Sensor-For-arduino-Smart-car-/400364471802
* http://electron-space.blogspot.cz/2013/09/soil-moisture-sensor-soil-hygrometer.html
* https://github.com/jerbly/Pi/blob/master/raspi-adc-pot.py