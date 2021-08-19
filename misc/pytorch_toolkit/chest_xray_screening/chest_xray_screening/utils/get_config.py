import os
import json


def get_config(action, optimised = False):
    """ action: train, test or export
        optimised: False --> DenseNet121 
                   True --> DenseNet121Eff
    """
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    config_path = os.path.join(root_path, 'configs')
    if optimised:
        with open(os.path.join(config_path, 'densenet121eff_config.json')) as f1:
            config_file = json.load(f1)
        config = config_file[action]
    else:
        with open(os.path.join(config_path, 'densenet121_config.json')) as f1:
            config_file = json.load(f1)
        config = config_file[action]

    return config