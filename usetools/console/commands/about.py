from cleo import Command
from pyfiglet import Figlet


class AboutCommand(Command):
    name = "about"

    description = "Shows information about Use Tools command line."

    def handle(self):
        custom_fig = Figlet(font='big')
        title = custom_fig.renderText('Use Tools')
        self.line(
            f"""{title}\n<info>This package provides a unified command line interface to useful resources for various activities</info>
            """
        )