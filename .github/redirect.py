import html, json, os

HOST = os.environ['LIVE_HOST'].rstrip('/')
PAGE = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta name="referrer" content="no-referrer"><title>Moved</title><script>location.replace({host}+location.pathname+location.search+location.hash)</script><meta http-equiv="refresh" content="0;url={to}"></head><body><a href="{to}">Moved</a></body></html>\n'

for d, dirs, files in os.walk('.'):
    dirs[:] = [x for x in dirs if not (d == '.' and x in ('.git', '.github'))]
    for n in files:
        f = os.path.join(d, n); rel = os.path.relpath(f, '.').replace(os.sep, '/')
        if not n.endswith('.html'): os.remove(f); continue
        path = '' if rel in ('index.html', '404.html') else rel.removesuffix('index.html').removesuffix('.html')
        open(f, 'w', encoding='utf-8').write(PAGE.format(host=json.dumps(HOST), to=html.escape(f'{HOST}/apps/{path}')))
