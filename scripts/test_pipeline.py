import torch
import pandas as pd
import openpyxl
import PIL
import cv2
import fitz
import pptx
import ezdxf

print("GPU:", torch.cuda.is_available())
print("Excel:", pd.__version__)
print("OpenCV:", cv2.__version__)
print("PyMuPDF:", fitz.__doc__.split()[1])
print("PPTX: ok")
print("DXF: ok")
print("Pipeline ready")
