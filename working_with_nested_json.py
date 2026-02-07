#  Task 3.3: Working with Nested JSON (5 points)
# Create functions to handle complex JSON structures:

def flatten_nested_json(data: dict) -> dict:
    """
    Flatten nested JSON structure one level
    Example: {'user': {'name': 'Alice', 'age': 25}}
    Becomes: {'user.name': 'Alice', 'user.age': 25}
    Return: flattened dictionary
    """
    if data is None:
        return {}
    flat = {}
    for key, value in data.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flat[f"{key}.{sub_key}"] = sub_value
        else:
            flat[key] = value
    return flat

def extract_nested_value(data: dict, path: str) -> object:
    """
    Extract value from nested JSON using dot notation
    path examples: 'user.name', 'address.city', 'items.0.name'
    Return: extracted value or None if path doesn't exist
    """
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, list):
            try:
                idx = int(key)
            except ValueError:
                return None
            try:
                current = current[idx]
            except (IndexError, TypeError):
                return None
        elif isinstance(current, dict):
            try:
                current = current[key]
            except (KeyError, TypeError):
                return None
        else:
            return None
    return current