#!/usr/bin/env python3
"""使用純 Python 生成簡單的封面圖（無需外部依賴）"""

import struct
import zlib
import os

def create_png(width, height, filename):
    """創建一個簡單的 PNG 圖片"""
    
    def png_chunk(chunk_type, data):
        """生成 PNG chunk"""
        chunk = struct.pack('>I', len(data)) + chunk_type + data
        checksum = zlib.crc32(chunk_type + data)
        chunk += struct.pack('>I', checksum)
        return chunk
    
    # PNG 簽名
    signature = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr = png_chunk(b'IHDR', ihdr_data)
    
    # IDAT chunk (圖片數據)
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'  # 過濾類型
        for x in range(width):
            # 根據位置生成簡單的漸變色
            if y < 8:  # 頂部強調條
                r, g, b = 255, 215, 0  # 金色
            elif y > height - 60:  # 底部區域
                r, g, b = 30, 30, 50
            else:
                # 漸變背景
                r = int(26 + (y / height) * 20)
                g = int(54 + (y / height) * 30)
                b = int(93 + (y / height) * 40)
            
            raw_data += bytes([r, g, b])
    
    compressed = zlib.compress(raw_data, 9)
    idat = png_chunk(b'IDAT', compressed)
    
    # IEND chunk
    iend = png_chunk(b'IEND', b'')
    
    # 寫入文件
    with open(filename, 'wb') as f:
        f.write(signature + ihdr + idat + iend)
    
    print(f"✅ 已生成：{filename}")

def main():
    output_dir = os.path.expanduser("~/.openclaw/workspace/jekyll-blog/assets/images/posts")
    os.makedirs(output_dir, exist_ok=True)
    
    print("🎨 使用純 Python 生成簡單封面圖...\n")
    
    # 由於純 PNG 太簡陋，我們改用 SVG 格式
    covers = [
        {
            'title': '被動收入入門',
            'filename': '2026-03-25-被動收入入門-cover.png'
        },
        {
            'title': '提升工作效率',
            'filename': '2025-03-25-提升工作效率-cover.png'
        },
        {
            'title': 'GitHub Pages 教學',
            'filename': '2026-03-20-github-pages-blog-cover.png'
        }
    ]
    
    for cover in covers:
        create_png(1200, 630, os.path.join(output_dir, cover['filename']))
    
    print(f"\n📁 存放位置：{output_dir}")

if __name__ == '__main__':
    main()
