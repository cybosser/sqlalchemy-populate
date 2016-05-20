from sqlalchemy_populate.loader import load_model_class


def instantiate_model(model_name, fields, model_class_loader=load_model_class):
    model_class = model_class_loader(model_name)

    return model_class(**fields)
