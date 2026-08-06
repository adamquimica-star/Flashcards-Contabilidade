"""Testes da etapa 1 (ingestão).

Rodar da raiz do projeto:
    python -m pytest            # se tiver pytest
    python tests/test_e01_ingestao.py   # execução direta (sem pytest)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from analisador.etapas import e01_ingestao  # noqa: E402


def test_limpar_texto_une_hifenizacao():
    entrada = "conta-\nbilidade"
    assert e01_ingestao.limpar_texto(entrada) == "contabilidade"


def test_limpar_texto_colapsa_espacos():
    assert e01_ingestao.limpar_texto("a    b\t\tc") == "a b c"


def test_limpar_texto_limita_linhas_em_branco():
    assert e01_ingestao.limpar_texto("a\n\n\n\n\nb") == "a\n\nb"


def test_extrair_texto_arquivo_inexistente():
    try:
        e01_ingestao.extrair_texto("/caminho/que/nao/existe.pdf")
    except FileNotFoundError:
        return
    raise AssertionError("esperava FileNotFoundError")


if __name__ == "__main__":
    falhas = 0
    for nome, func in list(globals().items()):
        if nome.startswith("test_") and callable(func):
            try:
                func()
                print(f"✓ {nome}")
            except Exception as erro:  # noqa: BLE001
                falhas += 1
                print(f"✗ {nome}: {erro}")
    raise SystemExit(1 if falhas else 0)
