import pathlib,sys,re
p=pathlib.Path('wrangler.jsonc');s=p.read_text();s=re.sub(r'"TURNSTILE_SITE_KEY"\s*:\s*"[^"]+"',f'"TURNSTILE_SITE_KEY":"{sys.argv[1]}"',s);p.write_text(s)
