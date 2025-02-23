import os
import pytest
from zipfile import ZipFile


@pytest.fixture(scope="session")
def ARCHIVE_FILE_PATH(tmpdir_factory):
    # Создаем временный архив
    tmp_dir = os.path.join(os.path.dirname(__file__), "..", "tmp")
    archive_path = tmpdir_factory.mktemp("data").join("files.zip")

    # Создаем архив с файлами
    with ZipFile(archive_path, "w") as zipf:
        for file in ["csv_file.csv", "pdf_file.pdf", "xlsx_file.xlsx"]:
            file_path = os.path.join(tmp_dir, file)
            if os.path.exists(file_path):
                zipf.write(file_path, arcname=file)

    yield str(archive_path)

    # Очистка после выполнения тестов
    if os.path.exists(archive_path):
        os.remove(archive_path)
