# Backplane connector pinouts

The backplane contains slots for 8 connectors named JM0 to JM7, JM0 being on the bottom. There are
rules regarding the connector usage and future-proofing of the platform:

-	All connector positions are optional from the electrical point of view. Absence of any
	single connector MUST NOT cause any malfunction.
-	Some connector combinations have no meaningful sense. Such combinations SHOULD NOT be used.
	If a slot usage depends on any other slot, it MUST be noted in the specification
	and the reason MUST BE properly explained.
-	A compatible version of the specification MAY add connectors to unused slots
-	Replacing connector in an existing slot or removing a connector slot from the specification
	means introducing an incompatible specification change.


> [!note]
> Add connector dependencies and connector group usage notes. Probably the best place for this
> information is directly in the following subsections.


## JM0

``JM0`` connector provides power and data for simple and low power units usually in the 1-3 power class.
No power or communication redundancy is available if only JM0 is used. Signal placement on the connector
is optimized to allow using PCBs made with simple processes, 2 or 4 layer.

![Backplane connector pinout and suggested routing - JM0](figures/jm0.svg)

``JM0`` backplane connector signal description:

|Signal     |Description                                          |
|-----------|-----------------------------------------------------|
|CD         |Card detect. Connect resistor to GND or VBUS_LP. See [card detection](card-detect.md) section. |
|CH         |Chassis ground. See `grounding-concept`. |
|GND        |Plug-in unit main ground connection. |
|VBUS_LP    |Low-power bus connection |
|T1S_P      |10Base-T1S bus, positive |
|T1S_N      |10Base-T1S bus, negative |
|NBUS_P     |First ``nwdaq-nbus2`` bus, positive |
|NBUS_N     |First ``nwdaq-nbus2`` bus, negative |
|Reserved   |Reserved pins for debug, ID LED, etc. |


## JM1

``JM1`` connector provides a redundant ``VBUS_LP`` power and a redundant ``nwdaq-nbus2`` data communication.
For units with higher data transfer requirements, ``100Base-T1/1GBase-T1`` interface is available.

> [!warning]
> When speaking of redundancy, there is no point in including the ``JM1`` connector without also including
> the ``JM0`` connector. While it may be reasonable to use ``JM1`` alone eg. for a high-speed plug-in
> unit utilizing only the ``100Base-T1`` bus and the second ``VBUS_LP`` bus, it does not work in practice.
> A power sourcing unit may only supply the first ``VBUS_LP`` power bus, leaving such unit unpowered.
> Hence, when ``JM1`` connector is used, ``JM0`` MUST also be used.

![Backplane connector pinout and suggested routing - JM1](figures/jm1.svg)


``JM1`` backplane connector signal description:

|Signal     |Description                                          |
|-----------|-----------------------------------------------------|
|GND        |Plug-in unit main ground connection. |
|VBUS_LP    |Redundant low-power bus connection |
|SPE_P      |Single-pair ethernet 100Base-T1/1GBase-T1 bus, positive |
|SPE_N      |Single-pair ethernet 100Base-T1/1GBase-T1 bus, negative |
|NBUS_P     |Redundant ``nwdaq-nbus2`` bus, positive |
|NBUS_N     |Redundant ``nwdaq-nbus2`` bus, negative |
|Reserved   |Reserved pins for USB, etc. |


## JM2

``JM2`` connector carries any application specific differential signals in a star topology. The exact fan-out
is backplane and bus/protocol specific. A few examples of plug-in units with ``JM2`` used for custom
signalling are:

* a main unit or a USB hub unit using the connector to fan-out its USB downstream ports
* an ethernet switch unit connecting individual switch ports to ``JM2`` differential lanes
* a clock distribution unit using ``JM2`` lanes to distribute differential clock to neighboring units


![Backplane connector pinout and suggested routing - JM2](figures/jm2.svg)

``JM2`` backplane connector signal description:

|Signal     |Description                                          |
|-----------|-----------------------------------------------------|
|GND        |Ground connection. |
|Lx_P       |Lane x, positive   |
|Lx_N       |Lane x, negative   |


## JM7

``JM7`` connector provides a high power ``VBUS_HP`` bus capable of delivering maximum of ``10 A`` at a ``28 V``
nominal voltage (``26.4 V`` centered when the power sources/sinks are in regulation).

Additionally, it provides a separate chassis ground connection, a separate card detect input/output
and a ``nwdaq-pbus`` single-wire bus to communicate all power sources/sinks on the backplane.

> [!tip]
> A plug-in unit MAY use ``JM7`` connector alone without any other connectors if the sole purpose of the
> unit is sinking or sourcing power. Hot-plug is handled with the dedicated ``CD`` pin and the communication goes
> only through the ``nwdaq-pbus`` bus.

> [!tip]
> If a power sinking plug-in unit is capable of operating with various power levels, it may contain both ``JM0/JM1``
> and ``JM7`` connectors and use whatever is available, or, use ``JM7`` when available to sink higher power levels
> while fall-backing to ``JM0/JM1`` when only ``VBUS_LP`` is available.

![Backplane connector pinout and suggested routing - JM7](figures/jm7.svg)


``JM7`` backplane connector signal description:

|Signal     |Description                                          |
|-----------|-----------------------------------------------------|
|CD         |Card detect. Connect resistor to GND or VBUS_LP. See [card detection](card-detect.md) section. |
|CH         |Chassis ground. See [grounding concept](grounding.md). |
|GND        |Plug-in unit main ground connection. |
|VBUS_HP    |High-power bus connection |


