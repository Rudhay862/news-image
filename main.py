import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        print(f"size mismatch: {src_size} != {dst_size}", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({dst_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
