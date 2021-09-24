from abc import ABC, abstractmethod


class StatusBar(ABC):
    def __init__(self, system: str):
        self.system = system

    @abstractmethod
    def create(self):
        pass


class MainPage(ABC):
    def __init__(self, system: str):
        self.system = system

    @abstractmethod
    def create(self):
        pass


class WinStatusBar(StatusBar):
    def __init__(self):
        super(WinStatusBar, self).__init__('Windows')

    def create(self):
        print(f'Created for {self.system}')


class WinMainPage(MainPage):
    def __init__(self):
        super(WinMainPage, self).__init__('Windows')

    def create(self):
        print(f'Created main-page for {self.system}')


class GUIAbstractFactory(ABC):

    @abstractmethod
    def getstatusbar(self):
        pass

    @abstractmethod
    def getmainpage(self):
        pass


class WindowsGUIFactory(GUIAbstractFactory):

    def getstatusbar(self):
        return WinStatusBar()

    def getmainpage(self):
        return WinMainPage()


class Application:

    def __init__(self, factory: GUIAbstractFactory):
        self.factory = factory

    def create_gui(self):
        status_bar = self.factory.getstatusbar()
        main_page = self.factory.getmainpage()
        status_bar.create()
        main_page.create()


def create_factory(system: str):
    factory_dict = {
        'Windows': WindowsGUIFactory
    }

    return factory_dict[system]()


if __name__ == '__main__':
    system = create_factory('Windows')
    app = Application(system)
    app.create_gui()
