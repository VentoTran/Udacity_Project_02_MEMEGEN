
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import random

# TASK DONE
class MemeEngine:
    """ Create MEME """

    def __init__(self, out_path):
        """ Initialize MemeEngine object """
        self.out_path = out_path
        check_path = Path(out_path)
        if not check_path.exists():
            check_path.mkdir(parents=True)
            print(f"Folder created: {check_path}")
        #endif
    #enddef

    def make_meme(self, img_path: str = None, body: str = None, author: str = None, width: int = 500) -> str:
        """ Create a meme from input image and quotes """

        generated_pic = f"{self.out_path}/{random.randint(0, 1000000)}.png"

        width = min(width, 500)

        try:
            with Image.open(img_path) as img:
                ratio = img.height / img.width
                height = width * ratio
                img = img.resize((int(width), int(height)))
                font_size = int(img.height / 25)

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("./_data/Font/FiraCode/FiraCodeNerdFont-Bold.ttf", font_size)

                x_loc = random.randint(0, int(img.width / 4))
                y_loc = random.randint(0, int(img.height - (font_size * 2)))

                draw.text((x_loc, y_loc), 
                            body, 
                            font=font, 
                            fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                draw.text((int(x_loc * 1.15), y_loc + font_size), 
                            " - " + author, 
                            font=font, 
                            fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                img.save(generated_pic)
            #endwith
        except Exception:
            print("Failed to generate meme!!")
            raise FileNotFoundError("Image file has problem ~!")
        #endtrycatch

        return generated_pic
    #enddef

#endclass

