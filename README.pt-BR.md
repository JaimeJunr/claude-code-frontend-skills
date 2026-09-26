# Claude Code Frontend Skills (pt-BR)

**A stack de design frontend pro Claude Code num marketplace só.** Junta as
melhores skills, plugins e agents de frontend, sem conflito entre eles, e
sincroniza toda semana com os repositórios originais:

- [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) (Anthropic)
- [Impeccable](https://github.com/pbakaus/impeccable) (Paul Bakaus)
- [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (Next Level Builder)
- [Taste](https://github.com/leonxlnx/taste-skill) (Leonxlnx)
- [Skills do Emil Kowalski](https://github.com/emilkowalski/skills) (design engineering e animação)

E um plugin de cola, o **`frontend-stack`**, com uma skill roteadora que
escolhe a skill certa pra cada tarefa, as regras de desempate quando os
pacotes discordam, e dois agents (`design-director` e `ui-reviewer`).

## Instalar

```
/plugin marketplace add JaimeJunr/claude-code-frontend-skills
/plugin install frontend-stack@frontend-stack
/plugin install frontend-design@frontend-stack
/plugin install impeccable@frontend-stack
/plugin install ui-ux-pro-max@frontend-stack
/plugin install taste@frontend-stack
/plugin install emil-design-eng@frontend-stack
```

Opcionais: `taste-imagegen@frontend-stack` (precisa de ferramenta de gerar
imagem) e `emil-native@frontend-stack` (React Native/Expo e Swift).

Se você já tem algum desses instalado pelo repo original, desinstale antes
pra skill não carregar duas vezes.

## O que a camada de compatibilidade resolve

- O Taste pede micro-animação o tempo todo; o Emil pergunta se deveria animar
  e mantém animação de UI abaixo de 300 ms. Em UI de produto, vale o Emil.
- O `design-taste-frontend` diz que não serve pra dashboard. O roteador
  respeita isso.
- O Impeccable e a skill Stitch do Taste escrevem `DESIGN.md` em formatos
  diferentes. O `DESIGN.md` fica com o Impeccable.
- Os presets de estética (minimalista, brutalista, "cara de agência") só
  disparam quando você pede explicitamente.

Detalhes no [README em inglês](README.md) e nas
[regras de conflito](plugins/frontend-stack/skills/frontend-stack/references/conflicts.md).
