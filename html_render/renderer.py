import json
from yattag import Doc


class Renderer:

    def __init__(self, file):
        json_file = open(file, encoding='utf8')
        contents = json_file.read()
        self.data = json.loads(contents)

    def render_program(self):
        doc = Doc()
        for semester in iter(r.data.get('semestres')):
            with doc.tag('tr'):
                self.render_semester(semester, doc)
        return doc.getvalue()

    def render_semester(self, semester, doc):
        with doc.tag('td', klass='rotate'):
            doc.text('Semestre ' + semester.get('numero'))
        for ramo in iter(semester['ramos']):
            self.render_course(ramo, doc)

    def render_course(self, ramo, doc):
        with doc.tag('td', klass='ramo'):
            self.render_course_element('codigo', ramo.get('codigo'), doc)
            self.render_course_element('nombre', ramo.get('nombre'), doc)
            self.render_course_element('creditos', ramo.get('creditos'), doc)

    @staticmethod
    def render_course_element(name, data, doc):
        with doc.tag('div', klass=name):
            doc.text(data)


if __name__ == '__main__':
    r = Renderer('../malla.json')
    print(r.render_program())
