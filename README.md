# Job Seeker

A program to apply for jobs automatically using Selenium and Glassdoor.com website.

## Getting Started

To use this program, it is necesary to install an automatization tool called Selenium. It can be installed as a Python library following the next instructions.

### Prerequisites

If you have pip on your system, you can simply install or upgrade the Python bindings:

```
pip install -U selenium
```
Alternately, you can download the source distribution from PyPI (e.g. selenium-4.6.0.tar.gz), unarchive it, and run:
```
python3 setup.py install
```
To solve the captcha after each application. An extension called google reCAPTCHA must be installed on your browser
```
## Running the program
To run the program we might select the glassdoor link with the corresponding filters and change it according to our specifications. It is important as well to specify the root where we have our CV and out personal data in order to send it to the employers. To edit the lines we can use vim editor:
```
vim glassdoor3.py
```
To run the program after we edit it we use:
```
python3 glassdoor3.py
```
## Built With

* [Mozilla](http://www.mozilla.org) - The navigator used
* [Selenium webdriver](https://www.selenium.dev/documentation/webdriver/) - Webdriver tool
* [Python](https://www.python.org/downloads/) - Programming language

## Authors

* **Jose Luis Cordoba Cabanillas** - [p3p31v](https://github.com/p3p31v)
