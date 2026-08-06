"""Etapa 6 — Criativos para redes sociais (ramo lateral do fluxo).

ENTRADA: PontosImportantes (e, opcionalmente, o conteúdo programático).
SAÍDA:   lista de Criativo (peças de Feed e Stories).
"""

from __future__ import annotations

from ..config import Config
from ..modelos import Criativo, PontosImportantes


def gerar_criativos(
    config: Config,
    pontos: PontosImportantes,
    formatos: list[str] | None = None,
) -> list[Criativo]:
    """Gera textos/roteiros para postagem (Feed e Stories).

    Passos (a implementar):
      1. Definir os formatos desejados (default: ["feed", "stories"]).
      2. Carregar o prompt "06_criativos.md" e injetar tom/hashtags do settings.
      3. Para cada formato, chamar a IA pedindo título, texto, legenda e hashtags.
      4. Converter para objetos Criativo e retornar
         (e salvar em data/saida/criativos/).
    """
    raise NotImplementedError(
        "e06_criativos.gerar_criativos ainda não implementado."
    )
