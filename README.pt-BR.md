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

### Num projeto de time

Pra todo mundo do repositório usar a stack, versione isto em
`.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "frontend-stack": {
      "source": {
        "source": "github",
        "repo": "JaimeJunr/claude-code-frontend-skills"
      }
    }
  },
  "enabledPlugins": {
    "frontend-stack@frontend-stack": true,
    "frontend-design@frontend-stack": true,
    "impeccable@frontend-stack": true,
    "ui-ux-pro-max@frontend-stack": true,
    "taste@frontend-stack": true,
    "emil-design-eng@frontend-stack": true
  }
}
```

**Ligado não é instalado.** Esse arquivo diz quais plugins o projeto quer. A
instalação fica registrada em cada máquina, em
`~/.claude/plugins/installed_plugins.json`, que não vai pro git. Então, em
toda máquina nova (colega de time, notebook novo, CI), os plugins aparecem
como ligados mas só carregam depois de instalados ali uma vez. Na raiz do
repositório:

```bash
for p in frontend-stack frontend-design impeccable ui-ux-pro-max taste emil-design-eng; do claude plugin install "$p@frontend-stack" --scope project; done
```

O comando pode reformatar o `.claude/settings.json` sem mudar o conteúdo;
`git checkout .claude/settings.json` deixa o diff limpo. Confira com
`claude plugin list` e **abra uma sessão nova**: os plugins só
carregam quando a sessão começa, então a sessão onde você rodou o comando não
enxerga eles.

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
