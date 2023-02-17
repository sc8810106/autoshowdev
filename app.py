import web
import os

urls = (
    '/', 'index',
    '/code', 'code',
)
app = web.application(urls, globals())
render = web.template.render('templates/')
class index:
    def GET(self):
        return render.autoshow()

class code:
    def POST(self):
        code = str(web.data(), encoding="utf-8")
        print(code)
        file = open(r"code.py", "w", encoding='utf-8')
        file.write(code)
        file.close()
        f = os.popen(r"code.py", "r")
        result = f.read()
        print(result)
        return result
if __name__ == "__main__":
    app.run()