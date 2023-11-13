import random

def roletaIdade():
    idades = ["Abaixo dos 19 anos", "Entre 18 e 20 anos", "Entre 21 e 25 anos", "Entre 26 e 30 anos", "Entre 30 e 35 anos", "Entre 40 e 45 anos", "Entre 45 e 50 anos", "Entre 55 e 60 anos", "Mais do que 60 anos"]
    pesos = [1, 1.3, 1.5, 1.4, 1, 1, 1, 1, 1]
    idadeRoletada = random.choices(idades, weights=pesos, k=1)
    return idadeRoletada[0]

def roletaRenda():
    rendas = ["Abaixo de 1 salário mínimo", "Entre 1 e 2 salários mínimos", "Entre 2 e 3 salários mínimos", "Entre 3 e 4 salários minímos", "Entre 4 e 5 salários minímos", "Mais que 5 salários minímos"]
    pesos = [1, 1, 1, 1, 0.8, 0.5] 
    rendaRoletada = random.choices(rendas, weights=pesos, k=1)
    return rendaRoletada[0]

def roletaTreinamento():
    treinamento = ["Sim","Não"]
    pesos = [0.6,1]
    treinamentoRoletado = random.choices(treinamento, weights=pesos, k=1)
    return treinamentoRoletado[0]


#Caminho caso tenha marcado Sim no "Você treina atualmente?"
def roletaPagamento():
    pagamentos = ["Menos que 70 reais", "Entre 70 e 80 reais", "Entre 81 e 90 reais", "Entre 91 e 100 reais", "Entre 101 e 110 reais", "Acima de 111 reais"]
    pesos = [1, 1.5, 1.5, 1, 0.8, 0.8]
    pagamentoRoletado = random.choices(pagamentos, weights=pesos, k=1)
    return pagamentoRoletado[0]

def roletaHorario():
    horarios = ["Antes das 6:00 horas", "Entre 6:00 e 8:00", "Entre 8:00 e 12:00", "Entre 12:00 e 18:00", "Entre 18:00 e 22:00", "Entre 22:00 e 00:00"]
    pesos = [1, 1, 1, 1.2, 1.2, 1]
    horarioRoletado = random.choices(horarios, weights=pesos, k=1)
    return horarioRoletado[0]

def roletaRecorrencia():
    recorrencias = ["1 vez por semana", "2 vezes por semana", "3 vezes por semana", "4 vezes por semana", "5 vezes por semana", "6 vezes por semana", "7 vezes por semana"]
    pesos = [1, 1, 1, 1, 1, 1, 1]
    recorrenciaRoleta = random.choices(recorrencias, weights=pesos, k=1)
    return recorrenciaRoleta[0]

def aumentarRecorrencia():
    aumentarRec = ["Maior disponibilidade de horário", "Oferecer descontos para usuários frequentes", "Ampliar a variedade de aulas e atividades", "Investir na modernização e ampliação das instalações", "Realizar desafios de superação com prêmios atrativos", "Estou satisfeito com a minha frequência"]
    pesos = [2, 1, 1, 1, 1, 0.5]
    aumentarRecRoleta = random.choices(aumentarRec, weights=pesos, k=1)
    return aumentarRecRoleta[0]

#Caminho caso tenha marcado Não no "Você treina atualmente?"

#Por que não treina?
def pqnt():
    porques = ["Falta de interesse", "Horários não atende minha necessidade", "Custo Elevado", "Falta de Conveniência na Localização"]
    pesos = [1,2,1,1]
    pqntRoletado = random.choices(porques, weights=pesos, k=1)
    return pqntRoletado[0]

def disposicaoPagamento():
    disposicao = ["Menos que 70 reais", "Entre 70 e 80 reais", "Entre 81 e 90 reais", "Entre 91 e 100 reais", "Entre 101 e 110 reais", "Acima de 111 reais"]
    pesos = [1, 1, 3, 1, 1, 1]
    disposicaoRoletada = random.choices(disposicao, weights=pesos, k=1)
    return disposicaoRoletada[0]

#usar a mesma roleta de horario