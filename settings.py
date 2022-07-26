class Settings:
    def getHDResolution(self) -> tuple:
        return (1280, 720)

    def getFullHDResolution(self) -> tuple:
        return (1920, 1080)

    def goFullScreen(self) -> tuple:
        return (0, 0)

    def getLightGreen(self) -> tuple:
        return (0, 0, 128)

    def getCaption(self) -> str:
        return "alient invasion".title()

    def getSpeed(self) -> float:
        return 1.5

    def setWidth(self, width: int):
        self.width = width

    def setHeight(self, height: int):
        self.height = height