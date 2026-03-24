# Object Size Measurement using Camera Calibration

This project demonstrates object size measurement using OpenCV and camera calibration.

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Project Structure
- `calibration.py`: Script for camera calibration using checkerboard images.
- `measure.py`: Script for measuring object size from image or webcam.
- `calibration_images/`: Folder containing checkerboard images for calibration.
- `object.jpg`: Test image for measurement (you need to provide this).

## Setup
1. Install dependencies:
   ```
   pip install opencv-python numpy
   ```

2. Add checkerboard images to `calibration_images/` folder. Use a 6x9 checkerboard pattern.

3. Add a test image named `object.jpg` in the project root.

## Usage

### Camera Calibration
Run the calibration script:
```
python calibration.py
```
This will detect chessboard corners in the images and compute calibration parameters, saving them to `calibration_data.npz`.

### Object Measurement
Run the measurement script:
```
python measure.py
```
By default, it measures from `object.jpg`. To measure from webcam, edit the script and uncomment the webcam part.

For live webcam measurement, modify `measure.py` to call `measure_object(source='webcam')`.

## How it Works
1. **Calibration**: Uses multiple checkerboard images to compute camera matrix and distortion coefficients.
2. **Measurement**: Undistorts the image, detects edges, finds contours, draws bounding box, and calculates real-world dimensions using a scale factor.

## Notes
- The scale factor (0.026 cm/pixel) is an example; adjust based on your setup.
- Ensure good lighting for accurate edge detection.
- Press 'q' to quit webcam mode.