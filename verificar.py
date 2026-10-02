"""Verificador de formato. Não diz se as respostas estão certas.

Uso: python verificar.py   (na pasta com respostas.json e progress.md)
"""
import json
import re
import sys
from pathlib import Path

TETO = 350
MODOS = {"poisoning", "distraction", "confusion", "clash"}
TECNICAS = {"write", "select", "compress", "isolate"}
SECOES = {
    "Objetivo": r"^#{1,6}\s*(objetivo|meta)",
    "Abordagem": r"^#{1,6}\s*(abordagem|estrat[eé]gia)",
    "Passos concluídos": r"^#{1,6}\s*(passos|etapas|feito|conclu)",
    "Falha atual": r"^#{1,6}\s*(falha|erro|problema)",
}


def tokens(texto):
    return len(re.findall(r"\w+|[^\w\s]", texto, flags=re.UNICODE))


def parte_a(pasta):
    erros = []
    f = pasta / "respostas.json"
    if not f.exists():
        return ["respostas.json não encontrado"]
    try:
        dados = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"respostas.json não é JSON válido: {e}"]
    casos = dados.get("casos", {})
    for i in range(1, 7):
        c = casos.get(str(i))
        if not isinstance(c, dict):
            erros.append(f"caso {i}: ausente")
            continue
        if str(c.get("modo_falha", "")).strip().lower() not in MODOS:
            erros.append(f"caso {i}: modo_falha inválido")
        if str(c.get("tecnica", "")).strip().lower() not in TECNICAS:
            erros.append(f"caso {i}: tecnica inválida")
        arq = pasta / "casos" / f"caso{i}.txt"
        n = len(arq.read_text(encoding="utf-8").splitlines()) if arq.exists() else None
        ln = c.get("linha_evidencia")
        if not isinstance(ln, int) or ln < 1 or (n and ln > n):
            erros.append(f"caso {i}: linha_evidencia deve ser um inteiro de 1 a {n or 'N'}")
    return erros


def parte_b(pasta):
    erros = []
    f = pasta / "progress.md"
    if not f.exists():
        return ["progress.md não encontrado"], 0
    texto = f.read_text(encoding="utf-8")
    n = tokens(texto)
    if n > TETO:
        erros.append(f"progress.md tem {n} tokens, o limite é {TETO}")
    linhas = texto.splitlines()
    for nome, rx in SECOES.items():
        idx = next((i for i, l in enumerate(linhas) if re.search(rx, l, re.I)), None)
        if idx is None:
            erros.append(f"seção ausente: {nome}")
            continue
        corpo = []
        for l in linhas[idx + 1:]:
            if l.startswith("#"):
                break
            corpo.append(l)
        if not "".join(corpo).strip():
            erros.append(f"seção vazia: {nome}")
    return erros, n


def main():
    pasta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    ea = parte_a(pasta)
    eb, n = parte_b(pasta)
    print(f"Parte A: {'ok' if not ea else 'problemas'}")
    for e in ea:
        print("  -", e)
    print(f"Parte B: {'ok' if not eb else 'problemas'} ({n} de {TETO} tokens)")
    for e in eb:
        print("  -", e)
    sys.exit(1 if ea or eb else 0)


if __name__ == "__main__":
    main()
