from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv, os

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location=r"C:\Program Files (x86)\chrome-win64\chrome.exe"

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                          options=chrome_options)

driver.get("https://clutch.co/pk/developers/artificial-intelligence")
driver.maximize_window()
csv_file = "data.csv"
if not os.path.exists(csv_file):
    # Create the CSV file and write column headers
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['names', 'locations'])
    print(f"CSV file '{csv_file}' created successfully.")

driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyButtonAccept"]')
close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="CybotCookiebotDialogBodyButtonAccept"]')))
close.click()
names = []
locations = []
for page in range(4):
    j = driver.find_elements(By.XPATH, f'//a[@class="company_title directory_profile"]')
    k = len(j)
    name = driver.find_elements(By.XPATH, f'(//*[@class="company col-md-12 prompt-target"]/h3)')
    location = driver.find_elements(By.XPATH,f'(//span[@class="locality"])')
    if len(location)> 50:
        location = location[2:]
    for ii,jj in zip(name, location):
        names.append(ii.text)
        locations.append(jj.text)
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ii.text, jj.text])
    WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '(//*[@class = "pagination justify-content-center"]/li)[5]'))).click()

print(len(names))
print(len(locations))

