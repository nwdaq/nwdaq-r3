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
1       0-1 mW          100 mW          Extremely low power optimized devices or devices in standby
                                        during normal use. For primary battery powered applications. LP bus connection
                                        only.
2       1-100 mW        1 W             Middle power devices optimized for low power consumption. The elevated power
                                        usage is usually caused by more complex data logging, fast sampling,
                                        RF usage, etc. Low power main units are usually Class 2.
3       100 mW - 2 W    5 W             Middle power devices, usually multi-radio interface units, Linux-capable
                                        main units, data storage units.
4       2-10 W          20 W            High power specialized devices.
4b                      +-20 W          Middle power bidirectional units intended for providing power, battery backup
                                        units, solar input units.
4h      2-10 W          20 W            High power units connected to the high power bus, 20 W maximum.
                                        various power sinks for isolated power sources, bus power sources, etc.
                                        Sink only allowing a simple bus connection.
4hb                     +-20 W          Same as 4b, power is provided over the high power bus. Bidirectional power flow.
5hb                     +-110 W (4 A)   High power bidirectional unit.
6hb                     +-280 W (10 A)  High power bidirectional unit usually with specific cooling requirements.
======= =============== =============== ================================================================================


