from paver.easy import *

@task
def setup():
    if sh('which yarn', capture=True, ignore_error=True):
        if not path('node_modules').isdir():
            sh('yarn')
        if not path('ui-src/node_modules').isdir():
            sh('yarn', cwd='ui-src')
        if not path('ui-automation/node_modules').isdir():
            sh('yarn', cwd='ui-automation')
    else:
        if not path('node_modules').isdir():
            sh('npm install')
        if not path('ui-src/node_modules').isdir():
            sh('npm install', cwd='ui-src')
        if not path('ui-automation/node_modules').isdir():
            sh('npm-install', cwd='ui-automation')

@task
@needs(['setup'])
@cmdopts([
    ('runtime', 'r', 'Include runtime in app DNA'),
])
def build(options):
    hc_api = ['// Holochain API functions for Transcrypted Python module']
    hc_functions = [
        'property', 'makeHash', 'debug', 'call', 'bridge', 'getBridges', 'sign',
        'verifySignature', 'commit', 'get', 'getLinks', 'update', 'updateAgent',
        'remove', 'query', 'send', 'bundleStart', 'bundleClose']
    for function in hc_functions:
        hc_api.append('var hc_' + function + ' = ' + function + ';')
    hc_api += [' = '.join(hc_functions[1:]) + ' = undefined;', '']
    runtime = polyfill = []
    if hasattr(options, 'runtime'):
        rtfile = path('dna/runtime.js')
        if rtfile.isfile():
            runtime = rtfile.lines()
        else:
            polyfill = ['// Using babel polyfill libraries for otto']
            polyfill += path('node_modules/babel-polyfill/dist/polyfill.js').lines()
    for dir in path('dna').dirs():
        for pyfile in dir.files('*.py'):
            jsfile = dir + '/__javascript__/' + pyfile.namebase + '.js'
            if jsfile.isfile() and jsfile.ctime > pyfile.ctime: continue
            modfile = path(jsfile.relpath()[:-3] + '.mod.js')
            sh('transcrypt -n -p .none ' + pyfile.relpath())
            if hasattr(options, 'runtime') and options.runtime and not runtime:
                # Construct javascript runtime for otto
                runtime = polyfill[:]
                runtime.append('\n// Transcrypt runtime code for otto')
                for line in jsfile.lines()[3:]:
                    if line[1:2] == '(': break
                    runtime.append(line)

            modlines = ['\n// Transcrypted Python module for otto']
            for line in modfile.lines()[2:]:
                if line[3:4] == '_': break
                modlines.append(line[2:])

            jsfile.write_lines(hc_api + runtime + modlines)
            minfile = path(jsfile.relpath()[:-3] + '.min.js')
            print('Minifying target code in: ' + minfile.relpath())
            sh('node_modules/uglify-js/bin/uglifyjs --compress --mangle -- ' +
                jsfile.relpath() + ' > ' + minfile.relpath())

    if sh('which yarn', capture=True, ignore_error=True):
        sh('yarn build', cwd='ui-src')
    else:
        sh('npm run-script build', cwd='ui-src')

@task
def clean():
    sh('for x in `find . -name "__javascript__"`; do rm -rf $x; done')
    sh('paver clean', cwd='ui-src')

@task
@needs(['clean'])
def distclean():
    sh('for x in `find . -name "package-lock.json"`; do rm $x; done')
    sh('for x in `find . -name "yarn.lock"`; do rm $x; done')
    sh('for x in `find . -name "node_modules"`; do rm -rf $x; done')
    sh('rm -rf ui ui-automation/cypress/videos')
