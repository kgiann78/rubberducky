from simple_chalk import chalk, yellow, red

TEXTS = {
    'ducky': [
        yellow.bold('           _.._'),
        yellow.bold('          / ') +
          chalk.bold('a a') +
          yellow.bold('\\') +
          red.bold('__,'),
        yellow.bold('          \\  ') + red.bold('-.___/'),
        yellow.bold('           \\  \\'),
        yellow.bold('(\\__,-----,_)  \\'),
        yellow.bold('(    (_         )'),
        yellow.bold(' \\_   (__       /'),
        yellow.bold('   \\___________/'),
        ''
    ],
}

def ducky():
    return TEXTS.get('ducky')
