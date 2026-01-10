# Contributing to CANdata2matcsv

Thank you for your interest in contributing to CANdata2matcsv! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear description of the problem
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Your environment (OS, Python version, etc.)
- Sample files if possible (but please don't share proprietary DBC files)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear description of the enhancement
- Use cases that would benefit from this enhancement
- Any implementation ideas you might have

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Coding Standards

- Follow PEP 8 style guidelines for Python code
- Add comments for complex logic
- Update README.md if you change functionality
- Maintain backward compatibility when possible

### Testing

- Test with various CAN log formats (BLF, ASC)
- Test with different DBC files
- Test all resampling options
- Test both CSV and MAT output formats
- Verify the GUI works correctly

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/yourusername/CANdata2matcsv.git
cd CANdata2matcsv
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make your changes and test:
```bash
python CANdata2matcsv.py
```

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Accept constructive criticism gracefully

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to create an issue for any questions about contributing.
