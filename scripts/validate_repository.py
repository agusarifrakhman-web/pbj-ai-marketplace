#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
market = ROOT / '.agents/plugins/marketplace.json'
errors=[]

def load_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'{path.relative_to(ROOT)}: invalid JSON: {e}')
        return None

m=load_json(market)
if m:
    if not isinstance(m.get('name'), str) or not m['name']:
        errors.append('marketplace.json: missing name')
    plugins=m.get('plugins')
    if not isinstance(plugins,list) or not plugins:
        errors.append('marketplace.json: plugins must be a non-empty array')
    else:
        seen=set()
        for item in plugins:
            name=item.get('name')
            if not name or name in seen:
                errors.append(f'marketplace plugin name invalid/duplicate: {name}')
                continue
            seen.add(name)
            source=item.get('source',{})
            if source.get('source')!='local':
                errors.append(f'{name}: expected local source for repo marketplace')
            rel=source.get('path','')
            if not rel.startswith('./'):
                errors.append(f'{name}: source.path must start with ./')
                continue
            p=(ROOT / rel[2:]).resolve()
            if not p.is_dir():
                errors.append(f'{name}: plugin directory missing: {rel}')
                continue
            pj=p/'plugin.json'; cj=p/'.codex-plugin/plugin.json'
            if not pj.is_file(): errors.append(f'{name}: missing plugin.json')
            if not cj.is_file(): errors.append(f'{name}: missing .codex-plugin/plugin.json')
            portable=load_json(pj) if pj.is_file() else None
            compat=load_json(cj) if cj.is_file() else None
            if portable:
                if portable.get('name')!=name:
                    errors.append(f'{name}: portable manifest name mismatch: {portable.get("name")}')
                if '$schema' not in portable:
                    errors.append(f'{name}: portable manifest missing $schema')
            skills=list((p/'skills').glob('*/SKILL.md')) if (p/'skills').is_dir() else []
            if not skills:
                errors.append(f'{name}: no skills/<name>/SKILL.md found')

if errors:
    print('VALIDATION FAILED')
    for e in errors: print(' -',e)
    raise SystemExit(1)
print('VALIDATION OK')
