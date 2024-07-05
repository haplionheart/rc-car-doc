.. _app_overview:

Mobile App Overview
===================

.. _app_description:

App Description
---------------

The mobile app is used to send commands to the car's HM-10 module via Bluetooth Low Energy (BLE). These commands indicate which direction the car should move in.

.. _app_interface:

App Interface
-------------

.. video:: ../../../media/videos/rc-car-app-rec-comp.mp4
   :width: 300
   :autoplay:

Our app uses a single page interface with two components:

- A Connect Button: Used to connect/disconnect from our car's BLE module
- A Joystick: We use this to drive and steer the car. The direction of the stick indicates which direction the car should move in.

.. _app_architecture:

App Architecture
----------------

The app is built using the mobile app framework, React Native. This lets us build an app that we can deploy to both Android and iOS. We also use Expo, a React Native framework that lets us make changes to our code and see the results instantly. This lets us quickly test code changes without reinstalling the app every time.

React Native can have a steep learning curve if you aren't familiar with Javascript. However there are alternative app frameworks that are built to be more beginner-friendly. MIT App Inventor is a popular example as it lets you build apps without writing code. If you don't want to build your own app, there are existing mobile apps you can download that may match your project requirements.