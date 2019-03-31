# img2hex
Convert a 212x104 image to an hex text to send to [FireBeetle Covers-ePaper](https://www.dfrobot.com/wiki/index.php/FireBeetle_Covers-ePaper_Black%26White%26Red_Display_Module_SKU:_DFR0531)


## Table of contents

- [Requirements](#requirements)
- [Usage](#usage)
- [What's included](#whats-included)
- [License](#license)
- [Creator](#creator)


## Requirements

- Python 3


## Usage

IMG2HEX imagefile [output] [-i]

    imagefile: Specifies the image file to convert
  
    output: Indicates a file to write the hex characters to (if omitted saved to out.txt)
  
    -i: Invert colors of the image"


## What's included

- E-ink image converter.ipynb - Python Notebook with examples
- black.bmp                   - Example image (size 212x104)
- black.jpg                   - Example image (size 104x212)
- black.txt                   - Example output for black.bmp / black.jpg
- image.pdn                   - Paint.net file with images black/red
- **img2hex.py**              - **Command line python program**
- PictureDemo_Jorge.ino       - Arduino example to upload to an ESP32 (Firebeetle Board ESP32 in this particular case)
- red.bmp                     - Example image (size 212x104)
- red.txt                     - Example output for red.bmp


## License
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](https://github.com/Naish21/img2hex/blob/master/LICENSE) file for details


## Creator

**Jorge Aranda**

- <https://twitter.com/jam_naish>
- <https://github.com/Naish21>
- <https://www.linkedin.com/in/jorgearandamoro>
