.. _firmware_data_transfer:

Handling data received from BLE module
======================================

In :doc:`../mobile-application/app-overview`, we said that command signals from the app are used to control the car's movement. Here's an overview of how this works:

#. The app sends a BLE signal telling the car to either move in a specific direction or stop
#. The BLE module wirelessly receives the signal and sends it to the microcontroller via a wired connection
#. The microcontroller receives the signal and uses it to determine what commands to send to the motor driver
#. The microcontroller sends signals to the motor driver telling it how the car should move
#. The motor driver receives the signals and moves the motors as instructed

..
    Might help to have a diagram illustrating this