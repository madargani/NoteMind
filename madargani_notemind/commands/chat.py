import typer

app = typer.Typer()

@app.command()
def chat():
    print('Opening chat')
