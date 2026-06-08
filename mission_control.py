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