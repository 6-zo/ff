import importlib


def load_operation(module_name, function_name):
    try:
        if __package__:
            module = importlib.import_module(f".{module_name}", __package__)
        else:
            module = importlib.import_module(module_name)
    except ModuleNotFoundError as error:
        if error.name not in (module_name, f"{__package__}.{module_name}"):
            raise
        return None

    return getattr(module, function_name, None)


def main():
    operations = {
        "add": load_operation("add", "add"),
        "minus": load_operation("minus", "minus"),
        "multiplication": load_operation("multiplication", "multiplication"),
        "division": load_operation("division", "divide"),
    }

    for name, operation in operations.items():
        if operation is None:
            print(f"{name}.py is not ready yet.")
            continue

        print(f"{name}(10, 2) = {operation(10, 2)}")


if __name__ == "__main__":
    main()
