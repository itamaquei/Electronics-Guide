from flet import *

class Ui(UserControl):
    def build(self):
        super().__init__()

        self.youtubers = [
        ["dereksgc", "RF/amateur radio"],
        ["saveitforparts", "RF/amateur radio"],
        ["CNLohr", "Embedded systems, quirky projects"],
        ["learnelectronics", "Electronics fundamentals"],
        ["Mellow_labs", "Electronics, circuit design"],
        ["Julian Ilett", "Teardowns, repairs"],
        ["DiodeGoneWild", "High-voltage experiments, power electronics"],
        ["DENKI-OTAKU", "Electronics projects"],
        ["EugeneKhutoryansky", "Animated videos visualizing electronic physics"],
        ["Alphaphoenix", "Electricity demonstrations"],
        ["Stephen Hawes", "Pick & place machine builds"],
        ["Skyentific", "Mechatronics"],
        ["Maxim Integrated", "Electronics company channel"],
        ["Keysight Technologies", "Electronics company channel"],
        ["Analog Devices Inc", "Electronics company channel"],
        ["Altium", "Electronics company channel"],
        ["SparkFun", "Electronics retailer channel"],
        ["Robert Frenerec", "Electronics content"],
        ["Jeremy Fielding", "Electronics content"],
        ["Adafruit", "Electronics retailer channel"],
        ["Breaking Taps", "Electronics content"],
    ]

        # Create the table header
        self.table_header = ["YouTuber", "Area of Expertise"]

        # Create an empty list to store the table rows
        self.table_rows = []

        # Loop through the list of YouTubers and create table rows
        for youtuber in self.youtubers:
            self.table_rows.append([youtuber[0], youtuber[1]])

        # Print the table
        #print(table_header)
        self.data_rows = []
        for row in self.table_rows:
            self.data_row = DataRow(
                cells=[
                    DataCell(Text(f"{row[0]}")),
                    DataCell(Text(f"{row[1]}"))
                ]
            )
            self.data_rows.append(self.data_row)

            self.wigets = DataTable(
                columns=[
                    DataColumn(Text("Youtube Username")),
                    DataColumn(Text("Area of Expertise"))
                ],
                rows=self.data_rows
            )
        return self.wigets

def main(page:Page):
    page.window_height = 900
    page.window_width = 700
    page.scroll = True
    page.auto_scroll = True
    ui = Ui()

    page.add(ui)


app(target=main)