#!/usr/bin/env python3
"""生成文章封面圖的腳本"""

from PIL import Image, ImageDraw, ImageFont
import os

# 設定目錄
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 封面圖尺寸
WIDTH, HEIGHT = 1200, 630

# 分類配色方案
COLOR_SCHEMES = {
    'investment': {
        'bg': '#1a365d',      # 深藍色背景
        'accent': '#ffd700',   # 金色強調
        'text': '#ffffff',     # 白色文字
        'secondary': '#4a5568' # 灰色次要
    },
    'learning': {
        'bg': '#2d3748',       # 深灰背景
        'accent': '#48bb78',   # 綠色強調
        'text': '#ffffff',
        'secondary': '#718096'
    },
    'tech': {
        'bg': '#1a202c',       # 極深藍背景
        'accent': '#4299e1',   # 藍色強調
        'text': '#ffffff',
        'secondary': '#2d3748'
    },
    'life': {
        'bg': '#fff5f5',       # 淺粉背景
        'accent': '#f56565',   # 紅色強調
        'text': '#2d3748',
        'secondary': '#e2e8f0'
    },
    'health': {
        'bg': '#f0fff4',       # 淺綠背景
        'accent': '#38a169',   # 綠色強調
        'text': '#2d3748',
        'secondary': '#c6f6d5'
    }
}

def hex_to_rgb(hex_color):
    """將 hex 顏色轉換為 RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_cover(title, category, output_filename, subtitle=""):
    """創建封面圖"""
    scheme = COLOR_SCHEMES.get(category, COLOR_SCHEMES['life'])
    
    # 創建圖片
    img = Image.new('RGB', (WIDTH, HEIGHT), hex_to_rgb(scheme['bg']))
    draw = ImageDraw.Draw(img)
    
    # 嘗試載入字體，失敗則使用預設
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        accent_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        accent_font = ImageFont.load_default()
    
    # 繪製裝飾元素（頂部色條）
    draw.rectangle([0, 0, WIDTH, 8], fill=hex_to_rgb(scheme['accent']))
    
    # 繪製左側裝飾線
    draw.rectangle([60, 200, 68, 430], fill=hex_to_rgb(scheme['accent']))
    
    # 繪製分類標籤
    category_names = {
        'investment': '投資理財',
        'learning': '學習成長',
        'tech': '技術教學',
        'life': '生活分享',
        'health': '健康生活'
    }
    cat_text = category_names.get(category, category)
    draw.text((100, 180), f"#{cat_text}", font=accent_font, fill=hex_to_rgb(scheme['accent']))
    
    # 繪製標題（支援換行）
    title_lines = []
    if len(title) > 15:
        # 嘗試在適當位置斷句
        mid = len(title) // 2
        for i, char in enumerate(title[mid:], mid):
            if char in '：，。、！？ ':
                title_lines = [title[:i+1], title[i+1:]]
                break
        if not title_lines:
            title_lines = [title[:len(title)//2+5], title[len(title)//2+5:]]
    else:
        title_lines = [title]
    
    y_offset = 250
    for line in title_lines:
        draw.text((100, y_offset), line, font=title_font, fill=hex_to_rgb(scheme['text']))
        y_offset += 70
    
    # 繪製副標題
    if subtitle:
        draw.text((100, y_offset + 30), subtitle, font=subtitle_font, fill=hex_to_rgb(scheme['secondary']))
    
    # 繪製底部裝飾
    draw.rectangle([0, HEIGHT-60, WIDTH, HEIGHT], fill=hex_to_rgb(scheme['secondary']))
    
    # 底部網站名稱
    try:
        footer_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        footer_font = ImageFont.load_default()
    draw.text((100, HEIGHT-42), "Sun ny 的部落格", font=footer_font, fill=hex_to_rgb(scheme['text']))
    
    # 儲存圖片
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    img.save(output_path, 'PNG', optimize=True)
    print(f"✅ 已生成：{output_filename}")
    return output_path

def main():
    print("🎨 開始生成文章封面圖...\n")
    
    # 生成各文章封面
    covers = [
        {
            'title': '被動收入入門',
            'category': 'investment',
            'filename': '2026-03-25-被動收入入門-cover.png',
            'subtitle': '從零開始建立你的第一個收入來源'
        },
        {
            'title': '提升工作效率的五個技巧',
            'category': 'learning',
            'filename': '2025-03-25-提升工作效率-cover.png',
            'subtitle': '讓你的工作事半功倍'
        },
        {
            'title': 'GitHub Pages 部落格教學',
            'category': 'tech',
            'filename': '2026-03-20-github-pages-blog-cover.png',
            'subtitle': '從零開始建立個人網站'
        }
    ]
    
    for cover in covers:
        create_cover(
            title=cover['title'],
            category=cover['category'],
            output_filename=cover['filename'],
            subtitle=cover.get('subtitle', '')
        )
    
    print(f"\n✨ 完成！共生成 {len(covers)} 張封面圖")
    print(f"📁 存放位置：{OUTPUT_DIR}")

if __name__ == '__main__':
    main()
