"""Etapa 1 — Ingestão do PDF do edital.

ENTRADA: caminho para o PDF do edital.
SAÍDA:   texto bruto do edital (str). Se `pasta_processado` for informada,
         também grava o texto em <pasta_processado>/<nome-do-pdf>.txt.

Estratégia de extração:
  1. `pdfplumber` — melhor fidelidade de layout/colunas (preferido).
  2. `pypdf` — fallback mais leve, caso o pdfplumber falhe.
  3. Se ambos devolverem texto vazio, o PDF é provavelmente escaneado
     (imagem) — nesse caso levantamos um erro pedindo OCR.
"""

from __future__ import annotations

import re
from pathlib import Path


class PdfSemTextoError(RuntimeError):
    """PDF sem texto extraível (provavelmente escaneado — requer OCR)."""


def _extrair_com_pdfplumber(caminho_pdf: Path) -> str:
    import pdfplumber

    partes: list[str] = []
    with pdfplumber.open(str(caminho_pdf)) as pdf:
        for pagina in pdf.pages:
            partes.append(pagina.extract_text() or "")
    return "\n".join(partes)


def _extrair_com_pypdf(caminho_pdf: Path) -> str:
    from pypdf import PdfReader

    leitor = PdfReader(str(caminho_pdf))
    partes = [(pagina.extract_text() or "") for pagina in leitor.pages]
    return "\n".join(partes)


def limpar_texto(texto: str) -> str:
    """Normaliza o texto extraído.

    - Junta palavras quebradas por hífen no fim da linha (ex.: "conta-\\nbilidade").
    - Colapsa espaços/tabs repetidos.
    - Remove excesso de linhas em branco (máx. 2 seguidas).
    """
    # une hifenização de fim de linha: "palavra-\n" -> "palavra"
    texto = re.sub(r"-\n(?=\w)", "", texto)
    # normaliza espaços horizontais
    texto = re.sub(r"[ \t]+", " ", texto)
    # tira espaços à direita de cada linha
    texto = re.sub(r" +\n", "\n", texto)
    # no máximo 2 quebras seguidas
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


def extrair_texto(
    caminho_pdf: str | Path,
    pasta_processado: str | Path | None = None,
) -> str:
    """Extrai o texto de um PDF de edital.

    Args:
        caminho_pdf: caminho do PDF a ler.
        pasta_processado: se informado, grava o texto em
            <pasta_processado>/<nome>.txt.

    Returns:
        O texto do edital, já limpo.

    Raises:
        FileNotFoundError: se o PDF não existir.
        PdfSemTextoError: se não houver texto extraível (PDF escaneado).
    """
    caminho_pdf = Path(caminho_pdf)
    if not caminho_pdf.exists():
        raise FileNotFoundError(f"PDF não encontrado: {caminho_pdf}")

    texto = ""
    try:
        texto = _extrair_com_pdfplumber(caminho_pdf)
    except Exception:
        texto = ""

    if not texto.strip():
        # fallback para pypdf
        try:
            texto = _extrair_com_pypdf(caminho_pdf)
        except Exception:
            texto = ""

    if not texto.strip():
        raise PdfSemTextoError(
            f"Não foi possível extrair texto de '{caminho_pdf.name}'. "
            "O PDF provavelmente é escaneado (imagem). "
            "Habilite o OCR (pytesseract + pdf2image) para tratá-lo."
        )

    texto = limpar_texto(texto)

    if pasta_processado is not None:
        pasta_processado = Path(pasta_processado)
        pasta_processado.mkdir(parents=True, exist_ok=True)
        destino = pasta_processado / f"{caminho_pdf.stem}.txt"
        destino.write_text(texto, encoding="utf-8")

    return texto
