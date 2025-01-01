import typer

from commands import generate

app = typer.Typer()
app.add_typer(generate.app)

if __name__ == '__main__':
    app()
