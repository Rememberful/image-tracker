from PIL import Image
import piexif

# Open the image (ensure it's properly recognized as a JPEG)
img = Image.open("th.jpg")

# Convert the image to proper JPEG format if it's not
img = img.convert("RGB")  # Ensure it is in RGB mode before saving as JPEG

# The URL to track (replace with your tracking URL)
url = "https://image-tracker-rbxs.onrender.com/track?id=user123"  # Replace with your server URL

# Check if EXIF data exists, if not, create an empty EXIF structure
if "exif" in img.info:
    exif_dict = piexif.load(img.info["exif"])
else:
    exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": b""}

# Store the URL in the 'Make' tag (or any other tag you prefer)
exif_dict["0th"][piexif.ImageIFD.Make] = url.encode("utf-8")

# Save the image with the updated EXIF metadata
img.save("image_with_tracking.jpeg", exif=piexif.dump(exif_dict), quality=95)

print("✅ Tracking URL embedded in JPEG metadata.")
