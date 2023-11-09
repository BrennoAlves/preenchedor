from playwright.sync_api import Playwright, sync_playwright
import roletas

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://docs.google.com/forms/d/e/1FAIpQLSeyAtCtdop1EfcStNz6Lee6LzqdRNI1HHNpDwHkseHXVGuOeQ/viewform")
        
    #sorteando idade
    page.get_by_text(roletas.roletaIdade()).click()

    #sorteando renda
    page.get_by_text(roletas.roletaRenda()).click()

    #sorteando se treina ou não
    b = roletas.roletaTreinamento()
    page.get_by_text(b).click()

    #passando de pagina
    page.get_by_role("button", name="Próxima").click()
    if b == "Sim":
        



    #enviar o forms
    page.get_by_role("button", name="Enviar").click()
    
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
