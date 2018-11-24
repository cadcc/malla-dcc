import json
from yattag import Doc


class Renderer:

    def __init__(self, file):
        json_file = open(file, encoding='utf8')
        contents = json_file.read()
        self.data = json.loads(contents)

    def render_program(self):
        pass

    def render_semestre(self):
        pass


if __name__ == '__main__':
    r = Renderer('../malla.json')
    for semester in iter(r.data['semestres']):
        print(semester)
