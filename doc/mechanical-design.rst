====================================
Mechanical design
====================================


Horizontal rail position and side panel dimensions
=======================================================

The *platform* uses only 3U high subracks. Height of the subrack assembly is ``132.35 mm``.

Width of the subrack is variable. The following rules must be respected:

- one horizontal pitch unit ``HP`` is ``5.08 mm`` wide
- unit width is exactly ``4 HP``, yielding ``20.32 mm``. We call it a *module*.
- the first ``HP`` starts ``2.54 mm`` (``0.5 HP``) from the left
- there is an additional ``0.5 HP`` at the end of the rail


.. figure:: _static/horizontal-rails.svg
	:width: 600pt

	Front horizontal rails with rack-mountable side panels (drawing not to scale)


The resulting horizontal rail length is ``(n * 20.32 + 5.08) mm``, ``n`` being the count of modules
in the subrack assembly. Table below lists some common combinations and rail lengths.

.. table:: Common horizontal rail lengths

	========== =============== ===================== ===============================
	Modules    Width in HP     Rail length in mm     Comment
	========== =============== ===================== ===============================
	10         41              208.28                Size for 10" racks
	21         85              431.80                Size for 19" racks
	========== =============== ===================== ===============================


Side view of the subrack with the corresponding dimensions is pictured below.

.. figure:: _static/side-view.svg
	:width: 600pt

	Side panel with horizontal rails attached, side view



Plug-in unit front panels
==================================


The cceptable thickness of the front panel is 2, 2.5 and 3 mm. Width of the front panel is calculated as
``n * 20.32 - 0.30 mm``, where ``n`` represents the width of the unit in modules with each module being ``20.32 mm``
wide. For a 1-module wide plug-in unit, the nominal width is ``20.02 mm``. The height of a 3U front panel is
``128.4 mm``.

Front panels contain two holes for attaching to a PCB, they are horizontally centered to the second HP from the left.
Vertical distance of the holes is ``99.00 mm``, diameter is ``2.7 mm`` and they are vertically centered.

Near the bottom PCB holder hole, there are multiple helper holes to aid in the alignment of the front bracket/holder.
These holes are spaced ``5.08 mm`` apart, typically one hole to the left and two holes to the right of the PCB holder
hole. Please refer to the figure below for further clarification.

Front panels are secured to the subrack front rails using two ``M2.5`` screws for 1 module wide units and four
``M2.5`` for units that are 2 modules or wider. The attachment holes are horizontally centered in the second HP from
the left (and second HP from the right for 2-module and wider units). The holes are vertically centered and their
vertical distance is ``122.5 mm``.


.. figure:: _static/front-panel-1m.svg
	:width: 600pt

	Front panel for 1 module wide plug-in unit



Plug-in unit PCB dimensions
=================================

A single plug-in unit comprises of at least these components:

- front panel with the specified design
- front panel bracket/holder to assist with pullting the unit out of the subrack
- two PCB holders
- one or more backplane connectors on the back
- PCB

For more elaborate designs there may be more components in a single unit, eg. multiple PCB holders when more than one
PCB is used, helper connectors, PCB cover, etc.


.. figure:: _static/pcb-dimensions.svg
	:width: 600pt

	Dimensions of a plug-in unit main PCB


