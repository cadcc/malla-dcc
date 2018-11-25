import json
from yattag import Doc


class Renderer:

    def __init__(self, file):
        json_file = open(file, encoding='utf8')
        contents = json_file.read()
        self.data = json.loads(contents)
        self.doc = Doc()

    def render_program(self):
        for semester in iter(r.data.get('semestres')):
            with self.doc.tag('tr'):
                self.render_semester(semester)
        return self.doc.getvalue()

    def render_semester(self, semester):
        with self.doc.tag('td', klass='semester'):
            self.doc.text('Semestre ' + semester.get('numero'))
        for ramo in iter(semester['ramos']):
            self.render_course(ramo)

    def render_course(self, ramo):
        self.doc.asis(self.generate_opening_td(ramo))
        self.render_course_element('codigo', ramo.get('codigo'))
        self.render_course_element('nombre', ramo.get('nombre'))
        self.render_course_element('creditos', ramo.get('creditos') + ' créditos')
        self.doc.asis('</td>')

    def render_course_element(self, name, data):
        with self.doc.tag('div', klass=name):
            self.doc.text(data)

    def generate_opening_td(self, ramo):
        requirements = map(
            lambda req: '"{}"'.format(req),
            ramo.get('requisitos', [])
        )
        requirements_string = ','.join(requirements)
        return "<td asd data-requirements='[" + requirements_string + "]' class='ramo' id='" + ramo.get('codigo') + "'>"



if __name__ == '__main__':
    r = Renderer('../malla.json')
    with open('../base.html', encoding='utf8') as f:
        base = f.read()
    out = base.replace('{{ content }}', r.render_program())
    with open('../out.html', 'w', encoding='utf8') as out_file:
        out_file.write(out)

