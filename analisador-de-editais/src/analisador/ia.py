"""Wrapper do cliente da Claude — ponto único de contato com a API de IA.

Centralizar aqui facilita trocar o modelo, adicionar cache, logs e tratamento
de erro sem mexer nas etapas.

TODO: implementar a chamada real com o SDK `anthropic`.
"""

from __future__ import annotations

from .config import Config


def perguntar(
    config: Config,
    prompt_sistema: str,
    prompt_usuario: str,
) -> str:
    """Envia um prompt à Claude e devolve o texto da resposta.

    Passos (a implementar):
      1. Criar o cliente: `anthropic.Anthropic(api_key=config.anthropic_api_key)`.
      2. Chamar `client.messages.create(model=config.modelo, system=prompt_sistema,
         messages=[{"role": "user", "content": prompt_usuario}], max_tokens=...,
         temperature=config.temperatura)`.
      3. Extrair e retornar `resposta.content[0].text`.
      4. Tratar erros de rede/limite (retry com backoff).
    """
    raise NotImplementedError(
        "ia.perguntar ainda não implementado — ver docstring para os passos."
    )


def carregar_prompt(nome_arquivo: str) -> str:
    """Lê um arquivo de prompt da pasta prompts/ e retorna seu conteúdo.

    Ex.: carregar_prompt("02_pontos_importantes.md")
    """
    from pathlib import Path

    caminho = Path(__file__).resolve().parents[2] / "prompts" / nome_arquivo
    return caminho.read_text(encoding="utf-8")
