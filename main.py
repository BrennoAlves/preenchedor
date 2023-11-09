from playwright.sync_api import Playwright, sync_playwright
import roletas
import time
import random

# Sorteia um tempo aleatório entre 1 e 3 minutos


# Verifica se o tempo já passou
while True:
    # Faz alguma coisa enquanto espera o tempo acabar
    tempo = random.randint(60, 180)
    time.sleep(tempo)

    #Função
    def run(playwright : Playwright) -> None:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://docs.google.com/forms/d/e/1FAIpQLSeyAtCtdop1EfcStNz6Lee6LzqdRNI1HHNpDwHkseHXVGuOeQ/viewform")


        #sorteando idade
        page.get_by_text(roletas.roletaIdade()).click()

        #sorteando renda
        page.get_by_label(roletas.roletaRenda()).click()

        #sorteando se treina ou não
        b = roletas.roletaTreinamento()
        page.get_by_label(b).click()

        #passando de pagina
        page.get_by_role("button", name="Próxima").click()

        #esperando carregar
        page.wait_for_load_state("load")

        #caminho para a pessoa que já treina
        if b == "Sim":

            #sorteando o valor que a pessoa paga
            page.get_by_text(roletas.roletaPagamento()).click()

            #sorteando o horario que a pessoa frequenta
            page.get_by_text(roletas.roletaHorario()).click()

            #sorteando a recorrencia que pessoa frequenta
            page.get_by_text(roletas.roletaRecorrencia()).click()

            #sorteando o que faria a pessoa aumentar a frequencia
            page.get_by_text(roletas.aumentarRecorrencia()).click()


        #caminho para a pessoa que não treina
        else:

            #sorteando o motivo de não treinar
            page.get_by_text(roletas.pqnt()).click()

            #sorteando o quanto pagaria
            page.get_by_text(roletas.disposicaoPagamento()).click()

        #enviar o forms
        page.get_by_role("button", name="Enviar").click()

        #fechando o navegador
        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)


    print('Concluido')