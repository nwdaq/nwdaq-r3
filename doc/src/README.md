# The nwDAQ-R3 subrack DAQ platform

![nwdaq-r3](nwdaq-r3.svg)

## Introduction

The nwDAQ-R3 is the third revision of a subrack platform designed to house remote data acquisition and logging devices
in the form of plug-in units. It is compliant with the IEC 60297-3 standard and utilizes common components that are
widely available from multiple manufacturers and distributors.

For detailed information on the subrack assembly and its components, including dimensions, please refer to the
[mechanical design](mechanical-design.md) section. This section covers topics such as side panels, horizontal rails,
rail positions, subrack sizes and depths, backplane mounting, front panels and blinds for plug-in units, plug-in units
themselves, and backplane connector layouts.

The [electrical design](electrical-design.md) section provides details on the signals on the backplane,
including power rail types, power classes, and redundant communication buses for both low-power, slow and high-speed
data transfer.

To ensure software compatibility, the [communication protocols](protocols.md) section outlines the protocols used on
the ``nwdaq-nbus2`` bus, as well as the ``10Base-T1S`` and ``100Base-T1/1GBase-T1`` buses. Additionally, this section
describes the protocol used for the ``nwdaq-pbus`` bus, which is employed for communicating power resource information.


## State of the document

The current state of the specification is WIP (Work In Progress).

Changes can be tracked in the
[specification GitHub repository](https://github.com/nwdaq/nwdaq-r3), which serves as the normative source of this text.


## Key-word usage

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in
BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
capitals, as shown here.

## License

<img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="width: 4em;">
<img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="width: 4em;">
<img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" style="width: 4em;">

This work is licensed under CC BY-SA 4.0. To view a copy of this license,
visit [https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)

© 2025-2026 Marek Koza <marek.koza@nwdaq.com> \
© 2023-2024 Marek Koza <qyx@krtko.org>
