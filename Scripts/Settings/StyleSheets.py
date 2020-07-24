def GenerateButtonStyleSheet(name: str = "Back", fontSize: int = 15, fontFamily: str = "Trench"):
    return f"""
            #{name} {{
                font-size: {fontSize}pt;
                font-family: {fontFamily};
                background-image: url(Files/Images/UI/Button_Empty.png);
                color: rgb(255, 255, 255);
            }}
            #{name}::hover {{
                background-image: url(Files/Images/UI/Button_Empty_Hover.png);
                color: rgb(200, 200, 200);
            }}
            #{name}:pressed {{
                background-image: url(Files/Images/UI/Button_Empty_Press.png);
                color: rgb(140, 140, 140);
            }}
    """
