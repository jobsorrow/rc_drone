# rc_drone
This project is simple a radio controlled drone that target ARM cortex-m processor (stm32f103c8) on BluePill development board
This project is developed in STM32CubeIDE that shipped for stm32 microprocessor development. Using computer as a server, written in Python (rc_drone/joy.py)
the computer is interface with USB joystick via pygame library, process the data, then send it in bytes to Radio transmitter via pyserial library
through USB port. The application that run on stm32 microcontroller is written in c (rc_drone/Core/Src/main.c). Using HAL ARM cortex-m hardware driver to-
interface with hardware peripherals inside a microcontroller
