"""Ponto de entrada do Analisador de Editais.

Uso (quando implementado):
    python cli.py analisar data/entrada/edital.pdf      # pipeline completo
    python cli.py etapa pontos data/entrada/edital.pdf  # uma etapa só

Este é o esqueleto: a estrutura de comandos existe; as etapas ainda lançam
NotImplementedError até serem implementadas.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite `import analisador` rodando a partir da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from analisador.config import carregar_config  # noqa: E402
from analisador import pipeline  # noqa: E402


def cmd_analisar(args: argparse.Namespace) -> int:
    config = carregar_config()
    pdf = Path(args.pdf)
    if not pdf.exists():
        print(f"❌ Arquivo não encontrado: {pdf}")
        return 1
    print(f"▶️  Analisando edital: {pdf.name}")
    pipeline.analisar_edital(config, pdf)
    print("✅ Concluído. Veja os resultados em data/saida/")
    return 0


def cmd_etapa(args: argparse.Namespace) -> int:
    print(f"▶️  Rodando etapa isolada: {args.nome} sobre {args.pdf}")
    # TODO: despachar para a etapa correspondente conforme args.nome
    print("ℹ️  Etapas isoladas ainda não conectadas — ver src/analisador/etapas/.")
    return 0


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="analisador-de-editais",
        description="Analisa o PDF de um edital de concurso e gera material.",
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    p_analisar = sub.add_parser("analisar", help="Roda o pipeline completo.")
    p_analisar.add_argument("pdf", help="Caminho para o PDF do edital.")
    p_analisar.set_defaults(func=cmd_analisar)

    p_etapa = sub.add_parser("etapa", help="Roda uma etapa isolada.")
    p_etapa.add_argument(
        "nome",
        choices=[
            "ingestao", "pontos", "documento", "conteudo",
            "verticalizado", "criativos", "banco",
        ],
        help="Nome da etapa.",
    )
    p_etapa.add_argument("pdf", help="Caminho para o PDF do edital.")
    p_etapa.set_defaults(func=cmd_etapa)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
