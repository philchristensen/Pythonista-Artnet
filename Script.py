import logging

#import GitHubLoader as loader

logging.basicConfig(level=logging.INFO)

log = logging.getLogger('dmxista')

def main():
    try:
        from distribute_setup import use_setuptools
        use_setuptools()
        import cement
        print repr(cement)
    except:
        import traceback
        traceback.print_exc()

#	path = loader.get_latest(
#		username = 'philchristensen',
#		reponame = 'python-artnet',
#		path = 'src',
#	)
#	if(path not in sys.path):
#		log.info('Added python-artnet to Python path.')
#		sys.path.append(path)
#	
#	path = loader.get_latest(
#		username = 'philchristensen',
#		reponame = 'dmxista',
#	)
#	if(path not in sys.path):
#		log.info('Added dmxista to Python path.')
#		sys.path.append(path)
#	
#	from dmxista import app
#	app.main()


if(__name__ == '__main__'):
	main()
