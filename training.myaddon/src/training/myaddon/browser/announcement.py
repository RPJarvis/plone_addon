from Products.Five import BrowserView


class View(BrowserView):

    def all_caps(self):
        #self.context is current item
        #self.request is also there
        text = self.context.description
        return text.upper()

    def reverse(self):
        text = self.context.more_text
        return str(text)[::-1]

    def display_text(self):
        return 'here is some text'
