"""Estruturas de dados que trafegam entre as etapas do pipeline.

São `dataclasses` simples — servem de contrato entre as etapas. Ajuste os campos
conforme a realidade dos editais que você analisa.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PontosImportantes:
    """Etapa 2 — dados-chave extraídos do edital."""

    banca: str = ""
    orgao: str = ""
    cargos: list[str] = field(default_factory=list)
    vagas: int | None = None
    remuneracao: str = ""
    escolaridade: str = ""
    taxa_inscricao: str = ""
    periodo_inscricao: str = ""
    data_prova: str = ""
    requisitos: list[str] = field(default_factory=list)
    observacoes: str = ""


@dataclass
class Topico:
    """Um tópico (e seus subtópicos) dentro de uma disciplina."""

    titulo: str = ""
    subtopicos: list[str] = field(default_factory=list)


@dataclass
class Disciplina:
    """Etapa 4/5 — uma disciplina do conteúdo programático."""

    nome: str = ""
    topicos: list[Topico] = field(default_factory=list)


@dataclass
class Criativo:
    """Etapa 6 — uma peça para redes sociais."""

    formato: str = ""      # "feed" ou "stories"
    titulo: str = ""
    texto: str = ""
    legenda: str = ""
    hashtags: list[str] = field(default_factory=list)


@dataclass
class Edital:
    """Objeto agregador — o resultado completo da análise de um edital."""

    arquivo_origem: str = ""
    texto_bruto: str = ""
    pontos: PontosImportantes | None = None
    conteudo_programatico: list[Disciplina] = field(default_factory=list)
    criativos: list[Criativo] = field(default_factory=list)
