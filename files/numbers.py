class Numbers:

        def __init__(self, display):
            self.display = display

        def show_numbers(self, count, render):
            for i in range(count):
                self.display("txt")
            
