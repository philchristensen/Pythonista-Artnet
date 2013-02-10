import logging
import os.path

logging.basicConfig(level=logging.INFO)

log = logging.getLogger('touchlight')

def main():
	try:
		import site
		for dir in site.getsitepackages():
			if not(os.path.exists(dir)):
				os.makedirs(dir)

		from distribute_setup import use_setuptools
		use_setuptools()
		import cement
		log.info(repr(cement))
	except:
		import traceback
		traceback.print_exc()

if(__name__ == '__main__'):
	main()
