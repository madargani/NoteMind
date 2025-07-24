import typer
from .commands import init, status, commit, search, chat

app = typer.Typer()

app.add_typer(init.app)
app.add_typer(status.app)
app.add_typer(commit.app)
app.add_typer(search.app)
app.add_typer(chat.app)

if __name__ == '__main__':
    app()
