import typer
from jinja2 import Environment, FileSystemLoader

# def main(author: str, loop: bool):
#     # 创建模板环境，指定模板文件所在的目录
#     env = Environment(loader=FileSystemLoader('templates'))
#
#     # 加载模板
#     template = env.get_template('template-tpl')
#     # 渲染模板
#     output = template.render({'author': author, 'loop': loop})
#
#     # 打印结果或保存到文件
#     print(output)
from commands import generate

app = typer.Typer()
app.add_typer(generate.app)

if __name__ == '__main__':
    app()
