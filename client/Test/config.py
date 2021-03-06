DEVICE = {
    'deviceId': 'a06752e0-9045-4bbf-ab0a-e30df8277f18',
    'pairingCode': 'o1gOd7R',
    'manufacturerName': 'LightBerry',
    'friendlyName': 'SwitchBerry',
    'type': 'switch',
    'description': 'A simple on and off switch',
    'alexa': {
        'displayCategories': ['SWITCH'],
        'additionalDetails': {},
        'capabilities': [
            {
                "type": "AlexaInterface",
                "interface": "Alexa.PowerController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "powerState" }
                    ],
                    "proactivelyReported": False,
                    "retrievable": True
                }
            },
            {
                "type": "AlexaInterface",
                "interface": "Alexa.EndpointHealth",
                "version": "3",
                "properties": {
                    "supported":[
                        { "name":"connectivity" }
                    ],
                    "proactivelyReported": False,
                    "retrievable": True
                }
            },
            {
                "type": "AlexaInterface",
                "interface": "Alexa",
                "version": "3"
            }
        ]
    }
}
