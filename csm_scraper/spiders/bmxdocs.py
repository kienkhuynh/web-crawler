import scrapy
from selenium import webdriver
import io
class QuotesSpider(scrapy.Spider):
    name = "bmxdocs"
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.start_urls = [
            'http://console.bluemix.net/docs'
        ] 

    def parse(self, response):
        file_name = self.name + ".html"
        timeout = 20
        try:
            wait = WebDriverWait(browser, timeout)
            wait.until(EC.visibility_of_element_located((By.XPATH, “//a[@class="tile__item")))
        except TimeoutException:
            print(“Timed out waiting for page to load”)
            browser.quit()

        
        #complete_name = os.path.join(save_path, file_name)
        #file_object = codecs.open(file_name, "w", "utf-8")
        #html = self.driver.page_source
        #file_object.write(html)
        ''' while True:
            next = self.driver. find_element_by_xpath('//td[@class="pagn-next"]/a')

            try:
                next.click()

                # get the data and write it to scrapy items
            except:
                break

        self.driver.close()'''