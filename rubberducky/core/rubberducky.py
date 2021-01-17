import sys
from simple_chalk import chalk, green, yellow

from rubberducky.core.text_map import ducky
from rubberducky.core.parse import send_message


class RubberDucky():

    def _print(self):
        print(chalk.green("success"))
        print(yellow("my rubber ducky"))
        for line in ducky():
            print(line)

    def start(self):
        self._print()
        while 1:
            text = input("you: ")
            if text == 'exit':
                break

            try:
                kati, response = self.reply(text)
                print('ducky: {}'.format(response))
                if kati is not None:
                  break
            except Exception as e:
                print('ducky: error: {}'.format(e))

    def reply(self, sentence):
        return send_message(sentence)
