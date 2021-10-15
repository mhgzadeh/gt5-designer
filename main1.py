import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle('My First PyQt')

        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create A Label
        my_label = qtw.QLabel(f"Hochschule fur Technik Stuttgart \n\n")

        # Change the font of the label
        my_label.setFont(qtg.QFont('Helvetica', 12))
        self.layout().addWidget(my_label)

        # Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setPlaceholderText("Enter Your Name ... ")
        self.layout().addWidget(my_entry)

        # Create Button
        my_button = qtw.QPushButton("Send", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f"Hello {my_entry.text()}. Welcome to my app.")
            print(my_entry.text())
            return my_entry


if __name__ == "__main__":
    app = qtw.QApplication([])
    main_window = MainWindow()

    # Run the app
    app.exec_()
