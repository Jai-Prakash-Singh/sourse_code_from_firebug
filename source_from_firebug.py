#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

fp = webdriver.FirefoxProfile()
file_name = "/home/user/.mozilla/firefox/41bljqjm.default/extensions/firebug@software.joehewitt.com.xpi"
fp.add_extension(extension=file_name)
fp.set_preference("extensions.firebug.currentVersion", "1.11.2")
browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://goarticles.com/register.html")
html_source = browser.page_source
print html_source

