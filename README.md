# CANdata2matcsv

[![English](https://img.shields.io/badge/Language-English-blue)](README.md)
[![日本語](https://img.shields.io/badge/Language-日本語-red)](README_ja.md)

A Python-based GUI tool for converting CAN (Controller Area Network) log files (BLF, ASC) to CSV or MAT format using DBC database files.

[![GitHub Sponsors](https://img.shields.io/github/sponsors/Nishina-N?style=social)](https://github.com/sponsors/Nishina-N)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)



<img width="484" height="485" alt="CANDataConverter" src="https://github.com/user-attachments/assets/f2745b5e-3a61-4e88-895b-35a00bf1a443" />



## Features

- **Supported Input Formats**: BLF (Binary Logging Format), ASC (ASCII format)
- **Supported Output Formats**: CSV, MAT (MATLAB format)
- **Multiple Resampling Options**:
  - 10ms period resampling
  - 100ms period resampling
  - 1 second period resampling
  - Original sampling (individual time axis for each message)
- **GUI Interface**: Easy-to-use tkinter-based graphical interface
- **Progress Tracking**: Real-time progress bar during conversion
- **DBC Support**: Uses CAN database files (.dbc) for signal decoding

## Requirements

- Python 3.7 or higher
- See `requirements.txt` for detailed dependencies

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Nishina-N/CANDataConverter.git
cd CANDataConverter
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the main script:
```bash
python CANdata2matcsv.py
```

2. In the GUI:
   - Select your CAN database file (.dbc)
   - Select your CAN log file (.blf or .asc)
   - Choose your preferred time axis resampling option
   - Choose output format (CSV or MAT)
   - Click "Convert!"

3. The converted file will be saved in the same directory as your input log file with an appropriate suffix indicating the resampling method used.

## Download Pre-built Binary

Windows users can download the pre-built executable from the [Releases](https://github.com/Nishina-N/CANDataConverter/releases) page.

## File Structure

```
CANDataConverter/
├── CANdata2matcsv.py      # Main GUI application
├── CDW.py                 # CAN Data Wrapper class
├── tool/
│   ├── CAN_Extractor.py   # CAN data extraction module
│   └── CDW.py             # CAN Data Wrapper (copy for tool)
├── ico/                   # Icon files (optional)
├── LICENSE                # MIT License
├── README.md              # This file (English)
├── README_ja.md           # Japanese README
└── requirements.txt       # Python dependencies
```

## Output Format

### CSV Format
- Resampled data: Single CSV with all signals aligned to common time axis
- Original sampling: Transposed CSV with individual time axes per message

### MAT Format
- Structured MATLAB file with signal groups organized by CAN ID
- Each CAN ID group contains its signals and time axis

## Support This Project

If this tool has been helpful for your work, please consider supporting its development:

- ⭐ **Star this repository** - It helps others discover this tool
- 💖 **[Become a GitHub Sponsor](https://github.com/sponsors/Nishina-N)** - Support ongoing development
- 🐛 **Report bugs** - Help improve the tool for everyone
- 🔧 **Contribute** - Pull requests are welcome!

Your support helps maintain and improve this tool. Thank you! 🙏

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### What this means:
- ✅ **Free for commercial use** - Use it in your business without restrictions
- ✅ **Free to modify** - Adapt it to your needs
- ✅ **Free to distribute** - Share with colleagues and friends
- ✅ **No warranty** - Provided as-is

## Author

**Nishina**
- 🌐 Website: https://niseng.biz/software/#candataconverter
- 📝 Article: [CANDataConverter on niseng.biz](https://niseng.biz/software/app-can-data-converter-asc-blf-to-csv-mat-en/)
- 💌 Sponsor: [GitHub Sponsors](https://github.com/sponsors/Nishina-N)
- © 2022-2026 Nishina

## Acknowledgments

- Uses `cantools` library for DBC parsing
- Uses `python-can` library for CAN log file reading
- CAN_Extractor module uses LGPL v3 license

## Version History

- **v2.02** (2026): Added DBC/BLF integrity check and decode error handling
  - **Data Integrity Check**: Pre-conversion validation that detects data size mismatches between DBC definitions and actual BLF data
  - **Decode Error Skip**: Automatically skips messages that cannot be decoded and continues processing valid data
  - **Error Summary**: Displays detailed error report at the end of conversion, showing which message IDs had decode errors and how many
  - **User Confirmation**: Asks for user confirmation before processing when integrity issues are detected
  - **Improved User Experience**: Enhanced progress indicators and cleaner warning messages
- **v2.01** (2026): GitHub release version - Replaced CAN_Extractor.exe with CAN_Extractor.py
- **v2.00**: 64-bit version
- **v1.05en**: English message support
- **v1.05**: Performance improvements, individual time axis support
- **v1.04**: Icon settings, UI refinements
- **v1.03**: Bug fixes for certain DBC files
- **v1.02**: Support for filenames containing dots
- **v1.01**: Error message improvements
- **v1.0**: Initial release

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Support & Issues

- 📖 **Documentation**: This README
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Nishina-N/CANDataConverter/issues)
- 💬 **Questions**: [GitHub Discussions](https://github.com/Nishina-N/CANDataConverter/discussions)

---

<div align="center">

**If this tool saved you time, consider [sponsoring ❤️](https://github.com/sponsors/Nishina-N)**

Made by Nishina

</div>
