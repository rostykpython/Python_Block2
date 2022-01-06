import asyncio
from aiopath import AsyncPath
from pathlib import Path
import shutil


DOC_DOC = []
DOCX_DOC = []
XLSX_DOC = []
PPTX_DOC = []
PDF_DOC = []
ZIP_ARCH = []
TAR_ARCH = []
OTHER = []

REGISTERED_EXT = {

    'DOC': DOC_DOC,
    'DOCX': DOCX_DOC,
    'XLSX': XLSX_DOC,
    'PPTX': PPTX_DOC,
    'PDF': PDF_DOC,
    'ZIP': ZIP_ARCH,
    "TAR": TAR_ARCH,
    'OTHER': OTHER
}


async def parse_folder(input_path: Path):
    path = AsyncPath(input_path)
    async for folder_item in path.iterdir():
        is_folder = await folder_item.is_dir()
        if is_folder:
            if folder_item.name not in ['IMAGES', 'VIDEOS', 'DOC', 'OTHER', 'MUSIC', 'ARCH']:
                await parse_folder(folder_item)
                continue
        else:
            ext = folder_item.suffix[1:]
            if ext.upper() in REGISTERED_EXT.keys():
                REGISTERED_EXT[ext.upper()].append(folder_item)
            else:
                REGISTERED_EXT['OTHER'].append(folder_item)


async def handle_file(root_path, file_path: Path):
    ext = file_path.suffix[1:].upper()
    if ext in ['JPG', 'SVG', 'PNG', 'JPEG']:
        category_folder = root_path / 'IMAGES'
    elif ext in ['DOC', 'DOCX', 'PPTX', 'PDF', 'XLSX']:
        category_folder = root_path / 'DOC'
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
    await file_path.replace(type_folder / file_path.name)


async def delfolder(input_path: Path):
    async for folder in input_path.iterdir():
        if folder.name not in ['IMAGES', 'DOC', 'ARCH', 'OTHER', 'VIDEOS', 'MUSIC'] and folder.is_dir():
            shutil.rmtree(folder)


async def main(input_path):
    await parse_folder(input_path)

    for items in REGISTERED_EXT.values():
        for item in items:
            await handle_file(input_path, item)


if __name__ == '__main__':
    path = r'C:\Users\User\Desktop\folder_test'

    sort_folder = Path(path)
    asyncio.run(main(sort_folder.resolve()))
