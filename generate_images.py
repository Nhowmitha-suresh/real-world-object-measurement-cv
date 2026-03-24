import cv2
import numpy as np
import os

def generate_checkerboard_images(num_images=10, board_size=(9, 6), square_size=50):
    """
    Generate synthetic checkerboard images for calibration.
    """
    if not os.path.exists('calibration_images'):
        os.makedirs('calibration_images')

    for i in range(num_images):
        # Create a larger blank image with white background
        img_size = (400, 600, 3)
        img = np.full(img_size, 255, dtype=np.uint8)

        # Draw checkerboard pattern in the center
        offset_x = (img_size[1] - board_size[0] * square_size) // 2
        offset_y = (img_size[0] - board_size[1] * square_size) // 2

        for row in range(board_size[1]):
            for col in range(board_size[0]):
                if (row + col) % 2 == 0:
                    # Black square
                    x1 = offset_x + col * square_size
                    y1 = offset_y + row * square_size
                    x2 = x1 + square_size
                    y2 = y1 + square_size
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), -1)

        # Add noise to make it more realistic
        noise = np.random.normal(0, 5, img.shape).astype(np.uint8)
        img = cv2.add(img, noise)

        # Save image
        filename = f'calibration_images/checkerboard_{i:02d}.jpg'
        cv2.imwrite(filename, img)
        print(f"Generated {filename}")

def generate_test_object():
    """
    Generate a simple test object image (a rectangle).
    """
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    img.fill(255)  # White background

    # Draw a black rectangle as the object
    cv2.rectangle(img, (200, 150), (400, 300), (0, 0, 0), -1)

    cv2.imwrite('object.jpg', img)
    print("Generated object.jpg")

if __name__ == "__main__":
    generate_checkerboard_images()
    generate_test_object()