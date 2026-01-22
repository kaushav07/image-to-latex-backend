from PIL import Image
import io

ALLOWED_FORMATS = ["PNG", "JPEG", "JPG"]

def validate_and_prepare_image(image_bytes: bytes) -> Image.Image:
    """
    Validates image format and converts to RGB
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))

        # ✅ Check image format
        if image.format not in ALLOWED_FORMATS:
            raise ValueError("Only PNG or JPG images allowed")

        # Convert to RGB for consistency
        image = image.convert("RGB")
        return image

    except ValueError:
        raise
    except Exception:
        raise ValueError("Invalid image file")
