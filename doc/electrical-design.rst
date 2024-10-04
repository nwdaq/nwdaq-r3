============================
Electrical design
============================


Overall concept
=========================

Plug-in units are interconnected with a backplane mounted on the rear horizontal rails within the subrack.
Power to the backplane is provided using bidirectional/source units from their respective front panels.
Data communication and any field connections are only done on plug-in unit front panels.


Backplane interconnects
=============================

The backplane provides redundant low power rails, a high power rail, redundant ``nqdaq-nbus`` communication
buses, ``nwdaq-pbus`` power resource communication bus, 10Base-T1S multidrop ethernet bus and 100Base-T1/1GBase-T1
point-to-point links. WIth the exception of the last one, all interconnections are using the bus topology.
Point-to-point ethernet links use star topology, more on that in the corresponding section. There are no external
connections going to the backplane except connections allowing backplane stacking.

All connections are organized into 8 possible backplane connectors with designations JM0 to JM7. The following
table lists all connections within the particular backplane connector.

.. table:: List of backplane connectors with their respective interconnects

	=============== ========================== =================================================================
	Connector       Name                       Interconnects
	=============== ========================== =================================================================
	JM0             Basic power and data       - VBUS_LP low power bus
	                                           - ``nwdaq-nbus`` communication bus
	                                           - 10Base-T1S ethernet bus
	                                           - card detect input/output
	                                           - chassis ground connection
	JM1		Redundant power and data   - VBUS_LP2 low power bus
	                                           - ``nwdaq-nbus`` redundant communication bus
	                                           - 100Base-T1/1GBase-T1 ethernet link
	JM2             App specific, star         Application-specific fanout of 10 differential lanes,
 	                                           connections to the other units are given by the backplane design.
	                                           See JM2 addendums for commonly used connections.
	JM3             Reserved
	JM3             Reserved
	JM3             Reserved
	JM3             Reserved
	JM3             High power bus             - VBUS_HP high power bus
	                                           - ``nwdaq-pbus`` power resource bus
	                                           - card detect input/output
	                                           - chassis ground connection
	=============== ========================== =================================================================



Redundant data connection over ``nwdaq-nbus``
------------------------------------------------


``nwdaq-nbus`` satisfies the following requirements:

- very low power during the idle state
- moderate speeds achievable (1-4 mbit/s on the backplane, 250 kbit/s nominally over long runs)
- initiator driven MAC (token passing) or CSMA/CA/CD MAC
- wired-OR operation to avoid power peaks during collisions
- source-based addressing (publish/subscribe)
- packet-switched
- native encryption using pre-shared keys providing basic security
- packet size up to 1024 B

On the **physical layer** (L1) level, the bus uses CAN signalling as specified in ISO 11898-2. Common CAN and CAN-FD
transceivers can be used to access the ``nwdaq-nbus`` bus. CAN MAC is not used.

.. note::

	There is also a legacy possibility of tunneling ``nqdaq-nbus`` over a CAN 2.0b bus. This concept is not part
	of this specification as it is no longer recommended nor used.


Redundant low power bus ``VBUS_LP`` and ``VBUS_LP2``
--------------------------------------------------------


High power bus ``VBUS_HP``
----------------------------------


Ethernet data connection over 10Base-T1S
---------------------------------------------



Ethernet data connection over 100Base-T1/1GBase-T1
-----------------------------------------------------


Application specific differential lanes
--------------------------------------------


Backplane connector pinouts
==================================

Backplane contains slots for 8 connectors named JM0 to JM7. Not all of them need to be used. These are the
usual combinations:

- JM0 only - for simple units, no requirement for redundancy
- JM1 only - not possible
- JM0+JM1 - redundant low power bus and redundant communication bus
- JM0+JM1 - simple units with fast data transfer requirement (100Base-T1/1GBase-T1)
- +JM2 - ethernet switching boards, USB hub boards, etc.
- JM7 only - high power units, photovoltaic input units, battery packs
- JM0+JM7 - power supplies, external power bus interfaces



JM0
-------------------

JM0 connector provides power and data for simple and low power units usually in the 1-3 power class.
No power or communication redundancy is available if only JM0 is used.


.. figure:: _static/jm0.svg
	:width: 400pt

	Backplane connector pinout and suggested routing - JM0


.. table:: JM0 backplane connector signal description

	========== ====================================================
	Signal     Description
	========== ====================================================
	CD         Card detect. Connect resistor to GND or VBUS_LP.
		   See `card-detection` section.
	CH         Chassis ground. See `grounding-concept`.
	GND        Plug-in unit main ground connection.
	VBUS_LP    Lopw-power bus connection
	T1SP       10Base-T1S bus, positive
	T1SN       10Base-T1S bus, negative
	NBUSP      ``nqdaq-nbus`` bus, positive
	NBUSN      ``nqdaq-nbus`` bus, negative
	========== ====================================================


JM1
------------------


.. table:: JM1 backplane connector signal description

	========== ====================================================
	Signal     Description
	========== ====================================================
	========== ====================================================


JM2
-----------------


.. table:: JM2 backplane connector signal description

	========== ====================================================
	Signal     Description
	========== ====================================================
	========== ====================================================



JM7
-----------------

.. table:: JM7 backplane connector signal description

	========== ====================================================
	Signal     Description
	========== ====================================================
	========== ====================================================




Unit power classes
====================

The backplane has the function to distribute power to all units within a single subrack. Dynamic range of the power
required by the units is very wide - from microwatts to 280 W. For the purpose of unit classification, a range
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

