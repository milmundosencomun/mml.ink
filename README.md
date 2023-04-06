# BAM's Custom Short Link Server (baml.ink)

## How to add a short link

1. Open [baml.yaml](./baml.yaml) and use Github's built-in editor to add a line under `urls:` that looks something like this:

```
  ig: https://www.instagram.com/bushwickayudamutua/
```

Here, `ig` is the path of short link, so you would then then share `baml.ink/ig` and it would point to `https://www.instagram.com/bushwickayudamutua/`. Please note that URLs are case-sensitive, so add multiple versions of the path to ensure people get where they're trying to go. You can also make versions in multiple languages this way, as well. Each line should have two-spaces of indentation before the path begins.

Expand for examples:

<details>
Good:

```
urls:
  goo: https://google.com
  yoo: https://yahoo.com
  moo: https://microsoft.com
```

Bad:

```
urls:
  goo: https://google.com
yoo: https://yahoo.com
  moo: https://microsoft.com
```

Bad:

```
urls:
  goo: https://google.com
 yoo: https://yahoo.com
  moo: https://microsoft.com
```
</details>

2. Save your changes in Github's editor and add a commit message describing the changes you made.
3. Wait a few minutes and your link(s) should be live!

## How this works

This repository generates a static website hosted on github pages with individual HTML pages for each of our short links. These pages are created by a tool called [urlzap](https://github.com/brunoluiz/urlzap/) and automatically built each time the repo changes using the [urlzap github action](https://github.com/brunoluiz/urlzap-github-action/). The static version of the site lives on the [gh-pages](https://github.com/bushwickayudamutua/baml.ink/tree/gh-pages) branch which is configured with the custom domain of `baml.ink`, which we configure in [gandi](https://gandi.net).

