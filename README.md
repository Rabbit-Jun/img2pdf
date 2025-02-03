# 이미지 to PDF 변환기

이 프로그램은 사용자가 선택한 이미지 파일을 PDF 파일로 변환하는 간단한 GUI 애플리케이션입니다.

## 요구사항

- Python 3.x
- Pillow
- Tkinter (기본적으로 Python에 포함됨)

## 설치 방법

1. 필요 라이브러리 설치:
   ```sh
   pip install -r requirements.txt
   ```

2. 프로그램 실행:
   ```sh
   python img2pdf.py
   ```

## PyInstaller로 실행 파일 만들기

```sh
pip install pyinstaller
pyinstaller --onefile --windowed img2pdf.py
```

실행 파일이 `dist/` 폴더에 생성됩니다.
