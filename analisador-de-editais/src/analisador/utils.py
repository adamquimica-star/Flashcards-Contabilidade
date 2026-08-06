"""Funções utilitárias compartilhadas entre as etapas."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def salvar_texto(caminho: Path, conteudo: str) -> Path:
    """Grava texto em UTF-8, criando as pastas necessárias."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(conteudo, encoding="utf-8")
    return caminho


def salvar_json(caminho: Path, dados: Any) -> Path:
    """Grava dados como JSON legível (indentado, UTF-8)."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return caminho


def ler_json(caminho: Path) -> Any:
    """Lê um arquivo JSON."""
    return json.loads(Path(caminho).read_text(encoding="utf-8"))
