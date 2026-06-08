# ============================================================
# MISSION CONTROL AI — GGT Odyssey
# Pensamento Computacional e Automação com Python
# FIAP Global Solution 2026.1
# Equipe GGT
# Glauco Kelly        — RM: 572840 — Turma: 1CCR
# Gabriel Fagundes    — RM: 569074 — Turma: 1CCR
# Thiago Renatino     — RM: 569073 — Turma: 1CCR
# ============================================================

NOME_MISSAO = "GGT Odyssey"
NOME_EQUIPE = "Equipe GGT"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

dados_missao = [
    [22, 95, 91, 97, 93],  # Ciclo 1 — Lançamento estável
    [26, 88, 80, 95, 87],  # Ciclo 2 — Primeiros sinais de aquecimento
    [31, 72, 65, 92, 74],  # Ciclo 3 — Aquecimento e queda de bateria
    [35, 50, 44, 88, 58],  # Ciclo 4 — Comunicação e energia em atenção
    [38, 33, 26, 81, 42],  # Ciclo 5 — Situação crítica se agravando
    [41, 22, 17, 76, 28],  # Ciclo 6 — Pico crítico — risco máximo
    [36, 48, 31, 82, 45],  # Ciclo 7 — Recuperação parcial
    [29, 68, 52, 89, 63],  # Ciclo 8 — Estabilização progressiva
]

# ============================================================
# FUNÇÕES DE ANÁLISE
# ============================================================

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacoes_por_area):
    maior = max(pontuacoes_por_area)
    indice = pontuacoes_por_area.index(maior)
    return areas_monitoradas[indice], maior


def gerar_recomendacao(classificacao, alertas_criticos):
    if classificacao == "MISSÃO CRÍTICA":
        if len(alertas_criticos) >= 3:
            return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
        recomendacoes = {
            "Temperatura interna": "Verificar controle térmico da missão.",
            "Comunicação com a base": "Tentar restabelecer contato com a base.",
            "Sistema de energia": "Ativar modo de economia de energia.",
            "Suporte de oxigênio": "Acionar protocolo de suporte à vida.",
            "Estabilidade operacional": "Reduzir operações não essenciais."
        }
        for area in alertas_criticos:
            if area in recomendacoes:
                return recomendacoes[area]
    elif classificacao == "MISSÃO EM ATENÇÃO":
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    return "Manter operação normal e continuar monitoramento."