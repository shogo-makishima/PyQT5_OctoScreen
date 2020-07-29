import Scripts.Settings.Settings as Settings


def GenerateButtonStyleSheet(name: str = "Back", fontSize: int = 15, fontFamily: str = "Trench", imageName: str = "home", imageNameHover: str = "home", imageNamePressed: str = "home"):
    return f"""
            #{name} {{
                font-size: {fontSize}pt;
                font-family: {fontFamily};
                /*
                background-image: url({Settings.UI_PATH}/{imageName}.png);
                background-repeat: False;
                background-resize: contain;
                */
                color: rgb(255, 255, 255);
            }}
            /*
            #{name}::hover {{
                background-image: url({Settings.UI_PATH}/{imageNameHover}.png);
                color: rgb(200, 200, 200);
            }}
            #{name}:pressed {{
                background-image: url({Settings.UI_PATH}/{imageNamePressed}.png);
                color: rgb(140, 140, 140);
            }}
            */
    """

def GenerateParameterStyleSheet(name: str = "Back", fontSize: int = 15, fontFamily: str = "Trench"):
    return f"""
            #{name} {{
                font-size: {fontSize}pt;
                font-family: {fontFamily};
                background-image: url(Files/Images/UI/Button_Empty.png);
                color: rgb(255, 255, 255);
            }}
    """
