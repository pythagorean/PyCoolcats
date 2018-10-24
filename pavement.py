from paver.easy import *

@task
def setup():
    if sh('which yarn', capture=True, ignore_error=True):
        installer = 'yarn'
    else:
        installer = 'npm install'
    if not path('ui-src/node_modules').isdir():
        sh(installer, cwd='ui-src')
    if not path('ui-automation/node_modules').isdir():
        sh(installer, cwd='ui-automation')

@task
@needs(['setup'])
def build(options):
    hc_api = ['// Holochain API functions for Transcrypted Python module']
    hc_functions = [
        'property', 'makeHash', 'debug', 'call', 'bridge', 'getBridges', 'sign',
        'verifySignature', 'commit', 'get', 'getLinks', 'update', 'updateAgent',
        'remove', 'query', 'send', 'bundleStart', 'bundleClose']
    for function in hc_functions:
        hc_api.append('var hc_' + function + ' = ' + function + ';')
    hc_api += [' = '.join(hc_functions[1:]) + ' = undefined;', '']
    rtfile = path('dna/runtime.js')
    runtime = rtfile.lines()
    for dir in path('dna').dirs():
        for pyfile in dir.files('*.py'):
            jsfile = path(pyfile.relpath()[:-3] + '.js')
            outfile = dir + '/__target__/' + pyfile.namebase + '.js'
            if jsfile.isfile() and jsfile.ctime > pyfile.ctime: continue
            sh('transcrypt -e 5 -n -p .none ' + pyfile.relpath())
            mainstart = False
            jslines = ['\n// Transcrypted Python module for otto']
            for line in outfile.lines():
                if not mainstart:
                    if line[:26] == "var __name__ = '__main__';":
                        mainstart = True
                    continue
                if line[:3] == "//#":
                    break
                if line[:7] == "export ":
                    line = line[7:]
                jslines.append(line)
            jsfile.write_lines(hc_api + runtime + jslines)
            # cleanup intermediate javascript
            sh('rm -rf ' + dir + '/__target__/')

    if sh('which yarn', capture=True, ignore_error=True):
        sh('yarn build', cwd='ui-src')
    else:
        sh('npm run-script build', cwd='ui-src')

@task
def clean():
    for dir in path('dna').dirs():
        for pyfile in dir.files('*.py'):
            jsfile = path(pyfile.parent + '/' + pyfile.namebase + '.js')
            if jsfile.isfile(): sh('rm ' + jsfile)
    sh('paver clean', cwd='ui-src')

@task
@needs(['clean'])
def distclean():
    sh('for x in `find . -name "package-lock.json"`; do rm $x; done')
    sh('for x in `find . -name "yarn.lock"`; do rm $x; done')
    sh('for x in `find . -name "node_modules"`; do rm -rf $x; done')
    sh('rm -rf ui ui-automation/cypress/videos')
