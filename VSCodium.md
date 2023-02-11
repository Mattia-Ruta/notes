# Editing Colours
File > Preferences > Settings | Search for json launch and click `Edit in settings.json`

Edit settings.json and add base for colour customisation

```json
{
    "workbench.colorTheme": "Default Dark+",
    "redhat.telemetry.enabled": false,
    "html.format.endWithNewline": true,
    "editor.definitionLinkOpensInPeek": true,
    "php.suggest.basic": false,
    "launch": {

        "configurations": [],
        "compounds": []
    },
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": [
                    "entity.name.function.php",
                    "meta.function.php"
                ],
                "settings": {
                    "foreground": "#4287f5",
                    "fontStyle": "bold"
                }
            },
            {
                "scope": [
                    "comment.line.double-slash.php",
                    "comment.block.documentation.phpdoc.php"
                ],
                "settings": {
                    "foreground": "#8f8f8f"
                }
            }
        ]
    }
}
```

## Inspect Element
To inspect an element in a language:
1. click on an element, 
2. Press Ctl-Shift-P to open Command Palette
3. Type `Inspect Editor Tokens and Scopes`
4. Copy the first line and paste inside of "scope"
