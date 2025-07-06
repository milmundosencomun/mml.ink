# MMeC's Custom Short Link Server (mml.ink)

## How to add a short link

1. Open [mml.yaml](./mml.yaml) and click the pencil icon on the right to open Github's built-in editor.
2.  Add a line under `urls:` that looks something like this:

```
  home: https://milmundosencomun.org/
```

Here, `home` is the path of short link, so you would then then share `mml.ink/home` and it would point to `https://milmundosencomun.org/`. Please note that URLs are case-sensitive, so add multiple versions of the path to ensure people get where they're trying to go. You can also make versions in multiple languages this way, as well. Each line should have two-spaces of indentation before the path begins.

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

3. Save your changes in Github's editor and add a commit message describing the changes you made.
4. Wait a few minutes and your link(s) should be live!
5. There will also be an image of a QR code @ [https://mml.ink/qr/{short_path}.png](https://mml.ink/qr/home.png) which will resolve to the short link.

## QR Codes 

You can view a list of all the qr codes and download them via [this link](https://github.com/milmundosencomun/mml.ink/tree/gh-pages/qr).

Alternatively, you can use the shortlink: https://mml.ink/qr

## How this works

This repository generates a static website hosted on github pages with individual HTML pages for each of our short links. These pages are created by a tool called [urlzap](https://github.com/brunoluiz/urlzap/) and automatically built each time the repo changes using the [urlzap github action](https://github.com/brunoluiz/urlzap-github-action/). The static version of the site lives on the [gh-pages](https://github.com/milmundosencomun/mml.ink/tree/gh-pages) branch which is configured with the custom domain of `mml.ink`, which we configure in [gandi](https://gandi.net).
