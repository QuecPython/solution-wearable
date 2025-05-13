# Wearable Solution for QuecPython

[中文](README.zh.md) | English

Welcome to the Wearable Solution repository for QuecPython! This repository provides a comprehensive solution for developing wearable device applications using QuecPython.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)
- [Support](#support)

## Introduction

QuecPython has launched a GUI solution for the wearable industry, including clock display, call making/answering, heart rate/temperature/blood oxygen measurement, step count display, system settings, and other optional functions.

![Wearable Solution](./docs/en/media/image-20231124092228717.png)

The wearable industry solution uses [LVGL](https://lvgl.io/) to draw graphical interfaces. LVGL is a lightweight, open-source embedded graphics library. QuecPython has integrated LVGL and uses NXP's [GUI Guider](https://www.nxp.com/design/software/development-software/gui-guider:GUI-GUIDER) as a graphical interface design tool to automatically generate QuecPython code, greatly improving the efficiency of embedded platform graphical interface design.

## Features

- **Clock Display**: Digital and analog clock interfaces with real-time updates.
- **Health Monitoring**: Heart rate, temperature, and blood oxygen measurement.
- **Activity Tracking**: Step count display and goal setting.
- **Communication**: Call making and answering, chat functionalities.
- **System Settings**: Device information, system upgrade, watch face settings, ringtone settings, vibration mode, factory reset, power off.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites:

- **Hardware**:
  - A QuecPython wearable development board
  - USB Data Cable (USB-A to USB-C)
  - PC (Windows 7, Windows 10, or Windows 11)

- **Software**:
  - USB driver for the QuecPython module
  - QPYcom debugging tool
  - QuecPython firmware and related software resources
  - Python text editor (e.g., [VSCode](https://code.visualstudio.com/), [Pycharm](https://www.jetbrains.com/pycharm/download/))

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/QuecPython/solution-wearable.git
   cd solution-wearable
   ```

2. **Flash the Firmware**:

   Follow the [instructions](https://python.quectel.com/doc/Application_guide/en/dev-tools/QPYcom/qpycom-dw.html#Download-Firmware) to flash the firmware to the development board.

### Running the Application

1. **Connect the Hardware**:
   - Insert the SIM card into the SIM card slot.
   - Connect the antenna.
   - Use a USB data cable to connect the development board to the computer's USB port.

2. **Download Code to the Device**:
   - Launch the QPYcom debugging tool.
   - Connect the data cable to the computer.
   - Press the **PWRKEY** button on the development board to start the device.
   - Follow the [instructions](https://python.quectel.com/doc/Application_guide/en/dev-tools/QPYcom/qpycom-dw.html#Download-Script) to import all files within the `code` folder into the module's file system, preserving the directory structure.

3. **Run the Application**:
   - Select the `File` tab.
   - Select the `main_t.py` script.
   - Right-click and select `Run` or use the run shortcut button to execute the script.

## Directory Structure

```plaintext
solution-wearable/
├── code/
│   ├── EventMesh.py        # Event management module
│   ├── common.py           # Common utilities and base classes
│   ├── constant.py         # Constant configurations
│   ├── lcd.py              # LCD and TP driver initialization
│   ├── css.py              # CSS styles and font styles
│   ├── ui.py               # UI screen classes and interface logic
│   ├── mgr.py              # Background functionalities and managers
│   ├── main_t.py           # Application entry script
│   ├── 16px.bin            # Font file
│   ├── 28px.bin            # Font file
│   ├── 56px.bin            # Font file
│   ├── img/                # Image resources
│   │   ├── point.png
│   │   ├── gps.png
│   │   ├── bat4.png
│   │   └── ...png
└── README.md               # This README file
```

## Usage

[Click](https://python.quectel.com/doc/Application_guide/en/solutions/Wear/index.html) for details of the wearable solution's implementation.

## Contribution

We welcome contributions to improve this project! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need support, please refer to the [QuecPython documentation](https://python.quectel.com/doc/en) or open an issue in this repository.
