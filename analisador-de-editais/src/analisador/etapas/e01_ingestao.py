"""Etapa 1 — Ingestão do PDF do edital.

ENTRADA: caminho para o PDF do edital.
SAÍDA:   texto bruto do edital (str), também salvo em data/processado/.
"""

from __future__ import annotations

from pathlib import Path


def extrair_texto(caminho_pdf: Path) -> str:
    """Extrai o texto de um PDF de edital.

    Passos (a implementar):
      1. Abrir o PDF com `pypdf` (ou `pdfplumber` p/ layout/tabelas).
      2. Concatenar o texto de todas as páginas.
      3. Se o PDF for escaneado (texto vazio), cair para OCR
         (pytesseract + pdf2image) — opcional.
      4. Limpar (remover cabeçalhos/rodapés repetidos, normalizar espaços).
      5. Retornar o texto e salvar em data/processado/<nome>.txt.
    """
    raise NotImplementedError(
        "e01_ingestao.extrair_texto ainda não implementado."
    )
