# Custom version for Pythonista/iOS

import Image
import console
import tempfile
from copy import copy

def show(image, title=None, **options):
	if image.mode != 'RGBA':
		image = image.convert('RGBA')
	tmpfile = tempfile.mktemp()
	w, h = image.size
	console.save_raw_image_data(copy(image.tostring()), image.mode, w, h, tmpfile)
	console.show_image(tmpfile)
	return True
		
	#tmpfile = image._dump(format='PNG')
	#console.show_image(tmpfile)
	#return True

