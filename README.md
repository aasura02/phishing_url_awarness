# phishing URL awarness checker
Overview

Phishing URL Awareness Checker is a simple Python project that identifies common warning signs in URLs.

Features

- Detects @ symbol in URLs.
- Checks URL length.
- Identifies IP address hostnames.
- Detects many hostname segments.
- Identifies punycode.
- Detects HTTP URLs.
- Allows checking multiple URLs.
- Handles invalid URL formats.

Requirements

- Python 3.13.17
- No external libraries required.

How to Run

Open the project folder in VS Code and run:

python phishing_checker.py

Enter a URL when prompted. Type "q" to exit.

Testing

Test results are recorded in "tests/test_samples.md".

Improvements

1. Added repeat URL checking with a quit option.
2. Added a review warning message and invalid URL handling.

Limitations

This tool checks URL text only. It does not open URLs or guarantee that a URL is safe.

Ethical Use

Use this project for educational purposes only. Do not open suspicious URLs.

Author

Student Project