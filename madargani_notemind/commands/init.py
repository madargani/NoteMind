import typer

app = typer.Typer()

@app.command()
def init():
    print('Initializing NoteMind directory')
