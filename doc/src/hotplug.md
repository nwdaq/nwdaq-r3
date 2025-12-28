# Hot-plug requirements

All platform components MUST handle hot-plug events in the described fashion. Failing to do so may result
in unpexpected behaviour, premature component failure or degradation. Connector contacts are extremely
susceptible to failure when unrush currents are not managed properly.

``VBUS_LP`` and ``VBUS_HP`` have slightly different requirements, these are described in their individual
sections right after the common hot-plug introduction.


## Definition of cold/hot/surprise plugging and unplugging of plug-in units

**Plugging** in a plug-in unit into a backplane means inserting the unit slowly into the card guide
groove and pushing it towards the backplane until a contact is made. During the process, an intermittent
reconnections may happen as the operator movement is not steady and perfect. After the unit is fully
inserted, it is secured with two or more front panel bolts.

**Unplugging** a plugin unit is a reverse process. First, the securing bolts are released and the unit is
pulled from the backplane afterwards. It is being pulled until it is completely off the card guide grooves.
During the instant of pulling the unit from the backplane, connectors may be intermittently reconnected as
a result of eg. multiple pull attempts.

Both events may be done in several platform states.

**Cold** plug or unplug means a plug-in unit is plugged-in or plugged-out to/from a system without any power
or communication on the backplane. This includes situations when there are individual plug-in units
still powered (eg. a power supply or a battery backup unit) but not sourcing any current into the backplane
ower rails and the bacplane is unpowered.

A system MAY BE commanded into a cold state externally by eg.pressing a button on a power supply or instructing
a programmable power supply to turn off remotely.

**Hot** plug/unplug means the unit is inserted or pulled out from a live system, when the backplane power rails are
powered and possibly a communication is ongoing on one or multiple data busses. The system MUST BE instructed
and prepared for hot-plug or hot-unplug event by suitable means, eg. by pressing a button or instructing
a main plug-in unit programatically. The system MUST allow hot-plug or hot-unplug in a timely manner and it
SHOULD signal the user when it is ready.

**Surprise** plug/unplug means the system is not prepared for the action in any way and the user is allowed
to insert or pull out a plug-in unit any time. This action MUST NOT cause any power supply instability or
any communication failure except when the communication was ongoing with the unit being pulled out.


## General requirements

**Stacking** plug-in units MAY support hot plugging or surprise plugging but are generally not required to. A stacking
plug-in unit is an unit which bridges backplane connections in a suitable way to external cabling, which can be
bridged back into another backplane with a second stacking plug-in unit. As connecting two live backplanes
together is a complex task, this functionality is not required. Stack assembly or disassembly MUST NOT be done
if at least one of the backplanes is live (powered) unless it is allowed explicitly by the stacking unit specification.

**Power sourcing units**, whether sourcing power to ``VBUS_LP`` or ``VBUS_HP``, MUST regulate the output in a constant
voltage, constant current manner, thus limiting the output current to the specified value. Moreover, they must sense
the ``CD`` pin on the ``JM0`` or ``JM7`` backplane connector to determine when they are fully inserted. Units SHOULD
debounce the ``CD`` input and wait at least one second after the ``CD`` input is stable, before applying any power
to the bacplane power rails.

Any unit which **sinks** power must use a suitable over-current protection on all power buses it uses. If the maximum
current draw of the unit is less than ``100 mA`` under all circumstances, it MAY use a polyfuse (PPTC) as
an over-current protection and a ``5 V`` TVS diode MAY be used as a over-voltage protection.
If the input capacitance of the unit power bus input is less than ``100 uF``,
a simple high-side MOSFET with a gate capacitor can be used for inrush current limiting and delayed turn-on.
If the input capacitance is ``1 uF`` or less, inrush current limiting is not mandatory. This capacitance includes
the input filter capacitance, if any.

In all other circumstances, a proper integrated circuit managing UVLO (under-voltage lockout), OVP (over-voltage
protection), inrush current limiting, OCP (over-current protection) and delayed turn-on SHOULD be used.
Refer to the [parts cross reference](parts.md) for suggestions.

> [!caution]
> With the simplest possible solution, no UVLO is provided. The unit MUST handle under-voltage by any other
> suitable method, eg. a UVLO input of the downstream voltage regulator or a brown-out detector on the MCU.
> The unit MUST go into a low power/reset state when under-voltage occurs.
