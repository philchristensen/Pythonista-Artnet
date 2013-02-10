import sys
sys.exec_prefix = sys.prefix
import site

import logging
import os.path
import os
import time

logging.basicConfig(level=logging.INFO)

log = logging.getLogger('touchlight')

def main():
	try:
#		for dir in site.getsitepackages():
#			if not(os.path.exists(dir)):
#				os.makedirs(dir)
#
#		from distribute_setup import use_setuptools
#		use_setuptools()
#
#		from setuptools.command import easy_install
#		easy_install.main(argv=['cement'])

#		from pip.commands import install
#		cmd = install.InstallCommand()
#		opts, args = cmd.parser.parse_args(['cement'])
#		log.error(opts)
#		cmd.run(opts, list(args))

#		import cement
#		log.info(repr(setuptools))
		import artnet
		from artnet.scripts import layered_chase
		layered_chase.main(dict(base='<broadcast>'))
		time.sleep(10)
	except:
		import traceback
		traceback.print_exc()

if(__name__ == '__main__'):
	main()
