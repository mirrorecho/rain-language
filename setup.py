from distutils.core import setup

install_requires = [
    'pytest',
    'abjad==3.4',
    'abjad-ext-rmakers',
    ]

def main():
    setup(
        author='Randall West',
        author_email='info@randallwest.com',
        install_requires=install_requires,
        name='rain',
        packages=('rain', 'tests'),
        url='https://github.com/mirrorecho/rain-language/',
        version='1.0',
        zip_safe=False,
        )

if __name__ == '__main__':
    main()