"""Configuração central: carrega variáveis de ambiente (.env) e settings.yaml.

TODO: implementar a leitura real. Este é o esqueleto.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

# Raiz do projeto (analisador-de-editais/)
RAIZ = Path(__file__).resolve().parents[2]


@dataclass
class Config:
    """Configurações efetivas do programa."""

    anthropic_api_key: str = ""
    modelo: str = "claude-sonnet-5"
    temperatura: float = 0.2
    max_tokens: int = 4096

    pasta_entrada: Path = field(default_factory=lambda: RAIZ / "data" / "entrada")
    pasta_processado: Path = field(default_factory=lambda: RAIZ / "data" / "processado")
    pasta_saida: Path = field(default_factory=lambda: RAIZ / "data" / "saida")


def carregar_config() -> Config:
    """Carrega a configuração a partir de .env e config/settings.yaml.

    Passos (a implementar):
      1. Carregar o .env (python-dotenv) para popular os os.environ.
      2. Ler config/settings.yaml (se existir) com pyyaml.
      3. Mesclar: valores do .env têm prioridade para segredos; o YAML define o resto.
      4. Retornar um objeto Config preenchido.
    """
    # Esqueleto: por ora só lê o essencial do ambiente.
    return Config(
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY", ""),
        modelo=os.environ.get("ANALISADOR_MODELO", "claude-sonnet-5"),
    )
    # TODO: mesclar com config/settings.yaml
