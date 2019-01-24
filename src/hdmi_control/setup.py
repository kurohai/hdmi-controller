from setuptools import setup

setup(
    name='hdmi-controller',
    version='0.0.1',
    py_modules=[
        'app',
        'codes',
        'logutil',
        'utils',
        'models',
        'config',
    ],
    include_package_data=True,
    install_requires=[
        'pySerial==3.4',
        'click==6.7',
    ],
    entry_points='''
        [console_scripts]
        hdmictl=app:cli
    ''',
)
