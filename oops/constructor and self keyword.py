class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("Ram:",self.ram)
        print("Processor:",self.processor)

hp= laptop()
dell= laptop()
hp.ram="32Gb"
hp.processor="i5"
dell.ram="64Gb"
dell.processor="i6"
hp.display()
dell.display()
