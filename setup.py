from distutils.core import setup
import setup_translate


setup(name='enigma2-plugin-extensions-auto-dcw-key-add',
		version='3.0',
		author='Youchie / ahmedmoselhi',
		author_email='ahmedmoselhi55@gmail.com',
		package_dir={'Extensions.DCWKeyAdd': 'src'},
		packages=['Extensions.DCWKeyAdd'],
		package_data={'Extensions.DCWKeyAdd': ['update-plugin.sh', 'image/*.png', '*.txt']},
		description='Add Auto DCW Key / Manual BISS Key Plugin for Enigma2',
		cmdclass=setup_translate.cmdclass,
	)
