"""Etapa 2 — Análise dos pontos importantes.

ENTRADA: texto bruto do edital.
SAÍDA:   objeto PontosImportantes (dados-chave estruturados).
"""

from __future__ import annotations

from ..config import Config
from ..modelos import PontosImportantes


def analisar(config: Config, texto_edital: str) -> PontosImportantes:
    """Extrai os pontos importantes do edital usando a IA.

    Passos (a implementar):
      1. Carregar o prompt: ia.carregar_prompt("02_pontos_importantes.md").
      2. Chamar ia.perguntar(config, prompt_sistema, texto_edital),
         pedindo a saída em JSON.
      3. Fazer o parse do JSON para um objeto PontosImportantes.
      4. Retornar o objeto (e opcionalmente salvar em data/processado/).
    """
    raise NotImplementedError(
        "e02_pontos_importantes.analisar ainda não implementado."
    )
