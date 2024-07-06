.. _firmware_overview:

Firmware Overview
=================

.. _firmware_description:

Firmware Description
--------------------

Firmware is a computer program that directly controls the behaviour of hardware. It doesn't usually get updated, so it's more permanent than other kinds of software—hence the word 'firm'. A system can have many different hardware components, each possibly having their own firmware. For example, the HM-10 module used in our RC car has its own firmware that handles BLE functionality. However, this section of the document is about the firmware responsible for the whole RC car system. In our example, this is the firmware we write for our system's main microcontroller, the STM32 NUCLEO-C031C6.

.. _firmware_responsibilities:

Firmware Responsibilities
-------------------------

In the context of our RC car, the firmware is responsible for two things:

#. :ref:`Receiving and interpreting data from the BLE module <firmware_data_transfer>`
#. :ref:`Sending commands to the motor driver <firmware_motor_control>`