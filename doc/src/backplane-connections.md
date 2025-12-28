# Backplane connections

The backplane provides redundant low power rails, a high power rail, redundant ``nwdaq-nbus2`` communication
buses, ``nwdaq-pbus`` power resource communication bus, ``10Base-T1S`` multidrop ethernet bus and
``100Base-T1/1GBase-T1`` point-to-point links. With the exception of the last one, all interconnections are using
the bus topology. Point-to-point ethernet links use the star topology, more on that in the corresponding section.
There are no external connections going to the backplane except connections allowing backplane stacking.

As a result, ``nwdaq-r3`` platform backplane can be fully passive for its essential purpose.
There are no mandatory components on the backplane except:

- ``nwdaq-nbus2`` bus termination (both ends)
- ``10Base-T1S`` bus termination (both ends)
- ``nwdaq-pbus`` pull-up resistor

All connections are organized into 8 backplane connectors placed in slots with designations JM0 to JM7. The following
table lists all connections within the particular backplane connector.


|Connector  |Name                       |Description |
|-----------|---------------------------|---------------------------|
|JM0        |Basic power and data       |Contains the required minimum for a unit. It carries ``VBUS_LP`` low power bus, ``nwdaq-nbus2`` communication bus, ``10Base-T1S`` ethernet bus, card detect input/output, chassis ground connection. |
|JM1        |Redundant power and data   |This is a redundancy and data speed extension. It carries an independent ``VBUS_LP2`` low power bus, an independent redundant ``nwdaq-nbus2`` communication bus and a 100Base-T1/1GBase-T1 point-to-point ethernet link (the actual connected target depends on the backplane design). |
|JM2        |App specific, star         |Application-specific fanout of 10 differential lanes, connections to other units are dictated by the backplane design. See JM2 addendums for commonly used connections. |
|JM3        |Reserved | |
|JM4        |Reserved | |
|JM5        |Reserved | |
|JM6        |Reserved | |
|JM7        |High power bus             |Carries signals and buses for high power units. ``VBUS_HP`` high power bus capable of delivering ``10 A`` at ``28.8 V`` maximum, ``nwdaq-pbus`` power resource bus, card detect input/output and a chassis ground connection. |


The following subsections briefly describe all available power and data buses.



## ``nwdaq-nbus2`` data bus


``nwdaq-nbus2`` is designed with the following constraints and requirements in mind:

- very low power during the idle state with commonly available CAN bus transceivers
- moderate speeds achievable (1-4 mbit/s on the backplane, 250 kbit/s nominally over long runs)
- request/response (unicast) or multicast
- wired-OR operation to avoid power peaks during collisions
- packet-switched
- native encryption using pre-shared keys providing basic security on the data link layer
- packet size up to 1024 B (this limit is TBD)

On the **physical layer** (L1) level, the bus uses ``CAN 2.0b`` signalling as specified in ISO 11898-2.
Common CAN transceivers can be used to access the ``nwdaq-nbus2`` bus. CAN MAC is not used.

Detailed description of the ``nwdaq-nbus2`` protocol on the MAC and higher levels can be found in the
corresponding section [nbus2 data link layert](nbus2-dll.md).

> [!note]
> There is also a legacy possibility of tunneling ``nqdaq-nbus2`` over a real ``CAN 2.0b`` bus.
> This concept is not part of this specification as it is no longer recommended nor used.
> ``CAN 2.0b`` has a maximum bus length limit for the specified bitrate (ACK bit) and also a
> bitrate limit. Newer CAN bus versions have in-force patents as of 2025.


## ``VBUS_LP`` low power bus (main and redundant)

``VBUS_LP`` buses carry ``5 V`` power to plug-in units, ``4 A`` maximum per unit. The total aggregated backplane
current is limited to ``8 A``. The bus uses its voltage to communicate the currently available amount of power
in total. It is called ``power-availability``, where ``pa--`` state means the shortage is
long lasting, all backup resources are deprived and power failure is imminent, ``pa-`` is the common state when eg.
running on batteries, ``pa0`` means the energy sinking/sourcing is in balance, ``pa+`` means there is a surplus of
energy available (eg. to charge backup batteries) but the amount of energy is limited, ``pa++`` means there is a
power source with virtually infinite capacity (an AC connection for example).

``pa0`` is always at the nominal bus voltage level, ``5 V`` for ``VBUS_LP``. ``pa-`` and ``pa--`` are 5% and 10% less
tha nominal, respectively. ``pa+`` and ``pa++`` are 5% and 10% more than nominal. There is a +-2.5% tolerance on the
voltage levels, that is, ``pa-`` being -7.5% to -2.5% lower than the nominal voltage, for example.

Voltage levels lower than 12.5% less than the nominal voltage are considered bus undervoltage and must trigger
plug-in units ``UVLO`` protection disconnecting the units from the bus.

Voltage levels higher than nominal + 12.5% are considered overvoltage and all units must deal with it individually by
cutting the bus off (an ``OVP`` protection).

Additionally, all sinking units must limit their current sink to the value specified in the corresponding unit
datasheet, no more than ``4 A``, which is the maximum current possible for the ``VBUS_LP`` bus. This limit protects
the backplane connector and wiring and maintains availability of the bus power in case of a misbehaving unit. The
same applies to sourcing units which are required to source power in a CC/CV manner, limiting the current to ``4 A``
per ``VBUS_LP``. This protects the unit itself from possible bus shorts.

![Graphical representation of power availability levels for ``VBUS_LP`` and ``VBUS_HP``](figures/power-availability.svg)

> [!note]
> For practical reasons, ``VBUS_LP`` voltage levels are compatible with USB 2.0 and USB 3.0 voltages and it can
> be interfaced with them using minimum amount of components. The power availability feature together
> with the sinking/sourcing regulation on individual units help sink the power without overloading the USB port.


## High power bus ``VBUS_HP``

``VBUS_HP`` bus provide the same functionality as ``VBUS_LP``, with higher voltage levels. The nominal ``VBUS_HP``
voltage is ``26.4 V``, power availability levels remain the same. The bus voltage is usually referred to as ``28 V``
despite not being strictly true. Maximum current per unit is ``4 A`` for standard units, yielding ``105 W`` of
available power. When appropriate measures are taken on the unit, the maximum current per unit can be ``10 A``
(``264 W`` of power), if the backplane allows that.

The total current permissible to be carried over the backplane is ``40 A`` and is limited by the
backplane design and thermal management. Refer to the backplane datasheet for the exact figure.

> [!note]
> Again, for practical reasons, voltage levels on ``VBUS_HP`` are compatible with 12-cell lead-acid batteries
> and with 8-cell LiFePO4 battery packs. Under specific circumstances and using appropriate protections,
> such battery packs can be connected to the ``VBUS_HP`` bus directly without any further regulation.

> [!caution]
> ``VBUS_HP`` carries high currents and current limiting and inrush current limiting is mandatory.
> See the corresponding section on handling hotplug events.

## Ethernet data connection over 10Base-T1S



## Ethernet data connection over 100Base-T1/1GBase-T1


## Application specific differential lanes

