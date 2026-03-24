import cv2
import numpy as np

def measure_object(source='image', scale_factor=0.026):
    """
    Measures object size from image or webcam using camera calibration.
    source: 'image' for loading from file, 'webcam' for live measurement.
    scale_factor: cm per pixel (example: 0.026 cm/pixel).
    """
    # Load calibration data
    try:
        data = np.load('calibration_data.npz')
        mtx = data['camera_matrix']
        dist = data['dist_coeffs']
        print("Calibration data loaded successfully.")
    except FileNotFoundError:
        print("Error: Calibration data file 'calibration_data.npz' not found. Run calibration.py first.")
        return

    if source == 'image':
        # Load image from file
        img = cv2.imread('object.jpg')
        if img is None:
            print("Error: Could not load 'object.jpg'. Make sure the file exists.")
            return
        process_image(img, mtx, dist, scale_factor)
    elif source == 'webcam':
        # Capture from webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        print("Press 'q' to quit webcam measurement.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from webcam.")
                break

            processed_frame = process_image(frame, mtx, dist, scale_factor)
            cv2.imshow('Object Measurement', processed_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Error: Invalid source. Use 'image' or 'webcam'.")

def process_image(img, mtx, dist, scale_factor):
    """
    Processes the image: undistort, detect object, measure size.
    Returns the processed image.
    """
    # Undistort the image
    undistorted = cv2.undistort(img, mtx, dist, None, mtx)

    # Convert to grayscale
    gray = cv2.cvtColor(undistorted, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest contour (assuming it's the object)
        largest_contour = max(contours, key=cv2.contourArea)

        # Get bounding box
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Draw rectangle around object
        cv2.rectangle(undistorted, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Calculate dimensions in pixels
        width_pixels = w
        height_pixels = h

        # Convert to real-world units (cm)
        width_cm = width_pixels * scale_factor
        height_cm = height_pixels * scale_factor

        # Display dimensions on image
        cv2.putText(undistorted, f"Width: {width_cm:.2f} cm", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(undistorted, f"Height: {height_cm:.2f} cm", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Print measurements to terminal
        print(f"Object Width: {width_cm:.2f} cm, Height: {height_cm:.2f} cm")

    return undistorted

if __name__ == "__main__":
    # Run calibration first if needed
    # calibrate_camera()  # Uncomment if you want to run calibration here

    # Measure from image
    print("Measuring from image...")
    measure_object(source='image')

    # Uncomment below for webcam measurement
    print("Measuring from webcam...")
    measure_object(source='webcam')