def main():
    interface_choice = input("Do you want to use the GUI or the CLI? ")
    if interface_choice.lower() == "cli":
        from cli.cli import cli
        cli()
    elif interface_choice.lower() == "gui":
        from views.view import view
        view()

if __name__ == "__main__":
    main()