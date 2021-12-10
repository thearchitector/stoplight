from typing import Dict, List, Optional, Type

from tortoise import BaseDBAsyncClient, Model, Tortoise
from tortoise.exceptions import ConfigurationError
from tortoise.signals import pre_save

from .strategies import STRAT_TO_FUNC, Strategies, MockTypes


async def init_anonymizations(models: Optional[List[Type[Model]]] = None):
    """
    Register anonymization strategies in every model. If models should be from
    discovery, this must be called after Tortoise initialization is complete.
    """
    # if models are not provided
    if not models:
        if not Tortoise._inited:
            raise ConfigurationError(
                "You have to call Tortoise.init() before registering model anonymities."
            )

        # extract the models from the ones discovered by Tortoise during initialization
        # https://tortoise.github.io/_modules/tortoise.html#Tortoise.describe_models
        models = []
        for app in Tortoise.apps.values():
            for model in app.values():
                models.append(model)

    # create a pre_save signal hook for all models with field <-> anonymization
    # strategy mappping
    pre_save(*[model for model in models if hasattr(model, "__anonymities__")])(
        anonymize
    )


async def anonymize(
    sender: Type[Model],
    instance: Model,
    db_client: Optional[BaseDBAsyncClient],
    updated_fields: List[str],
) -> None:
    for name, strategy, args in instance.__anonymities__:
        if not isinstance(name, str):
            raise ValueError(f"{name} is not a valid string field identifier.")
        elif not isinstance(strategy, Strategies):
            raise ValueError(f"{strategy} is not a valid anonymization Strategy.")
        elif not hasattr(instance, name):
            raise AttributeError(f"{sender} does not have a writable attribute {name}.")

        value = getattr(instance, name)
        nvalue = STRAT_TO_FUNC[strategy](value, *args)
        setattr(instance, name, nvalue)


__all__ = ["Strategies", "MockTypes"]
