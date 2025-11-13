def all_thing_is_obj(object: any) -> int:
    typ = type(object)
    name = typ.__name__
    if name not in ['list', 'tuple', 'set', 'dict', 'str']:
        print('Type not found')
    elif name == 'str':
        print(f'{object} is in the kitchen : {typ}')
    else:
        print(f'{name.capitalize()}: {typ}')
    return 42
