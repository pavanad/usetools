from cleo import Application as BaseApplication

from .commands.about import AboutCommand

try:
    from usetools.__version__ import __version__
except ImportError:
    from __version__ import __version__


class Application(BaseApplication):
    def __init__(self):
        super(Application, self).__init__("usetools", __version__)

        for command in self.get_default_commands():
            self.add(command)

    def get_default_commands(self) -> list:
        commands = [           
            AboutCommand()            
        ]
        return commands