# Atividade: diagnóstico e compactação de contexto

## O que entregar

Você deve entregar dois arquivos, com exatamente estes nomes:

- `respostas.json` (Parte A)
- `progress.md` (Parte B)

Antes de enviar, rode `python verificar.py` na pasta onde estão os dois arquivos. Ele aponta erros de formato e mostra o tamanho do seu `progress.md`. 

Nota: Parte A vale 5 pontos e Parte B vale 5 pontos.

## Parte A: diagnóstico (5 pontos)

A pasta `casos/` tem 6 dumps do contexto de um agente fictício no momento em que algo deu errado. Cada linha tem um número no começo. 
Em cada caso existe um modo de falha principal.

Para cada caso, preencha em `respostas.json`:

- `modo_falha`: um entre `poisoning`, `distraction`, `confusion`, `clash`.
- `linha_evidencia`: o número da linha que melhor mostra o problema. Para poisoning, é a linha onde a informação incorreta entra no contexto. Para clash, 
uma das duas linhas que se contradizem. Para os demais, a linha onde o problema já é visível no contexto.
- `tecnica`: a técnica de engenharia de contexto que você aplicaria primeiro para evitar a falha: `write`, `select`, `compress` ou `isolate`.

Alguns casos aceitam mais de uma técnica. Escolha uma só e esteja pronto para defendê-la.

Peso de cada caso: 50% pelo modo de falha, 25% pela linha de evidência, 25% pela técnica.

## Parte B: compactação (5 pontos)

`trace.md` é o log de uma sessão de agente que parou com a janela em 78%. Você vai fazer o que vimos em sala de aula: escrever o estado da sessão em um `progress.md` para uma sessão nova continuar de onde esta parou.

Use `progress.md` (já existe um modelo) com estas quatro seções, com estes títulos:

- `## Objetivo`
- `## Abordagem`
- `## Passos concluídos`
- `## Falha atual`

1. **Tamanho.** No máximo 350 tokens aproximados. O `verificar.py` usa a mesma contagem do corretor.
2. **Fatos.** O texto deve conter os fatos que uma sessão nova precisa para continuar sem reler o trace: o que já se sabe, o que já foi decidido, o que restringe a solução e onde o trabalho parou. Use os nomes exatos de arquivos, funções, testes, comandos e valores, não paráfrases. A correção procura esses identificadores.
3. **Informação envenenada.** O trace contém afirmações que o próprio agente fez e depois descobriu serem falsas ou desatualizadas. Elas não podem aparecer no seu `progress.md`, nem para negá-las.
