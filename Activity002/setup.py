from setuptools import find_packages, setup

package_name = 'Activity002'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mahmoud',
    maintainer_email='mahmoudahmedibrahim5@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "number_publisher = Activity002.number_publisher:main",
            "number_counter = Activity002.number_counter:main"
        ],
    },
)
