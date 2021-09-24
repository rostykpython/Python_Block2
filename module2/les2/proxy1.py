class Image:
    def __init__(self, filename):
        self.filename = filename

    def load_image_from_disk(self):
        print(f'Loading {self.filename}')

    def display_image(self):
        print(f'Display {self.filename}')


class Proxy:
    def __init__(self, subject):
        self.subject = subject
        self.proxy_state = None


class ProxyImage(Proxy):
    def display_image(self):
        if self.proxy_state is None:
            self.subject.load_image_from_disk()
            self.proxy_state = 1
        print(f'Display {self.subject.filename}')


image = ProxyImage(Image('photo1'))
image2 = ProxyImage(Image('photo2'))

image.display_image()
image2.display_image()
