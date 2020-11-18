import sys
import time

from cleo import Command
from googletrans import Translator, constants


class TranslateCommand(Command):
    """
    Google Translator as a command-line tool (unofficial library using the web API).

    translate
        {text : The text you want to translate.}
        {--s|src=auto : The source language you want to translate.}
        {--d|dest=en : The destination language you want to translate.}
        {--t|detect : Use for detect the source language.}
    """

    def handle(self):
        text = self.argument("text")
        if sys.getsizeof(text) > 15000:
            self.line(
                "\n<error>The maximum character limit on a single text is 15k</error>\n"
            )
            return

        attempts = 0
        translator = Translator()

        while True:
            try:
                if self.option("detect"):
                    detected = translator.detect(text)
                    self.__print_detected(detected)
                    break

                result = translator.translate(
                    text, src=self.option("src"), dest=self.option("dest")
                )
                self._print_results(result)
                break
            except AttributeError as error:
                self.line(
                    f"<error>Google API availability error. We are trying to translate again.</error>"
                )
                attempts += 1
                time.sleep(0.5)
            except ValueError as error:
                self.line(f"<error>{error}</error>")
                break

            if attempts > 2:
                self.line(
                    "<comment>Attempts exhausted, please try again in a few seconds.</comment>"
                )
                break

    def __print_detected(self, detected):
        language = constants.LANGUAGES.get(detected.lang)
        self.line(f"<comment>Language:</comment> {language}")
        self.line(f"<comment>Confidence:</comment> {detected.confidence}")

    def __print_result(self, result):
        src_lang = constants.LANGUAGES.get(result.src)
        self.line(f"<comment>Source language:</comment> {src_lang}")
        self.line(f"<comment>Original text:</comment> {result.origin}\n")

        dest_lang = constants.LANGUAGES.get(result.dest)
        self.line(f"<comment>Target language:</comment> {dest_lang}")
        self.line(f"<comment>Translated text:</comment> {result.origin}")
