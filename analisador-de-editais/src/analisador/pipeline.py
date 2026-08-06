"""Orquestrador — roda as etapas na ordem do fluxo.

    PDF ─▶ ingestão ─▶ pontos ─▶ documento ─▶ conteúdo programático
                          │                          │
                          └▶ criativos               └▶ verticalizado ─▶ banco de questões

Cada etapa é chamada aqui, passando adiante o resultado da anterior.
"""

from __future__ import annotations

from pathlib import Path

from .config import Config
from .modelos import Edital
from .etapas import (
    e01_ingestao,
    e02_pontos_importantes,
    e03_documento,
    e04_conteudo_programatico,
    e05_edital_verticalizado,
    e06_criativos,
    e07_banco_questoes,
)


def analisar_edital(config: Config, caminho_pdf: Path) -> Edital:
    """Executa o pipeline completo sobre um PDF de edital.

    Retorna um objeto Edital com todos os resultados. Cada etapa abaixo já
    tem seu módulo — basta implementá-las uma a uma.
    """
    edital = Edital(arquivo_origem=str(caminho_pdf))

    # 1. Ingestão: PDF -> texto
    edital.texto_bruto = e01_ingestao.extrair_texto(caminho_pdf)

    # 2. Pontos importantes
    edital.pontos = e02_pontos_importantes.analisar(config, edital.texto_bruto)

    # 3. Documento dos pontos importantes
    e03_documento.gerar_documento(edital.pontos)

    # (ramo lateral) 6. Criativos para redes sociais
    edital.criativos = e06_criativos.gerar_criativos(config, edital.pontos)

    # 4. Conteúdo programático
    edital.conteudo_programatico = e04_conteudo_programatico.analisar(
        config, edital.texto_bruto
    )

    # 5. Edital verticalizado
    e05_edital_verticalizado.verticalizar(config, edital.conteudo_programatico)

    # 7. Banco de questões consolidado por matéria
    e07_banco_questoes.consolidar(config, edital.conteudo_programatico)

    return edital
