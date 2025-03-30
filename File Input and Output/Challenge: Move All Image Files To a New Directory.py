from pathlib import Path

documents_dir = Path.home() / "Practice Files" / "documents"
images_dir = Path.home() / "Practice Files" / "images"
documents_dir.mkdir(parents=True, exist_ok=True)
images_dir.mkdir(parents=True, exist_ok=True)

paths = [
    documents_dir / "file1.txt",
    documents_dir / "file2.txt",
    documents_dir / "file3.txt",
    documents_dir / "image1.png",
    documents_dir / "image2.gif",
    documents_dir / "image3.png",
    documents_dir / "image4.jpg",
]

for path in paths:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

# Move all image files from documents_dir to images_dir
for path in documents_dir.rglob("*.*"):
    if path.suffix.lower() in [".png", ".jpg", ".gif"]:
        path.replace(images_dir / path.name)

