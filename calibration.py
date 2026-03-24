import cv2
import numpy as np
import os
import glob

def calibrate_camera():
    """
    Calibrates the camera using checkerboard images.
    Returns camera matrix and distortion coefficients.
    """
    # Checkerboard dimensions (number of internal corners)
    CHECKERBOARD = (8, 5)  # 8 corners in width, 5 in height for 9x6 squares

    # Termination criteria for corner refinement
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # Prepare object points (3D points in real world space)
    objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

    # Arrays to store object points and image points from all images
    objpoints = []  # 3D points
    imgpoints = []  # 2D points

    # Load calibration images
    images = glob.glob('calibration_images/*.jpg')
    if not images:
        print("Error: No calibration images found in 'calibration_images' folder.")
        return None, None

    print(f"Found {len(images)} calibration images.")

    for fname in images:
        img = cv2.imread(fname)
        if img is None:
            print(f"Could not load image: {fname}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

        if ret:
            objpoints.append(objp)
            # Refine corner locations
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

            # Draw and display corners (optional, for debugging)
            cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
            cv2.imshow('Chessboard Corners', img)
            cv2.waitKey(500)
        else:
            print(f"Chessboard corners not found in {fname}")

    cv2.destroyAllWindows()

    if not objpoints:
        print("Error: No valid calibration images found.")
        return None, None

    # Calibrate camera
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    if ret:
        print("Camera calibration successful.")
        # Save calibration data
        np.savez('calibration_data.npz', camera_matrix=mtx, dist_coeffs=dist, rvecs=rvecs, tvecs=tvecs)
        print("Calibration data saved to 'calibration_data.npz'.")
        return mtx, dist
    else:
        print("Camera calibration failed.")
        return None, None

if __name__ == "__main__":
    calibrate_camera()