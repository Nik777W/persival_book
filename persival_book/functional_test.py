from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

brauser = webdriver.Chrome(options=options)
brauser.get('http://localhost:8000')
assert 'The install worked successfully!' in brauser.title
print(brauser.title)
