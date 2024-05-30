import PySimpleGUI as gui
import Zip_creator_extractor

gui.theme("DarkGrey11")

select_files_to_compress = gui.Text("Select files to Compress: ")
input_box = gui.Input(tooltip="Choose Files")
choose_button_for_files = gui.FilesBrowse("Choose", key="files")

select_destination = gui.Text("Select destination folder: ")
input_box_dest = gui.Input(tooltip="Select Destination Folder")
choose_button_dest = gui.FolderBrowse("Choose", key="folder")

compress_button = gui.Button("Compress")
output_label = gui.Text(key="output", text_color="green")

select_file_to_compress = gui.Text("Select Archive: ")
input_box_file = gui.Input(tooltip="Choose File")
choose_button_for_file = gui.FileBrowse("Choose", key="archive")

select_destination_for_files = gui.Text("Select destination folder: ")
input_box_dest_folder = gui.Input(tooltip="Select Destination Folder")
choose_button_dest_folder = gui.FolderBrowse("Choose", key="folder_dist")

extract_button = gui.Button("Extract")
output_label_extraction = gui.Text(key="output", text_color="green")

window = gui.Window("File Zipper", layout=[[select_files_to_compress, input_box, choose_button_for_files],
                                           [select_destination, input_box_dest, choose_button_dest],
                                           [select_file_to_compress, input_box_file, choose_button_for_file],
                                           [select_destination_for_files, input_box_dest_folder,
                                            choose_button_dest_folder],
                                           [compress_button, extract_button], [output_label, output_label_extraction]],
                    background_color="black")

while True:
    event, values = window.read()
    print(event,values)
    try:
        filepath = values["files"].split(";")
        folder = values["folder"]
        Zip_creator_extractor.make_archive(filepath, folder)
        window["output"].update(value="Compression Completed !")
        archive_path = values['archive']
        dest_dir = values['folder_dest']
        Zip_creator_extractor.extract_archive(archive_path,dest_dir)
        window['output'].update(value="Extraction Completed")

        if gui.WIN_CLOSED:
            break
    except (AttributeError, TypeError):
        exit()
window.close()
