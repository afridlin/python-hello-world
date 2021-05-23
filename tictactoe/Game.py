class Game:
    width = 0
    height = 0
    field = []

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def play(self):
        self.generate_field()
        print(self.format_field())

    def generate_field(self):
        for i in range(0, self.height):
            row = []
            
            for i in range(0, self.width):
                row.append(" ")

            self.field.append(row)

    def format_field(self):
        formatted_field = ""

        for x in range(0, self.height):
            row = self.field[x]
            formatted_row = " " + " | ".join(row) + "\n"
            formatted_field += formatted_row

            if x != self.height - 1:
                for char in formatted_row:
                    if char == "|":
                        formatted_field += "+"
                    else:
                        formatted_field += "-"

                formatted_field += "\n"

        return formatted_field

                
 