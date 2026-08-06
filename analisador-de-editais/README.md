# 📑 Analisador de Editais

Programa que recebe o **PDF de um edital de concurso público** e produz, de forma
automatizada, todo o material de estudo e de divulgação a partir dele.

> Projeto **independente**. Não depende do app de flashcards que vive na raiz
> deste repositório — pode inclusive ser movido para um repositório próprio depois.

---

## 🔁 O fluxo (do esboço)

```
PDF do Edital
   │
   ▼
1. ANÁLISE  ──▶  Pontos importantes
   │
   ▼
2. DOCUMENTO  ──▶  Os pontos importantes organizados
   │                     │
   │                     └──▶ 3. CRIATIVOS p/ redes sociais (Feed + Stories)
   ▼
4. ANÁLISE do Conteúdo Programático
   │
   ▼
5. EDITAL VERTICALIZADO (todo o conteúdo, hierarquizado)
   │
   ▼
6. ANÁLISE de Bancos de questões (construídos + consolidados por matéria)
```

Cada etapa é um módulo isolado em `src/analisador/etapas/`. Elas podem rodar
sozinhas ou em sequência (orquestradas por `pipeline.py`).

| # | Etapa | Módulo | Entrada | Saída |
|---|-------|--------|---------|-------|
| 1 | Ingestão do PDF | `e01_ingestao.py` | PDF do edital | Texto bruto |
| 2 | Pontos importantes | `e02_pontos_importantes.py` | Texto | JSON estruturado (vagas, datas, taxa, banca, cargos, requisitos…) |
| 3 | Documento | `e03_documento.py` | Pontos (JSON) | Documento em Markdown |
| 4 | Conteúdo programático | `e04_conteudo_programatico.py` | Texto | Disciplinas e tópicos |
| 5 | Edital verticalizado | `e05_edital_verticalizado.py` | Conteúdo programático | Hierarquia disciplina → tópico → subtópico |
| 6 | Criativos p/ redes | `e06_criativos.py` | Pontos + conteúdo | Textos de Feed e Stories |
| 7 | Banco de questões | `e07_banco_questoes.py` | Edital verticalizado | Questões consolidadas por matéria |

---

## 🗂️ Estrutura de pastas

```
analisador-de-editais/
├── README.md               ← este arquivo
├── requirements.txt        ← dependências Python
├── .env.example            ← modelo de variáveis de ambiente (chave da API)
├── .gitignore
├── cli.py                  ← ponto de entrada: python cli.py ...
├── config/
│   └── settings.example.yaml
├── prompts/                ← prompts de IA de cada etapa (edite à vontade)
│   ├── 02_pontos_importantes.md
│   ├── 04_conteudo_programatico.md
│   ├── 05_edital_verticalizado.md
│   ├── 06_criativos.md
│   └── 07_banco_questoes.md
├── data/
│   ├── entrada/            ← coloque aqui os PDFs dos editais
│   ├── processado/         ← arquivos intermediários (texto, JSON)
│   └── saida/              ← resultados finais
├── docs/
│   └── fluxo.md            ← o fluxo desenhado, transcrito + diagrama
└── src/
    └── analisador/
        ├── config.py       ← carrega settings + .env
        ├── ia.py           ← wrapper do cliente Claude
        ├── modelos.py      ← estruturas de dados (Edital, Disciplina…)
        ├── pipeline.py     ← orquestra as etapas na ordem do fluxo
        ├── utils.py
        └── etapas/
            ├── e01_ingestao.py
            ├── e02_pontos_importantes.py
            ├── e03_documento.py
            ├── e04_conteudo_programatico.py
            ├── e05_edital_verticalizado.py
            ├── e06_criativos.py
            └── e07_banco_questoes.py
```

---

## 🚧 Status

**Esqueleto estruturado.** Os arquivos existem com a assinatura das funções,
a documentação de cada etapa e marcações `TODO` do que falta implementar. Nada
"faz" ainda — é o mapa para preencher.

## 🚀 Como será usado (quando implementado)

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Configurar a chave da API
cp .env.example .env        # e preencha ANTHROPIC_API_KEY

# 3. Rodar o pipeline completo sobre um edital
python cli.py analisar data/entrada/edital.pdf

# ou rodar só uma etapa
python cli.py etapa pontos data/entrada/edital.pdf
```

## 🧭 Próximos passos sugeridos

1. Implementar a **etapa 1 (ingestão)** — extrair texto do PDF (e OCR se escaneado).
2. Implementar a **etapa 2 (pontos importantes)** com a API da Claude.
3. Seguir etapa a etapa, testando com um edital real em `data/entrada/`.
