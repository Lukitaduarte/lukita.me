# lukita.me

Lukita's blog: a bored mobile dev using AI to learn things outside my field. Software engineering, product and applied AI, with the numbers on the table. Every post comes out in Portuguese and English.

## Running locally

Requires Ruby 3.3+ and Bundler.

```shell
bundle install
bundle exec jekyll serve --livereload           # http://127.0.0.1:4000
bundle exec jekyll serve --unpublished --future # include drafts (published: false)
```

## Layout

| Path | What |
|---|---|
| `_posts/` | Posts in pairs: `YYYY-MM-DD-slug.md` (pt) and `YYYY-MM-DD-slug-en.md` (en), each with `lang:` and a link to the other |
| `_tabs/about.md` | About page, pt and en on the same page |
| `_layouts/home.html` | Chirpy home with a language filter (flags); the choice is saved and, without one, follows the browser language |
| `_includes/chart-*.html` | SVG charts used in posts, light and dark themes |
| `_includes/newsletter.html` | Signup form (Kit) at the end of posts |
| `assets/css/jekyll-theme-chirpy.scss` | Visual tweaks on top of Chirpy (zinc palette, tables, charts, filter, newsletter) |
| `tools/newsletter.py` | Schedules a Kit email for every new post |

## Deploy and newsletter

- **Build and Deploy** (`.github/workflows/pages-deploy.yml`): on every push to `main`, builds the site and publishes it to GitHub Pages.
- **Newsletter** (`.github/workflows/newsletter.yml`): after a successful deploy, looks for published posts not yet in `_data/newsletter_sent.yml`, schedules the email on [Kit](https://kit.com) (free plan, up to 10k subscribers) 10 minutes ahead and records the slugs. A post `slug` and its English version `slug-en` go out as one email with both links, to all subscribers. Nothing is sent while `newsletter.send` is false; it stops at 2 articles per run and, when triggered manually, starts in dry-run mode (`list_ids` prints the Kit form ids).

Configuration: `newsletter.form_id` and `newsletter.send` in `_config.yml`, and the API key in the `KIT_API_KEY` secret.

## Credits

[Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme, MIT license (see `LICENSE`). Post text and images are the author's.
