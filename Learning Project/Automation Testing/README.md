# Introduction to Selenium
Selenium is a free (open-source) automated testing suite for web applications that supports cross-browser and cross-operating-system interoperability.
Selenium is useful for testing web applications only. Neither desktop (software) testing nor the testing of mobile applications is possible with Selenium.
## Selenium Types
Selenium is not just a single tool but a suite of software, each catering to different testing needs of an organization. It has four components:
- Selenium Integrated Development Environment (IDE)
- Selenium Remote Control (RC)
- Selenium Grid
- Selenium WebDriver
Now that you know about its types, let’s talk about each of them briefly
### Selenium IDE
is a tool that helps you develop your Selenium test cases. It’s an easy-to-use Chrome and Firefox extension and is generally the most reliable method to develop test cases. It records users’ actions in the browser for you, using the existing Selenium commands, with parameters defined by the context of the web element.
- The advantage of Selenium IDE is that the tests recorded via the plugin can be exported in different programming languages like Java, Ruby, Python, etc.
### Selenium RC (Remote Control)
it will act as an HTTP proxy to trick the browser into believing that Selenium Core and the web application being tested belong to the same domain, thus making RC a two-component tool.
- Selenium RC Server
- Selenium RC Client (Library containing the programming language code)
- RC can support the programming languages: Java, C#, PHP, Python, Perl, Ruby
### Selenium Grid
Selenium Grid is a testing tool that lets you run your tests on various machines against different browsers. It is part of the Selenium suite that specializes in running multiple tests across different browsers, operating systems, and machines.

With Selenium Grid, one server makes a move as a hub. Tests communicate to the hub to get access to browser instances. The hub has a list of servers that provide access to browser instances (WebDriver nodes) and lets tests use these instances.

Selenium Grid allows parallel testing and also allows managing different browser versions and browser configurations centrally (instead of in each individual test).

<img src="https://miro.medium.com/proxy/1*ZubHsUOAW_NC2-eumTwXVQ.png"/>

## Selenium WebDriver
elenium WebDriver was the first cross-platform testing framework that would control the browser at the OS level. Selenium WebDriver is a successor to Selenium RC. Selenium WebDriver accepts commands (sent in Selenium or via a Client API) and sends them to a browser.

This is implemented through a browser-specific driver, which sends commands to a browser and retrieves the results. Each driver launches and accesses a browser application. Different WebDrivers are:
- Firefox Driver (Gecko Driver), Chrome Driver, Internet Explorer Driver, Opera, Safari, HTML Unit Driver
### Benefits of Selenium WebDriver
- Selenium WebDriver supports seven programming languages: Java, C#, PHP, Ruby, Perl, Python, and .Net.
- It supports cross-browser interoperability that helps you perform testing on various browsers like Firefox, Chrome, IE, Safari, etc.
- Tests can be performed on different operating systems: Windows, Mac, Linux, Android, and iOS.
- Selenium WebDriver overcomes limitations of Selenium v1 like file upload, download, pop-ups, and dialog barrier
- Cons of Selenium WebDriver
- Detailed test reports cannot be generated.
- Testing images is not possible.
No matter what, these shortcomings can be overcome by integrations with other frameworks. That is, for testing images Sikuli can be used, and for generating detailed test reports, TestNG can be used.

### What are Browser Elements?
Browser elements are different components present on web pages. The most common elements you will notice while browsing are:
- Text boxes
- CTA buttons
- Images
- Hyperlinks
- Radio buttons/Checkboxes
- Text area/Error messages
- Dropdown box/List box/Combo box
- Web table/HTML table
- Frame

Testing these elements essentially means, you have to check whether they are working fine and responding the way you want them to. For example, if you are testing a text box, what would you test it for?

1. Whether you are able to send text or numbers to the text box
2. If you can retrieve text that has been passed to the text box, etc.

If you are testing an image, you might want to:

- Download the image
- Upload the image
- Click on the image link
- Retrieve the image title, etc.
Similarly, operations can be performed on each of the elements mentioned earlier. But only after the elements are located on the web page, you can perform operations on them and start testing them.

## Element locator in Selenium

There are eight attributes that can be used to locate elements on a web page, they are ID, Name, Class Name, Tag Name, Link Text, Partial Link Text, CSS, and XPath.

**Download & Install Pycharm** 
[Click Here]("https://www.guru99.com/how-to-install-python.html")
**Download & Install selenium at Pycharm or python IDE path**
<img src="https://224926-685269-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2017/04/python-selenium-4.png"/>
**Download Chrome driver & store it somewhere [Click Here]("https://chromedriver.chromium.org/downloads")**
