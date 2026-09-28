# lukita.me

Blog do Lukita: um dev mobile entediado usando IA para aprender coisas fora da minha área. Engenharia de software, produto e IA aplicada, com os números na mesa. Todo post sai em português e em inglês.

*Lukita's blog: a bored mobile dev using AI to learn things outside my field. Every post comes out in Portuguese and English.*

## Rodando local

Precisa de Ruby 3.3+ e Bundler.

```shell
bundle install
bundle exec jekyll serve --livereload          # http://127.0.0.1:4000
bundle exec jekyll serve --unpublished --future # inclui rascunhos (published: false)
```

## Estrutura

| Onde | O quê |
|---|---|
| `_posts/` | Posts em pares: `AAAA-MM-DD-slug.md` (pt) e `AAAA-MM-DD-slug-en.md` (en), cada um com `lang:` e link para o outro |
| `_tabs/about.md` | Página Sobre, em pt e en na mesma página |
| `_layouts/home.html` | Home do Chirpy com filtro de idioma (bandeiras); a escolha fica salva e, sem escolha, segue o idioma do navegador |
| `_includes/grafico-*.html` | Gráficos SVG dos posts, com tema claro e escuro |
| `_includes/newsletter.html` | Formulário de inscrição (Kit) no fim dos posts |
| `assets/css/jekyll-theme-chirpy.scss` | Ajustes visuais sobre o Chirpy (paleta zinc, tabelas, gráficos, filtro, newsletter) |
| `tools/newsletter.py` | Agenda no Kit um e-mail para cada post novo |

## Deploy e newsletter

- **Build and Deploy** (`.github/workflows/pages-deploy.yml`): a cada push na `main`, gera o site e publica no GitHub Pages.
- **Newsletter** (`.github/workflows/newsletter.yml`): depois de um deploy bem-sucedido, procura posts publicados que ainda não estão em `_data/newsletter_enviados.yml`, agenda o e-mail no [Kit](https://kit.com) (plano grátis, até 10 mil inscritos) para 10 minutos depois e registra o slug. Posts em pt vão para quem se inscreveu pelo formulário pt, os demais para o en. Trava em 2 posts por vez e, rodando à mão, começa em modo ensaio.

Configuração: ids dos formulários e segmentos em `newsletter:` no `_config.yml` e a chave da API no secret `KIT_API_KEY`.

## Créditos

Tema [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy), licença MIT (veja `LICENSE`). Os textos e imagens dos posts são do autor.
