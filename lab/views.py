from django.shortcuts import render
import cloudinary.uploader
from django.templatetags.static import static
import os
from django.conf import settings

# Create your views here.

## lab view
def lab(request):
    return render(request, 'lab/lab.html')

def transform_image(request):
    image_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'doctor-removebg.png')
    result = cloudinary.uploader.upload(image_path, 
        transformation=[
            {"effect": "cartoonify"},
            {"width": 500, "height": 500, "crop": "fill"}
        ]
    )

    transformed_image_url = result['url']; print(transformed_image_url)

    return render(request, 'lab/lab.html', {'transformed_image_url': transformed_image_url})
