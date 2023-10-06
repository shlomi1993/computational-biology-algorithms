# File: app.py
# Content: the entry point of the program.


from src.cli import FutoshikiCli


if __name__ == '__main__':
    cli = FutoshikiCli()
    cli.mainloop()
