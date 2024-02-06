def add_attribute(obj, attribute, value):
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
