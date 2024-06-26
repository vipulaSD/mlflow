from mlflow.entities.model_registry import RegisteredModel


class RegisteredModelSearch(RegisteredModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def tags(self):
        raise Exception(
            "UC Registered Models gathered through search_registered_models do not have tags. "
            "Please use get_registered_model to obtain an individual model's tags."
        )

    def aliases(self):
        raise Exception(
            "UC Registered Models gathered through search_registered_models do not have aliases. "
            "Please use get_registered_model to obtain an individual model's aliases."
        )
