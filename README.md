# PDF Liner

A simple Python script that adds equally spaced horizontal lines to PDF files, making them perfect for printing and handwriting and taking notes on them.

## Installation

1. Clone the repository.

2. Create a virtual python environment if needed.

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

```bash
python pdf_liner.py input.pdf
```

This will create `input_lined.pdf` with default settings (20-point spacing, 0.25 opacity).

### Specify Output File

```bash
python pdf_liner.py input.pdf -o output.pdf
# or
python pdf_liner.py input.pdf --output output.pdf
```

### Customize Line Spacing and Opacity

```bash
python pdf_liner.py input.pdf -o output.pdf -s 25 -a 0.2
# or
python pdf_liner.py input.pdf --output output.pdf --line-spacing 25 --opacity 0.2
```

- `-s` or `--line-spacing`: Space between lines in points (default: 20)
- `-a` or `--opacity`: Line opacity from 0.0 to 1.0 (default: 0.25)

### Enhance Bottom Lines for Better Printing

Some printers tend to fade lines at the bottom of pages. Use the `-e` option to make the bottom lines thicker and darker:

```bash
python pdf_liner.py input.pdf -e 5
# or
python pdf_liner.py input.pdf --enhance-bottom-lines 5
```

- `-e` or `--enhance-bottom-lines`: Number of bottom lines to enhance (default: 3, set to 0 to disable)

### Get Help

```bash
python pdf_liner.py -h
# or
python pdf_liner.py --help
```

### Install Globally

Make sure you have [pipx](https://github.com/pypa/pipx) installed.

```bash
pipx ensurepath
pipx install .
```

To re-install use
```bash
pipx uninstall pdf-liner
pipx install .
# or
pipx reinstall .
```

Now you can run `pdf-liner` from the terminal from anywhere.

## Parameters

- **input_pdf** (required) - Path to the input PDF file
- **-o, --output** (optional) - Path for the output file (default: `input_lined.pdf`)
- **-s, --line-spacing** (optional) - Space between lines in points (default: 20)
- **-a, --opacity** (optional) - Line opacity from 0.0 to 1.0 (default: 0.25)
- **-e, --enhance-bottom-lines** (optional) - Number of bottom lines to enhance for better printing (default: 3)
- **-p, --padding** (optional) - Adds a white page with lines after each page

## Requirements

- Python 3.6+
- PyPDF2
- reportlab
