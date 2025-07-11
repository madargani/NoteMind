import typer

app = typer.Typer()

@app.command()
def status():
    print('Checking status')
