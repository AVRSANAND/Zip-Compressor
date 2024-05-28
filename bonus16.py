import PySimpleGUI as gui
import zip_creator

select_files = gui.Text("Select files to Compress: ")
input_box = gui.Input(tooltip="Choose Files")
choose_button = gui.FilesBrowse("Choose", key="files")

select_destination = gui.Text("Select destination folder: ")
input_box_dest = gui.Input(tooltip="Select Destination Folder")
choose_button_dest = gui.FolderBrowse("Choose", key="folder")

compress_button = gui.Button("Compress")
output_label = gui.Text(key="output", text_color="green", background_color="black")

window = gui.Window("File Zipper",layout=[[select_files, input_box, choose_button],
                                              [select_destination,input_box_dest,choose_button_dest],
                                              [compress_button, output_label]],
                    background_color="black")

while True:
    event, values = window.read()
    try:
        filepath = values["files"].split(";")
        folder = values["folder"]
        zip_creator.make_archive(filepath,folder)
        window["output"].update(value="Compression Completed !")
        if gui.WIN_CLOSED:
            break
    except (AttributeError, TypeError):
        exit()
window.close()


