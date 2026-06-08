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


# ============================================================
# LOOP PRINCIPAL — ANÁLISE DOS CICLOS
# ============================================================

def executar_missao():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    riscos = []
    pontuacoes_por_area = [0, 0, 0, 0, 0]

    for i, ciclo in enumerate(dados_missao):
        temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

        status_temp,  pts_temp,  desc_temp  = analisar_temperatura(temperatura)
        status_com,   pts_com,   desc_com   = analisar_comunicacao(comunicacao)
        status_bat,   pts_bat,   desc_bat   = analisar_bateria(bateria)
        status_oxi,   pts_oxi,   desc_oxi   = analisar_oxigenio(oxigenio)
        status_est,   pts_est,   desc_est   = analisar_estabilidade(estabilidade)

        pontuacao_ciclo = pts_temp + pts_com + pts_bat + pts_oxi + pts_est
        riscos.append(pontuacao_ciclo)

        pontuacoes_por_area[0] += pts_temp
        pontuacoes_por_area[1] += pts_com
        pontuacoes_por_area[2] += pts_bat
        pontuacoes_por_area[3] += pts_oxi
        pontuacoes_por_area[4] += pts_est

        classificacao = classificar_ciclo(pontuacao_ciclo)

        alertas_criticos = []
        if status_temp == "CRÍTICO":
            alertas_criticos.append("Temperatura interna")
        if status_com == "CRÍTICO":
            alertas_criticos.append("Comunicação com a base")
        if status_bat == "CRÍTICO":
            alertas_criticos.append("Sistema de energia")
        if status_oxi == "CRÍTICO":
            alertas_criticos.append("Suporte de oxigênio")
        if status_est == "CRÍTICO":
            alertas_criticos.append("Estabilidade operacional")

        recomendacao = gerar_recomendacao(classificacao, alertas_criticos)

        print(f"\nCICLO {i + 1}")
        print("-" * 60)
        print(f"Temperatura:  {temperatura} °C | {status_temp} | {desc_temp}")
        print(f"Comunicação:  {comunicacao}%  | {status_com} | {desc_com}")
        print(f"Bateria:      {bateria}%  | {status_bat} | {desc_bat}")
        print(f"Oxigênio:     {oxigenio}%  | {status_oxi} | {desc_oxi}")
        print(f"Estabilidade: {estabilidade}%  | {status_est} | {desc_est}")
        print(f"\nPontuação de risco do ciclo: {pontuacao_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

    return riscos, pontuacoes_por_area


# ============================================================
# RELATÓRIO FINAL
# ============================================================

def gerar_relatorio_final(riscos, pontuacoes_por_area):
    total_ciclos = len(dados_missao)
    medias = []
    for col in range(5):
        total = 0
        for linha in dados_missao:
            total += linha[col]
        medias.append(total / total_ciclos)

    ciclo_critico = riscos.index(max(riscos)) + 1
    risco_medio = sum(riscos) / total_ciclos
    ciclos_criticos = sum(1 for r in riscos if r >= 6)
    tendencia = analisar_tendencia(riscos)
    area_afetada, pontos_area = identificar_area_mais_afetada(pontuacoes_por_area)
    classificacao_final = classificar_ciclo(round(risco_medio))

    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"\nQuantidade de ciclos analisados: {total_ciclos}")
    print(f"Média de temperatura:   {medias[0]:.2f} °C")
    print(f"Média de comunicação:   {medias[1]:.2f}%")
    print(f"Média de bateria:       {medias[2]:.2f}%")
    print(f"Média de oxigênio:      {medias[3]:.2f}%")
    print(f"Média de estabilidade:  {medias[4]:.2f}%")
    print(f"\nCiclo mais crítico: Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {max(riscos)}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {ciclos_criticos}")
    print("\nTendência da missão:")
    print(tendencia)
    print("\nPontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontuacoes_por_area[i]} pontos")
    print(f"\nÁrea mais afetada: {area_afetada}")
    print(f"\nClassificação final da missão: {classificacao_final}")
    print("\nConclusão:")
    if classificacao_final == "MISSÃO CRÍTICA":
        print("A missão enfrentou situação crítica severa. Protocolo de emergência deve permanecer ativo.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("A missão apresentou instabilidade relevante durante a operação. A equipe deve manter o plano de contingência ativo.")
    else:
        print("A missão foi concluída com estabilidade. Sistemas operando dentro dos parâmetros normais.")
    print("=" * 60)


# ============================================================
# EXECUÇÃO
# ============================================================

riscos, pontuacoes_por_area = executar_missao()
gerar_relatorio_final(riscos, pontuacoes_por_area)