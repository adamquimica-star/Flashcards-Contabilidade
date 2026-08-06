"""Etapa 4 — Análise do conteúdo programático.

ENTRADA: texto bruto do edital.
SAÍDA:   lista de Disciplina (com seus tópicos).
"""

from __future__ import annotations

from ..config import Config
from ..modelos import Disciplina


def analisar(config: Config, texto_edital: str) -> list[Disciplina]:
    """Identifica as disciplinas e tópicos cobrados no edital.

    Passos (a implementar):
      1. Localizar a seção de conteúdo programático / anexo (heurística ou IA).
      2. Carregar o prompt "04_conteudo_programatico.md".
      3. Chamar a IA pedindo a lista de disciplinas e tópicos em JSON.
      4. Converter para list[Disciplina] e retornar.
    """
    raise NotImplementedError(
        "e04_conteudo_programatico.analisar ainda não implementado."
    )
