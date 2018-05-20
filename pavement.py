from paver.easy import *

@task
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
            sh('transcrypt -n -p .none ' + pyfile.relpath())
            jsfile = dir + '/__javascript__/' + pyfile.namebase + '.js'
            modfile = path(jsfile.relpath()[:-3] + '.mod.js')
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
            if not path('node_modules/uglify-js').exists(): continue
            minfile = path(jsfile.relpath()[:-3] + '.min.js')
            print('Minifying target code in: ' + minfile.relpath())
            sh('node_modules/uglify-js/bin/uglifyjs --compress --mangle -- ' +
                jsfile.relpath() + ' > ' + minfile.relpath())

@task
def clean():
    sh('for x in `find . -name "__javascript__"`; do rm -rf $x; done')
