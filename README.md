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

  <img width="803" height="632" alt="Screenshot 2026-03-24 203113" src="https://github.com/user-attachments/assets/e9bcfe0e-445e-4a99-8fe5-3293f6c91e21" />
  <img width="805" height="632" alt="Screenshot 2026-03-24 204328" src="https://github.com/user-attachments/assets/43dc0512-d81f-4b58-a2a6-c5c6f29ed71f" />
  <img width="801" height="628" alt="Screenshot 2026-03-24 204021" src="https://github.com/user-attachments/assets/db3dbe23-0131-42f2-89d9-b5766e599ba2" />
  <img width="794" height="626" alt="Screenshot 2026-03-24 204154" src="https://github.com/user-attachments/assets/805b9050-de9f-4606-b024-f35617408b99" />





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
