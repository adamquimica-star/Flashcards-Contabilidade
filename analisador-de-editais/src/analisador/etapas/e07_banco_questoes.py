"""Etapa 7 — Análise de bancos de questões.

ENTRADA: edital verticalizado (disciplinas/tópicos).
SAÍDA:   questões consolidadas e organizadas por matéria/tópico.

Esta etapa liga o edital ao material de estudo (ex.: alimentar flashcards/quizzes).
"""

from __future__ import annotations

from ..config import Config
from ..modelos import Disciplina


def consolidar(config: Config, disciplinas: list[Disciplina]) -> dict:
    """Consolida/gera questões por matéria a partir do edital verticalizado.

    Passos (a implementar):
      1. Definir a fonte das questões: geradas por IA a partir de cada tópico,
         e/ou importadas de um banco existente (CSV/JSON).
      2. Para cada tópico, associar/gerar N questões (prompt "07_banco_questoes.md").
      3. Consolidar num dicionário { disciplina: { tópico: [questões...] } }.
      4. Retornar (e salvar em data/saida/banco_questoes.json).

    Formato sugerido de cada questão (compatível com quizzes):
        {"q": "...", "c": ["...", "..."], "a": 1, "h": "dica/explicação"}
    """
    raise NotImplementedError(
        "e07_banco_questoes.consolidar ainda não implementado."
    )
