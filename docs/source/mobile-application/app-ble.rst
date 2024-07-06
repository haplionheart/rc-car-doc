.. _app_ble:

BLE Connection and Data Transfer
================================

.. _wireless_protocols:

Wireless protocols
------------------

Different wireless protocols have their own rules for how devices should communicate. As Bluetooth ('Bluetooth Classic') and Bluetooth Low Energy are two different protocols, they also use different rules. We discussed some of the other differences between the two in :ref:`bc_vs_ble`.

.. _ble_overview:

Bluetooth Low Energy Overview
-----------------------------

BLE connections happen between "peripherals" and "central devices". The peripheral is usually a small, low-power device like a fitness tracker or our HM-10 module. A "central device" is usually a more powerful device like a computer or a smartphone. BLE connections happen in the following steps:

#. Peripherals send out radio signals to advertise that they're available for connection
#. Central devices can scan for these advertisements to see what peripherals are available
#. If a central device wants to connect to a peripheral, it sends a connection request
#. If the peripheral accepts the request, then a connection is established
#. The central device and the peripheral can now send data to each other

..
    Might help to have a labelled diagram showcasing this