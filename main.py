from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def configurarDriver():
    options = Options()
    options.add_argument("--incognito")
    #options.add_argument("--headless")
    return webdriver.Chrome(options=options)

if __name__ == "__main__":
    browser = configurarDriver()
    url = "https://forms.gle/FoAoauz53Xy7A4n68"
    browser.get(url)
    elemento = browser.find_element("css selector", "[aria-label='opções da pergunta']")
    print(elemento.text)
    browser.quit()
