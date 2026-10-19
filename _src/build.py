"""build.py — generate the static site (index, publications, projects, cv) from site.yaml + publications.bib.

    python _src/build.py          # writes the pages into the repo root (the folder above _src/)

Edit content in site.yaml and publications.bib only; the HTML is regenerated.
"""
import os, re, shutil, html
import yaml
from jinja2 import Environment, FileSystemLoader

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(SRC)
ME = 'Lin, Chunxiao'


# ------------------------------------------------------------------ minimal BibTeX reader
def read_bib(path):
    text = open(path, encoding='utf-8').read()
    text = '\n'.join(l for l in text.splitlines() if not l.lstrip().startswith('%'))
    entries = []
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,]+),', text):
        etype, key, i = m.group(1).lower(), m.group(2).strip(), m.end()
        depth, j = 1, i
        while depth and j < len(text):
            depth += {'{': 1, '}': -1}.get(text[j], 0)
            j += 1
        body, fields, k = text[i:j - 1], {}, 0
        for fm in re.finditer(r'(\w+)\s*=\s*', body):
            if fm.start() < k:
                continue
            name, p = fm.group(1).lower(), fm.end()
            if body[p] == '{':
                d, q = 1, p + 1
                while d:
                    d += {'{': 1, '}': -1}.get(body[q], 0)
                    q += 1
                val, k = body[p + 1:q - 1], q
            else:
                q = body.find(',', p)
                q = len(body) if q < 0 else q
                val, k = body[p:q].strip().strip('"'), q
            fields[name] = re.sub(r'\s+', ' ', val).strip()
        fields.update(type=etype, key=key)
        entries.append(fields)
    return entries


def tex2html(s):
    s = s.replace('---', '—').replace('--', '–').replace('{', '').replace('}', '')
    return html.escape(s, quote=False).replace('&amp;amp;', '&amp;')


def fmt_authors(a):
    out = []
    for name in [x.strip() for x in a.split(' and ')]:
        last, _, first = name.partition(',')
        full = (first.strip() + ' ' + last.strip()).strip()
        out.append('<em>%s</em>' % full if name == ME else full)
    return ', '.join(out)


def bibtex_clean(e):
    keep = ['title', 'author', 'journal', 'booktitle', 'publisher', 'volume', 'number', 'pages', 'year', 'doi']
    lines = ['@%s{%s,' % (e['type'], e['key'])] + ['  %s = {%s},' % (f, e[f]) for f in keep if f in e]
    return '\n'.join(lines).rstrip(',') + '\n}'


def load():
    site = yaml.safe_load(open(os.path.join(SRC, 'site.yaml'), encoding='utf-8'))
    pubs = read_bib(os.path.join(SRC, 'publications.bib'))
    for p in pubs:
        p['title_h'] = tex2html(p['title'])
        p['authors_h'] = fmt_authors(p['author'])
        p['venue_h'] = tex2html(p.get('journal') or p.get('booktitle') or '')
        if p.get('publisher'):
            p['venue_h'] += ', ' + tex2html(p['publisher'])
        if p.get('pages'):
            p['venue_h'] += ', pp. ' + tex2html(p['pages'])
        pdf = p.get('pdf')
        p['pdf_url'] = (pdf if pdf and pdf.startswith('http') else ('/files/' + pdf if pdf else None))
        p['doi_url'] = 'https://doi.org/' + p['doi'] if p.get('doi') else None
        p['bib'] = bibtex_clean(p)
    pubs.sort(key=lambda p: -int(p['year']))
    bykey = {p['key']: p for p in pubs}
    site['all_projects'] = []
    for g in site['project_groups']:
        for pr in g['projects']:
            pr['pub_list'] = [bykey[k] for k in pr.get('pubs', [])]
            for p in pr['pub_list']:
                p['project'] = pr
            pr['has_page'] = bool(pr.get('img') or pr.get('points') or pr.get('kpis') or pr.get('pubs') or pr.get('videos'))
            site['all_projects'].append(pr)
    site['highlights'] = [pr for pr in site['all_projects'] if pr.get('highlight')]
    site['demo'] = next(pr for pr in site['all_projects'] if pr['id'] == site['live_demo']['project'])
    return site, pubs


def main():
    site, pubs = load()
    env = Environment(loader=FileSystemLoader(os.path.join(SRC, 'templates')), autoescape=False)
    kinds = [('journal', 'Journal articles'), ('conference', 'Conference papers'), ('book', 'Book chapters')]
    pages = {'index.html': ('home.html', 'about', {}), 'publications/index.html': ('publications.html', 'publications', {}),
             'projects/index.html': ('projects.html', 'projects', {}), 'cv/index.html': ('cv.html', 'cv', {})}
    for pr in site['all_projects']:
        if pr['has_page']:
            pages['projects/%s/index.html' % pr['id']] = ('project.html', 'projects', {'pr': pr})
    for out, (tpl, active, extra) in pages.items():
        root = '../' * out.count('/')
        h = env.get_template(tpl).render(site=site, pubs=pubs, selected=[p for p in pubs if p.get('selected') == 'true'],
                                         kinds=kinds, active=active, root=root, **extra)
        dst = os.path.join(OUT, out)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, 'w', encoding='utf-8', newline='\n').write(h)
    print('wrote %d pages' % len(pages))
    os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    shutil.copy(os.path.join(SRC, 'style.css'), os.path.join(OUT, 'assets', 'style.css'))
    open(os.path.join(OUT, '.nojekyll'), 'w').close()


if __name__ == '__main__':
    main()
