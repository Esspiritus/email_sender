from setuptools import setup

setup(
    name='email_sender',
    version='1.0.0',
    description='A simple email sender library',
    url='https://github.com/Esspiritus/email_sender',
    author='Your Name',
    author_email='your_email@example.com',
    packages=['email_sender'],
    install_requires=[
        'smtplib',
        'email_validator'
    ]
)
