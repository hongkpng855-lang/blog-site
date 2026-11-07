import struct
import zlib
import os

def create_png(width, height, color_rgb, filename):
    """Create a solid color PNG image"""
    def chunk(chunk_type, data):
        """Create a PNG chunk"""
        chunk_len = struct.pack('>I', len(data))
        chunk_crc = struct.pack('>I', zlib.crc32(chunk_type + data) & 0xffffffff)
        return chunk_len + chunk_type + data + chunk_crc
    
    # PNG signature
    signature = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr = chunk(b'IHDR', ihdr_data)
    
    # IDAT chunk (image data)
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'  # filter type: none
        for x in range(width):
            raw_data += bytes(color_rgb)
    
    compressed = zlib.compress(raw_data, 9)
    idat = chunk(b'IDAT', compressed)
    
    # IEND chunk
    iend = chunk(b'IEND', b'')
    
    # Write PNG file
    with open(filename, 'wb') as f:
        f.write(signature + ihdr + idat + iend)

# Create avatar.jpg (actually PNG format, 200x200, blue-gray)
os.makedirs('posts', exist_ok=True)
create_png(200, 200, (74, 144, 164), 'avatar.jpg')

# Create post feature images (800x400)
create_png(800, 400, (70, 130, 180), 'posts/tech.jpg')      # Steel blue
create_png(800, 400, (46, 139, 87), 'posts/investment.jpg')  # Sea green
create_png(800, 400, (178, 34, 34), 'posts/health.jpg')      # Firebrick

print("Images created successfully!")
