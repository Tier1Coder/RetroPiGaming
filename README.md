# RetroPie Gaming Setup on Raspberry Pi 4 with Arduino Uno R3 Gamepad

This repository provides a comprehensive guide for setting up a retro gaming console using a Raspberry Pi 4, installing RetroPie, configuring an Arduino Uno as a gamepad, and installing games via SSH. Whether you're a retro gaming enthusiast or a beginner, this guide will help you build and configure your own gaming console.
![completed_project](https://github.com/user-attachments/assets/0cae4e70-fd8d-4249-aab7-5c2f98712ed2)

https://github.com/user-attachments/assets/bfca9009-48d0-4dd2-8a69-17c79cd01a2b


## Table of Contents

- [Introduction](#introduction)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup Guide](#setup-guide)
  - [1. Setting Up Raspberry Pi 4 with RetroPie](#1-setting-up-raspberry-pi-4-with-retropie)
  - [2. Configuring Arduino Uno as a Gamepad](#2-configuring-arduino-uno-as-a-gamepad)
  - [3. Installing Games via SSH](#3-installing-games-via-ssh)
- [Troubleshooting](#troubleshooting)

## Introduction

This guide is designed to help you set up a complete retro gaming console using a Raspberry Pi 4 and RetroPie, along with configuring an Arduino Uno R3 as a custom gamepad. Additionally, it covers how to install games on your emulator through SSH.

## Hardware Requirements

- **Raspberry Pi 4** (with power supply, microSD card, and case)
- **Arduino Uno R3** (with necessary buttons and joystick or a shield)
- **MicroSD card** (at least 32GB recommended, FAT32)
- **HDMI cable** (for connecting Raspberry Pi to a display)
- **Keyboard and Mouse** (for initial setup)
- **Network connection** (Ethernet or Wi-Fi)

## Software Requirements

- **RetroPie**: A free software that turns your Raspberry Pi into a retro-gaming console. [Official RetroPie Website](https://retropie.org.uk/)
- **Arduino IDE**: Required for configuring the Arduino Uno as a gamepad.
- **UnoJoy Library**: A library that allows the Arduino Uno to function as a USB gamepad.
- **SSH Client**: For remote access to your Raspberry Pi (e.g., PuTTY, Terminal).

## Setup Guide

### 1. Setting Up Raspberry Pi 4 with RetroPie

Follow these steps to set up your Raspberry Pi 4 with RetroPie:

1. Download the latest RetroPie image from the [official website](https://retropie.org.uk/download/).
2. Write the RetroPie image to your microSD card using e.g. Raspberry Pi Imager.
3. Insert the microSD card into the Raspberry Pi 4 and power it on.
4. Complete the initial RetroPie setup, including configuring your keyboard and connecting to Wi-Fi. As a system, choose legacy one, such as Legacy Buster OS. For location, select USA, America.
5. After callibration, open terminal and perform `sudo apt-get update && sudo apt-get upgrade`.
6. Find `locale` settings file and ensure the settings are: `LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_CTYPE="en_US.UTF-8" LC_NUMERIC="en_US.UTF-8" LC_TIME="en_US.UTF-8" LC_COLLATE="en_US.UTF-8" LC_MESSAGES="en_US.UTF-8" LC_PAPER="en_US.UTF-8" LC_NAME="en_US.UTF-8" LC_ADDRESS="en_US.UTF-8" LC_TELEPHONE="en_US.UTF-8" LC_MEASUREMENT="en_US.UTF-8" LC_IDENTIFICATION="en_US.UTF-8" LC_ALL=en_US.UTF-8`. You can use e.g. nano to edit those properties.
7. Use installation script: `cd RetroPie-Setup && chmod +x retropie_setup.sh && sudo ./retropie_setup.sh`.
8. Launch RetroPie using `emulationstation` command.

**Possible trouble**
If an error occured during installation, perform the following:
1. Navigate: `Manage Packages -> dependancy packages -> mesa-drm`. Launch: `install from source`.
2. Navigate: `Manage Packages -> dependancy packages -> omxiv`. Launch: `install from source`.
3. Perform the "Basic" installation.


### 2. Configuring Arduino Uno as a Gamepad

To use your Arduino Uno R3 as a gamepad, follow these steps:

1. Install the Arduino IDE on your computer.
2. Download and install the UnoJoy library from [this GitHub repository](https://github.com/AlanChatham/UnoJoy).
3. Program your Arduino Uno with the provided `.ino` file that configures it as a gamepad.
4. Connect the buttons and joystick to the appropriate pins on the Arduino Uno.
5. Follow the instructions from the UnoJoy library to flash the Arduino and enable joystick mode.

### 3. Installing Games via SSH

To add games to your RetroPie setup, you can use SSH for easy file transfer:

1. Enable SSH on your Raspberry Pi.
2. Use an SSH client (e.g. PuTTY, FileZilla) to connect to your Raspberry Pi.
3. Navigate to the appropriate folder on your Raspberry Pi (e.g. `/home/pi/RetroPie/roms/`).
4. Upload your game files to the corresponding emulator folder (e.g., `nes` for NES games).
5. Restart EmulationStation to load the newly added games.

## Troubleshooting

If you encounter any issues during the setup process, consider the following solutions:

- **No SSH Access**: Ensure that SSH is enabled on the Raspberry Pi and that you have the correct IP address.
- **Gamepad Not Working**: Double-check the Arduino wiring and configuration. Make sure the UnoJoy library was correctly installed.


## **Using with PC*
This gamepad can be used with PC. Launch the script, connect to the proper COM port that will receive inputs from Arduino's gamepad.
