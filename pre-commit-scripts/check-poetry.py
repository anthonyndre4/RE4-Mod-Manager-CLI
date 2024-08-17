def try_import() -> bool:
    import_working = True
    try:
        from pydantic import BaseModel

        return import_working
    except ImportError:
        import_working = False
        return import_working


print(try_import())
