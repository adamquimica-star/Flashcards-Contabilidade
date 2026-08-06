"""Etapa 3 — Documento dos pontos importantes.

ENTRADA: objeto PontosImportantes.
SAÍDA:   documento em Markdown (str), salvo em data/saida/.
"""

from __future__ import annotations

from ..modelos import PontosImportantes


def gerar_documento(pontos: PontosImportantes) -> str:
    """Monta um documento Markdown legível com os pontos importantes.

    Passos (a implementar):
      1. Montar um cabeçalho (órgão, banca, cargo).
      2. Listar em seções: vagas, remuneração, escolaridade, taxa, datas,
         requisitos, observações.
      3. Retornar a string Markdown (e salvar em data/saida/documento.md).

    Obs.: esta etapa é puramente de formatação — não precisa de IA.
    """
    raise NotImplementedError(
        "e03_documento.gerar_documento ainda não implementado."
    )
