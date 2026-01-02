import cv2


def main():
    image_path = "/Users/aadrita/python_codes/lesson7/image.jpeg"
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not load image from path: {image_path}")
        return
    print("Original image loaded successfully.")

    sizes = {
        "small": (200, 200),
        "medium": (400, 400),
        "large": (600, 600),
    }

    for size_name, dimensions in sizes.items():
        resized_image = cv2.resize(image, dimensions)  # width, height [web:6]
        window_name = f"{size_name.capitalize()} Image"

        cv2.imshow(window_name, resized_image)
        cv2.imwrite(f"input_image_{size_name}.jpeg", resized_image)
        print(f"Image resized to {dimensions[0]}x{dimensions[1]} pixels ({size_name}) and saved.")

    print("Displaying resized images. Press any key in an image window to exit.")
    cv2.waitKey(0)        # wait once after all images are shown [web:5]
    cv2.destroyAllWindows()
    print("All windows closed. Program completed successfully.")  # [web:1][web:3]


if __name__ == "__main__":
    main()
