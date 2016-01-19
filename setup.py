from setuptools import setup

setup(
    name="django-paymill",
    packages=['paymill'],
    version='0.0.1',
    author="Ross Crawford-d'Heureuse",
    license="MIT",
    author_email="sendrossemail@gmail.com",
    url="https://github.com/rosscdh/django-paymill",
    description="A Django app for integrating with paymill",
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'paymill-wrapper'
    ]
)
