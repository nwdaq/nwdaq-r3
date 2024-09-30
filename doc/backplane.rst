============================
Backplane
============================

Power concept
======================

The backplane has the function to distribute power to all units within a single subrack. Dynamic range of the power
required by the units is very wide - from microwatts to 200 W. For the purpose of unit classification, a range
of power classes is established. It can be used as a guide for selecting the right unit for the particular job.

======= =============== =============== ================================================================================
Class   Average power   Peak power      Examples
======= =============== =============== ================================================================================
``1``   0-1 mW          100 mW          Extremely low power optimized devices or devices in standby
                                        during normal use. For primary battery powered applications. LP bus connection
                                        only.
``2``   1-100 mW        1 W             Middle power devices optimized for low power consumption. The elevated power
                                        usage is usually caused by more complex data logging, fast sampling,
                                        RF usage, etc. Low power main units are usually Class 2.
``3``   100 mW - 2 W    5 W             Middle power devices, usually multi-radio interface units, Linux-capable
                                        main units, data storage units.
``4``   2-10 W          20 W            High power specialized devices.
``4b``                  +-20 W          Middle power bidirectional units intended for providing power, battery backup
                                        units, solar input units.
``4h``  2-10 W          20 W            High power units connected to the high power bus, 20 W maximum.
                                        various power sinks for isolated power sources, bus power sources, etc.
                                        Sink only allowing a simple bus connection.
``4hb``                 +-20 W          Same as 4b, power is provided over the high power bus. Bidirectional power flow.
``5hb``                 +-110 W (4 A)   High power bidirectional unit.
``6hb``                 +-280 W (10 A)  High power bidirectional unit usually with specific cooling requirements.
======= =============== =============== ================================================================================


Low-power bus connected sink-only units (class 1-4)
-----------------------------------------------------

Units with power class ``1`` to ``4`` are sink-only units connected only to the low power bus. The low power bus
provides power with a 5 V nominal voltage and current levels of 2 A average and 4 A peak. The electronics used to
connect to the power bus varies depending on the class. In the simplest case (class ``1``) no specific handling of
hot-plug events and inrush current is needed, whereas class ``4`` requires more delicate PCB design to handle high
currents, hot-plug controller and power switch, inrush current limiter, noise filtering, etc.



Low-power bus connected bidirectional units
------------------------------------------------

For systems utilizing low-power bus only, class ``4b`` provides means to source power to the backplane for low power
applications. A system with a class ``4b`` source only can usually provide power for multiple class ``1``-``3`` units
and one class ``4`` unit.



High-power bus connected sink-only units (class ``4h``)
-------------------------------------------------------

Proper hot-plug management is mandatory. Units are connected to high-power bus only.



High-power bus connected bidirectional units
-------------------------------------------------

Any other high power classes (``4hb``, ``5hb`` and ``6hb``) require advanced electronic for hit-plug management, power
bus protection, unit protection itself, advanced power filtering, advanced high power PCB design, etc. Bidirectional
power flow capability is mandatory.

These units are typically used to power the whole measurement/DAQ system:

- battery packs/units
- photovoltaic power input units
- AC power input units
- external power source/sink device connection using nwDaq p-bus.

