.. _home:

RC Car Conceptual Overview
==========================

.. _project_background:

Project Background
------------------

One of the most memorable toys I received as a child was a radio-controlled (RC) car. I remember being amazed that I could drive the car from a distance instead of pushing it by hand. Even the 'real' cars driven by adults required some manual control, so this RC car seemed like magic to me—a magic I wanted to understand. This document aims to answer some of the questions my younger self would've had about how RC cars work and how to build them.

.. _document_intention:

Intention of this document
--------------------------

This document gives a conceptual overview of the systems used to create an RC car. It uses a prototype RC car I've built as an example.

.. video:: ../../media/videos/car_action_comp.mp4
   :width: 300
   :autoplay:

This document is not a step-by-step tutorial on how to recreate the project. Rather, this document gives background knowledge on the systems and components used to build RC cars and other robotics projects. As you read the document, hopefully it becomes clear that there are improvements that can be made to the example project. By explaining my design choices and highlighting my design flaws, the hope is that you'll understand what you may need to consider when building your own projects. All the components discussed can be swapped out for alternatives based on part availability and your own design requirements.

..
   explain that sections are written assuming you have understanding of previous sections?

To understand this document, you must have an understanding of basic electric circuits. In particular you will need to understand the concepts of voltage, current, energy and power. You also need to know the different between Direct Current (DC) and Alternating Current (AC).

This document is organised as follows:

.. toctree::
   :caption: Project Overview
   :name: project-overview

   overview/project-overview

.. toctree::
   :caption: Hardware System
   :name: hardware-system

   hardware-system/hardware-overview
   hardware-system/chassis
   hardware-system/microcontroller
   hardware-system/gear-motors
   hardware-system/motor-driver
   hardware-system/power-supply
   hardware-system/ble-module

.. toctree::
   :caption: Mobile Application
   :name: mobile-application

   mobile-application/app-overview
   mobile-application/app-ble

.. toctree::
   :caption: System Firmware
   :name: system-firmware

   system-firmware/firmware-overview
   system-firmware/firmware-data-transfer
   system-firmware/firmware-motor-control
