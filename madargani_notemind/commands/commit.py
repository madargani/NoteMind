import typer

app = typer.Typer()

@app.command()
def commit():
    print('Indexing new files and changes')
