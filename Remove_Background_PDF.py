from fitz import open as fitzOpen, Matrix as fitzMatrix  # PyMuPDF
from time import sleep
from PIL import Image
from img2pdf import convert
from numpy import array, bincount
from os import listdir, path, makedirs


def find_background_color(image_path):

    # Open the image
    image = Image.open(image_path)
    
    # Convert image to numpy array
    image_array = array(image)
    
    # Flatten the array to make it 1-dimensional
    flattened_array = image_array.reshape(-1, image_array.shape[-1])
    
    # Find the most common color
    most_common_color = bincount(flattened_array[:,0]).argmax(), bincount(flattened_array[:,1]).argmax(), bincount(flattened_array[:,2]).argmax()
    
    return most_common_color


def replace_color_with_white(image, target_color, image_path, tolerance=37):
    """
    Replace a specific color in an image with white.
    
    Args:
    - image: The input image (PIL Image object).
    - target_color: The target color to replace (RGB tuple, e.g., (R, G, B)).
    - tolerance: Tolerance level for color similarity.
    
    Returns:
    - Image with the specified color replaced with white.
    """

    width, height = image.size
    pixels = image.load()
    target_color = find_background_color(image_path)
    print(f"{target_color = }, {image_path = }")
    if all(abs((255, 255, 255)[i] - target_color[i]) <= tolerance for i in range(3)) or (
      all(abs((0, 0, 0)[i] - target_color[i]) <= tolerance for i in range(3))):
        if tolerance > 7:
            replace_color_with_white(image, target_color, image_path, tolerance=7)
        print("White paper", f"{image_path = }")
        return image
    if tolerance == 7:
        tolerance = 37

    for y in range(height):
        for x in range(width):
            pixel_color = pixels[x, y]
            if all(abs(pixel_color[i] - target_color[i]) <= tolerance for i in range(3)):
                pixels[x, y] = (255, 255, 255)  # Replace with white
    print("Removed background color of the image", image_path)
    return image


def pdf_to_images(pdf_path, output_folder, resolution=300):
    """
    Convert each page of a PDF to a high-quality image.
    
    Args:
    - pdf_path: Path to the input PDF file.
    - output_folder: Folder where the output images will be saved.
    - resolution: Resolution of the output images (in DPI).
    """
    pdf_document = fitzOpen(pdf_path)
    image_paths = []
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        
        # Render the page to a pixmap with antialiasing
        image = page.get_pixmap(matrix=fitzMatrix(1, 1).prescale(resolution/72, resolution/72), alpha=True)
    
        # Save the image as PNG with high quality
        image_path = path.join(output_folder, f"{path.basename(pdf_path)[:-4]}.page_{page_number + 1}.png")
        print("Created image", image_path)
        image_paths.append(image_path)

        image.save(image_path, "png")
        # print(f"Page {page_number + 1} saved as {image_path}")
    return image_paths


def remove_background_pdf(pdf_file, output_name=None, input_folder=".", output_folder=".", subject=".", tolerance=30):
    if output_name is None:
        output_name = pdf_file
    makedirs(path.join(output_folder, "images"), exist_ok=True)
    makedirs(path.join(output_folder, "pdf"), exist_ok=True)
    image_paths = pdf_to_images(path.join(input_folder, subject, pdf_file), path.join(output_folder, "images"))
    tolerance = 30  # Tolerance level for color similarity

    # Open the input image
    for input_image_path in image_paths:
        input_image = Image.open(input_image_path)
        # input_image.save("test.png")
        # Replace the specified color with white
        output_image = replace_color_with_white(input_image, tolerance, input_image_path)

        # Save the output image
        output_image.save(input_image_path)

    with open(path.join(output_folder, "pdf", output_name), "wb") as f:
        f.write(convert(image_paths))
    print("PDF saved in", path.join(output_folder, "pdf", output_name))
# remove_background_pdf("/home/ghoudiy/Downloads/sciences_ex/math/2024.pdf", output_folder="/home/ghoudiy/")
# remove_background_pdf("/home/ghoudiy/Downloads/economie/math.pdf", output_name="eco_2024.pdf", output_folder="/home/ghoudiy/")
# remove_background_pdf("/home/ghoudiy/Downloads/technique/all/math/2024.pdf", output_name="tech_2024.pdf", output_folder="/home/ghoudiy/")

input_image = Image.open("/home/ghoudiy/Downloads/P-PIIM/web_statique/Projet/images/logo.webp")
# Replace the specified color with white
output_image = replace_color_with_white(input_image, 30, "/home/ghoudiy/Downloads/P-PIIM/web_statique/Projet/images/logo.webp")

# Save the output image
output_image.save("/home/ghoudiy/logo.webp")
output_image.save("/home/ghoudiy/logo.png")


if __name__ != "__main__":
    def remove_background_folder():
        subjects = [
            #  "algorithme",
            #  "bd",
            "math",
            # "physique"
            # "philo",
            # "anglais",
            # "francais"
        ]
        input_folder = "/home/ghoudiy/Downloads/sciences_ex/"
        output_folder = "/home/ghoudiy/Downloads/without"
        for subject in subjects:
            print(f"{subject = }")
        
            def remove_background_color(session, subject, output_folder, input_folder):
                if session == "controle":
                    subject = path.join(subject, "controle")
                output_folder = path.join(output_folder, subject)
                makedirs(path.join(output_folder, "images"), exist_ok=True)
                makedirs(path.join(output_folder, "pdf"), exist_ok=True)
                for pdf_file in listdir(path.join(input_folder, subject)):
                    if pdf_file.endswith(".pdf"):

                        image_paths = pdf_to_images(path.join(input_folder, subject, pdf_file), path.join(output_folder, "images"))
                        tolerance = 30  # Tolerance level for color similarity

                        # Open the input image
                        for input_image_path in image_paths:
                            input_image = Image.open(input_image_path)
                            # input_image.save("test.png")
                            # Replace the specified color with white
                            output_image = replace_color_with_white(input_image, tolerance, input_image_path)

                            # Save the output image
                            output_image.save(input_image_path)

                        with open(path.join(output_folder, "pdf", pdf_file), "wb") as f:
                            f.write(convert(image_paths))
                        print("PDF saved in", path.join(output_folder, "pdf", pdf_file))

            print("Principale: ", "#" * 50)
            remove_background_color("principale", subject, output_folder, input_folder)
            #  sleep(60) # To let the PC rest some time
            # print("Controle: ", "#" * 50)
            # remove_background_color("controle", subject, output_folder, input_folder)
