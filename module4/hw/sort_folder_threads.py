from pathlib import Path
import shutil
import time
import concurrent.futures

AVI = []
MP4 = []
MOV = []
MKV = []
MP3 = []
OGG = []
WAV = []
AMR = []
JPEG = []
JPG = []
PNG = []
SVG = []
DOC = []
DOCX = []
XLSX = []
PPTX = []
PDF = []
ZIP = []
TAR = []
OTHER = []


IMAGES = [JPG, JPEG, SVG, PNG]
DOCS = [DOC, DOCX, PPTX, XLSX, PDF]
ARCH = [TAR, ZIP]
VIDEOS = [MP4, MKV, AVI, MOV]
MUSIC = [MP3, OGG, WAV, AMR]
OTHERS = [OTHER]


REGISTERED_EXT = {
    'JPEG': JPEG,
    'JPG': JPG,
    'PNG': PNG,
    'SVG': SVG,
    'DOC': DOC,
    'DOCX': DOCX,
    'XLSX': XLSX,
    'PPTX': PPTX,
    'PDF': PDF,
    'ZIP': ZIP,
    "TAR": TAR,
    'MP4': MP4,
    'AVI': AVI,
    'MOV': MOV,
    'MKV': MKV,
    'MP3': MP3,
    'OGG': OGG,
    'WAV': WAV,
    'AMR': AMR,
    'OTHER': OTHER
}


def parse_folder(path: Path):
    for folder_item in path.iterdir():
        if folder_item.is_dir():
            if folder_item.name not in ['IMAGES', 'VIDEOS', 'DOCS', 'OTHER', 'MUSIC', 'ARCH']:
                parse_folder(folder_item)
                continue
        else:
            ext = folder_item.suffix[1:]
            if ext.upper() in REGISTERED_EXT.keys():
                REGISTERED_EXT[ext.upper()].append(folder_item)
            else:
                REGISTERED_EXT['OTHER'].append(folder_item)
    return REGISTERED_EXT


def handle_file(root_path, list_of_paths):
    for type_file in list_of_paths:
        for file_path in type_file:
            ext = file_path.suffix[1:].upper()
            if ext in ['JPG', 'SVG', 'PNG', 'JPEG']:
                category_folder = root_path / 'IMAGES'
            elif ext in ['DOC', 'DOCX', 'PPTX', 'PDF', 'XLSX']:
                category_folder = root_path / 'DOCS'
            elif ext in ['TAR', 'ZIP', 'RAR']:
                category_folder = root_path / 'ARCH'
            elif ext in ['MP3', 'OGG', 'WAV', 'AMR']:
                category_folder = root_path / 'MUSIC'
            elif ext in ['MP4', 'AVI', 'MOV', 'MKV']:
                category_folder = root_path / 'VIDEOS'
            else:
                category_folder = root_path / 'OTHER'
            category_folder.mkdir(exist_ok=True)
            type_folder = category_folder / ext
            type_folder.mkdir(exist_ok=True)
            file_path.replace(type_folder / file_path.name)


def del_empty_folders(path_file: Path):
    for folder in path_file.iterdir():
        if folder.name not in ['IMAGES', 'DOCS', 'ARCH', 'OTHER', 'VIDEOS', 'MUSIC'] and folder.is_dir():
            shutil.rmtree(folder)


def threading_files(root_path: Path):
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        list(executor.map(handle_file, (root_path for i in range(6)), (IMAGES, DOCS, ARCH, MUSIC, VIDEOS, OTHERS)))


def execute_command(root_path: Path):
    parse_folder(root_path)
    threading_files(root_path)
    del_empty_folders(root_path)


if __name__ == '__main__':
    folder_to_sort = Path(r'C:\Users\Lenovo\Desktop\Folder_for_script\new_one')
    start_time = time.time()
    execute_command(folder_to_sort)
    print(f'Program execution: {time.time() - start_time}')
    p = 'Program execution: 0.12106442451477051'
