import cv2
import color_text
import textfile_editor

pixel = "@"


def print_ascii_image(image, width: int):
    resized_img = resize_image(image, width)
    ascii_image = return_color_ascii_image(resized_img)
    print(ascii_image)


def output_ascii_image_as_txt_file(image,output_path : str,width: int):
    resized_img = resize_image(image, width)
    ascii_image = return_color_ascii_image(resized_img)
    ascii_image = raw(ascii_image)
    textfile_editor.write(output_path, ascii_image)
    

def raw(_text):
	return r'{}'.format(_text)

def resize_image(image, new_width):
    height, width, ch_count = image.shape
    ratio = (height / float(width * 2.5))
    new_height = int(new_width * ratio)
    frame = cv2.resize(image, (new_width, new_height))
    return frame


def return_color_ascii_image(image):
    height, width, ch_count = image.shape
    ascii_image = ""
    for i in range(height):
        if(i != 0):
            ascii_image += "\n"
        for j in range(width):
            BGR = image[i][j]
            RGB = convert_BGR_to_RGB(BGR)
            ascii_image += color_text.return_color_text_string(pixel, RGB[0], RGB[1], RGB[2])
    return ascii_image
    

#BGR = (Blue,Green,Red)  RGB = (Red,Green,Blue)
def convert_BGR_to_RGB(BGR):
    RGB = []
    for i in reversed(range(0, 3)):
        RGB.append(BGR[i])
    return RGB


def load_image_by_path(path):
    return cv2.imread(path)
