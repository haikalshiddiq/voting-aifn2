import json,os,pathlib,urllib.request
account=os.environ['CLOUDFLARE_ACCOUNT_ID'];token=os.environ['CLOUDFLARE_API_TOKEN'];base=f'https://api.cloudflare.com/client/v4/accounts/{account}/d1/database';h={'Authorization':f'Bearer {token}','Content-Type':'application/json'}
def call(url,method='GET',data=None):
 r=urllib.request.Request(url,method=method,headers=h,data=json.dumps(data).encode() if data else None)
 with urllib.request.urlopen(r,timeout=30) as x:return json.load(x)
x=call(base+'?name=voting-aifn2');items=x.get('result') or [];db=next((i for i in items if i.get('name')=='voting-aifn2'),None)
if not db:db=call(base,'POST',{'name':'voting-aifn2'})['result']
id=db.get('uuid') or db.get('id');p=pathlib.Path('wrangler.jsonc');p.write_text(p.read_text().replace('REPLACE_WITH_D1_DATABASE_ID',id));print('D1 ready',id)
