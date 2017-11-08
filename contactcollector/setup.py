from setuptools import setup, find_packages

setup(
    name="contact-collector",
    version="17.11.0",
    license="GNU General Public License version 3.0 (GPLv3)",
    description="Django-based framework for for collecting employers and job opportunities for WIL.",
    author="Peter Reutemann",
    author_email="fracpete@waikato.ac.nz",
    url="https://github.com/Waikato/automated-reporting",
    packages=find_packages(),
    install_requires=[
        "Django",
        "django_excel",
        "pyexcel-xls",
        "jinja2",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 3",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Framework :: Django",
    ],
)
