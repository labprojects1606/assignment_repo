
def show_properties(module) -> None:
    print(f"Module __name__: {getattr(module, '__name__', None)}")
    print(f"Module __file__: {getattr(module, '__file__', None)}")
    d = getattr(module, '__dict__', {})
    print(f"Module __dict__ keys (sample): {list(d.keys())[:10]}")
