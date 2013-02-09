import _clipboard

def get():
	"""get() -- Get the clipboard's text content as a unicode string"""
	s = _clipboard.get()
	if s is None:
		return None
	return unicode(s, 'utf-8')

def set(s):
	"""set(string) -- Set the clipboard's content to a string"""
	if not isinstance(s, basestring):
		raise ValueError('Must be string or unicode')
	if isinstance(s, unicode):
		_clipboard.set(s.encode('utf-8'))
	else:
		_clipboard.set(s)

def get_image(idx=0):
	"""Get the image at the given index in the clipboard as a PIL.Image. Returns None if the index is >= the number of images in the clipboard."""
	image_info = _clipboard.get_image_data(idx)
	if image_info is None:
		return None
	image_data, w, h = image_info
	import Image
	return Image.fromstring('RGBA', (w, h), image_data)

def set_image(image, format='png', jpeg_quality=0.75):
	"""Set the clipboard to a given PIL.Image."""
	rgba_image = image
	if image.mode != 'RGBA':
		rgba_image = image.convert('RGBA')
	image_data = rgba_image.tostring()
	is_jpeg = format.lower() == 'jpeg' or format.lower == 'jpg'
	_clipboard.set_image_data(image_data, image.size[0], image.size[1], is_jpeg, jpeg_quality)