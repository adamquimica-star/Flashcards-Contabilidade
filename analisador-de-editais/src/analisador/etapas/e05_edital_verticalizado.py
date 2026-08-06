"""Etapa 5 — Edital verticalizado.

ENTRADA: lista de Disciplina (conteúdo programático).
SAÍDA:   Markdown hierárquico (disciplina → tópico → subtópico) com checkboxes.
"""

from __future__ import annotations

from ..config import Config
from ..modelos import Disciplina


def verticalizar(config: Config, disciplinas: list[Disciplina]) -> str:
    """Transforma o conteúdo programático em um edital verticalizado.

    Passos (a implementar):
      1. Para cada disciplina, quebrar os tópicos em subtópicos atômicos
         (pode usar IA com o prompt "05_edital_verticalizado.md").
      2. Renderizar em Markdown com caixas de marcação, ex.:
             ## Contabilidade
             - [ ] 1. Conceito e objeto
               - [ ] 1.1 Patrimônio
      3. Retornar a string (e salvar em data/saida/verticalizado.md).
    """
    raise NotImplementedError(
        "e05_edital_verticalizado.verticalizar ainda não implementado."
    )
