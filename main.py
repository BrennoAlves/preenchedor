from playwright.sync_api import Playwright, sync_playwright
import random


def roletaIdade():
    idades = ["Abaixo dos 19 anos", "Entre 18 e 20 anos", "Entre 21 e 25 anos", "Entre 26 e 30 anos", "Entre 30 e 35 anos", "Entre 40 e 45 anos", "Entre 45 e 50 anos", "Entre 55 e 60 anos", "Mais do que 60 anos"]
    pesos = [1, 1.2, 1.2, 1, 1, 1, 1, 1, 1]
    idadeRoletada = random.choices(idades, weights=pesos, k=1)
    return idadeRoletada[0]

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://docs.google.com/forms/d/e/1FAIpQLSeyAtCtdop1EfcStNz6Lee6LzqdRNI1HHNpDwHkseHXVGuOeQ/viewform")
        
    #sorteando idade
    page.get_by_text(roletaIdade()).click()


    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
