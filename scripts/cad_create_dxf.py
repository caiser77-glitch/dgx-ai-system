from pathlib import Path
import ezdxf

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

doc = ezdxf.new()
msp = doc.modelspace()

msp.add_line((0, 0), (100, 0))
msp.add_line((100, 0), (100, 100))
msp.add_line((100, 100), (0, 100))
msp.add_line((0, 100), (0, 0))
msp.add_text("DGX DXF TEST", dxfattribs={"height": 10}).set_placement((10, 50))

out = output_dir / "test_drawing.dxf"
doc.saveas(out)

print(f"DXF 생성 완료: {out}")
