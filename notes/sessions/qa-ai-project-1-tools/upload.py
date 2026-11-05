import api, json, subprocess, sys
def upload(pid, name, path):
    base = api.req('/design/case?project='+pid)['version']
    out=subprocess.run(['curl','-s','-A','geomind-qa/1.0','-H','Authorization: Bearer '+api._tok,'-F','project='+pid,'-F',f'base={base}','-F','name='+name,'-F','file=@'+path,api.BASE+'/design/case/files'],capture_output=True,text=True).stdout
    return json.loads(out)
