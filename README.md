# Automated Painting Tool

Automate your digital artwork in paint programs using predefined coordinates and image processing!

## Repository Structure

```
.
├── sample/          # Upload source images here
├── test/            # Stores test images and processed outputs
├── coords/          # Contains button coordinates for specific monitors (.pkl files)
├── matrix/          # Holds converted images in .pkl format
├── cleaner.py       # Cleans test and matrix folders
├── getcoords.py     # Records button coordinates for your paint program
├── imgconvert.py    # Converts images to paintable matrix format
└── main.py          # Main automation script
```

## Features

- **Coordinate Mapping** - Store exact screen positions for paint tools
- **Image Conversion** - Transform JPG images to binary matrices
- **Automation** - Simulates mouse painting with precision
- **Safety** - Quick exit with `C` key during execution

## Installation

1. Clone repository:
```bash
git clone https://github.com/ugine-bor/auto-paint.git
cd auto-paint
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Record Coordinates
```bash
python getcoords.py
```
- Enter paint program name (e.g., "paint_pro")
- Open your paint program during the countdown
- Right-click to select colors (black/white)
- Left-click to set canvas boundaries

### 2. Prepare Image
Place source images in `sample/` folder

### 3. Run Automation
```bash
python main.py
```
1. Choose coordinate template (.pkl from coords/)
2. Select source image (.jpg from sample/)
3. Wait for image processing
4. Open paint program when prompted
5. Watch the magic happen!

## Cleanup
```bash
python cleaner.py
```
Clears all files in:
- `test/` (processed images)
- `matrix/` (binary matrices)

## Important Notes
- Test with simple images first
- Ensure consistent paint program window positioning
- Keep mouse stationary during automation
- Backup important files - cleaner.py removes generated content
