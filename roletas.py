import random

def roletaIdade():
    idades = ["Abaixo dos 19 anos", "Entre 18 e 20 anos", "Entre 21 e 25 anos", "Entre 26 e 30 anos", "Entre 30 e 35 anos", "Entre 40 e 45 anos", "Entre 45 e 50 anos", "Entre 55 e 60 anos", "Mais do que 60 anos"]
    pesos = [1, 1.2, 1.2, 1, 1, 1, 1, 1, 1]
    idadeRoletada = random.choices(idades, weights=pesos, k=1)
    return idadeRoletada[0]

def roletaRenda():
    rendas = ["Abaixo de 1 salário mínimo", "Entre 18 e 20 anos", "Entre 21 e 25 anos", "Entre 26 e 30 anos", "Entre 30 e 35 anos", "Entre 40 e 45 anos", "Entre 45 e 50 anos", "Entre 55 e 60 anos", "Mais do que 60 anos"]
    pesos = [1, 1.2, 1.2, 1, 1, 1, 1, 1, 1] 
    rendaRoletada = random.choices(rendas, weights=pesos, k=1)
    return rendaRoletada[0]

def roletaTreinamento():
    treinamento = ["Sim","Não"]
    pesos = [1,2]
    treinamentoRoletado = random.choices(treinamento, weights=pesos, k=1)
    return treinamentoRoletado

def roletaPagamento():
    pagamentos = ["Menos que 70 reais", "Entre 70 e 80 reais", "Entre 81 e 90 reais", "Entre 91 e 100 reais", "Entre 101 e 110 reais", "Acima de 111 reais"]
    pesos = [1, 1, 1, 1, 1, 1]
    pagamentoRoletado = random.choices(pagamentos, weights=pesos, k=1)
    return pagamentoRoletado

def roletaHorario():
    horarios = ["Antes das 6:00 horas", "Entre 6:00 e 8:00", "Entre 8:00 e 12:00", "Entre 12:00 e 18:00", "Entre 18:00 e 22:00", "Entre 22:00 e 00:00"]
    pesos = [1, 1, 1, 1, 1, 1]
    horarioRoletado = random.choices(horarios, weights=pesos, k=1)
    return horarioRoletado

def roletaRecorrencia():
    recorrencias = ["1 vez por semana", "2 vezes por semana", "3 vezes por semana", "4 vezes por semana", "5 vezes por semana", "6 vezes por semana", "7 vezes por semana"]
    pesos = [1, 1, 1, 1, 1, 1, 1]
    recorrenciaRoleta = random.choices(recorrencias, weights=pesos, k=1)
    return recorrenciaRoleta

def aumentarRecorrencia():
    aumentarRec = ["Maior disponibilidade de horário", "Oferecer descontos para usuários frequentes", "Ampliar a variedade de aulas e atividades", "Investir na modernização e ampliação das instalações", "Realizar desafios de superação com prêmios atrativos", "Estou satisfeito com a minha frequência"]
    pesos = [1, 1, 1, 1, 1, 1]
    aumentarRecRoleta = random.choices(aumentarRec, weights=pesos, k=1)
    return aumentarRecRoleta
