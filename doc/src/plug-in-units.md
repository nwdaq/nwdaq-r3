## Plug-in unit PCB dimensions

A single plug-in unit comprises of at least these components:

- front panel with the specified design
- front panel bracket/holder to assist with pullting the unit out of the subrack
- two PCB holders
- one or more backplane connectors on the back
- PCB

For more elaborate designs there may be more components in a single unit, eg. multiple PCB holders when more than one
PCB is used, helper connectors, PCB cover, etc.

The basic dimensions of a plug-in unit are depicted below:

![Dimensions of a plug-in unit main PCB](figures/pcb-dimensions.svg)


### PCB dimensions

The PCB SHOULD have rectangular shape, MUST be ``100 mm`` wide and SHOULD be ``73 mm`` long.
PCB to front panel gap SHOULD be ``2.54 mm`` and PCB to backplane distance SHOULD be ``12.5 mm``.
This distance is optimized for *TE Metral* connectors.

> [!tip]
> Under some circumstances it is possible to extend the PCB up to ``2.34 mm`` to the front panel, removing the
> gap and leaving some headroom of ``0.2 mm`` for PCB and front panel tolerances. The complete PCB length will
> be ``75.34 mm`` in this case (``75.0 mm`` being more common).
>
> This helps to accomodate PCB connectors which are mounted too close to the front panel.

> [!warning]
> Observe isolation clearance between the PCB and the front panel.


### PCB clearances

On both sides of the PCB, there is a space reserved for card guide grooves, which MOST NOT contain any
components on front and back PCB sides. The reserved space MUST be at least ``3 mm`` wide and it is recommended
to place a mask-free exposed copper pour at least on the outer ``2 mm`` of the PCB. If an exposed copper pour
is used, it MUST be connected to the chassis ground (``CH`` pin on the ``JM0`` and ``JM7`` backplane connector).


### PCB mounting holes

There are two mounting holes on the PCB which are used to fasten front panel angle brackets. These holes MUST
have a diameter of ``2.7 mm`` to accomodate ``M2.5`` bolts. Holes are positioned ``6.11 mm`` from the front panel
and are spaced ``88.90 mm`` apart, centered on the PCB. Refer to the figure above for hole positions.


### PCB components maximum height

Considering the PCB thickness of ``1.60 mm``, PCB surface to the module boundary/``HP`` distance is:

* ``2.50 mm`` on the bottom side of the PCB
* ``16.20 mm`` on the front side of the PCB

There MUST be at least ``0.40 mm`` distance between components and the module/``HP`` boundary, which means
the maximum allowable component height is:

* ``2.10 mm`` for bottom-side components
* ``15.80 mm`` for front-side components

> [!caution]
> If the PCB requires a defined minimum electrical clearance, it MUST consider the neighboring plug-in unit to fully
> utilize its available space.
