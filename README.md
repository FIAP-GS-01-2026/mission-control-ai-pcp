# Mission Control AI — GGT Odyssey

Sistema de monitoramento inteligente de missão espacial desenvolvido em Python.

**Disciplina:** Pensamento Computacional e Automação com Python  
**Instituição:** FIAP — Global Solution 2026.1  
**Equipe:** Equipe GGT  

| Integrante | RM | Turma |
|---|---|---|
| Glauco Kelly | 572840 | 1CCR |
| Gabriel Fagundes | 569074 | 1CCR |
| Thiago Renatino | 569073 | 1CCR |

---

## Sobre o projeto

O Mission Control AI simula o monitoramento de uma missão espacial experimental chamada **GGT Odyssey**, um satélite GNSS que passa por 8 ciclos de operação: desde o lançamento estável até uma crise crítica e posterior recuperação.

O sistema analisa 5 sensores por ciclo, calcula o risco, classifica a situação da missão e gera um relatório final completo.

---

## Como executar

```bash
python3 mission_control.py
```

Não requer instalação de bibliotecas externas. Compatível com Python 3.x.

---

## Regras de alerta

### Temperatura (°C)

| Condição | Classificação |
|---|---|
| Menor que 18 °C | ATENÇÃO |
| De 18 °C até 30 °C | NORMAL |
| Maior que 30 °C até 35 °C | ATENÇÃO |
| Maior que 35 °C | CRÍTICO |

### Comunicação (%)

| Condição | Classificação |
|---|---|
| Menor que 30% | CRÍTICO |
| De 30% até 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

### Bateria (%)

| Condição | Classificação |
|---|---|
| Menor que 20% | CRÍTICO |
| De 20% até 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

### Oxigênio (%)

| Condição | Classificação |
|---|---|
| Menor que 80% | CRÍTICO |
| De 80% até 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

### Estabilidade (%)

| Condição | Classificação |
|---|---|
| Menor que 40% | CRÍTICO |
| De 40% até 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

---

## Pontuação de risco

| Classificação | Pontos |
|---|---|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

| Pontuação total | Classificação do ciclo |
|---|---|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

## Estrutura do repositório

```
mission-control-ai-pcp/
├── README.md
└── mission_control.py

```

## Vídeo pitch

[Link do vídeo no YouTube](https://youtube.com)