#!/bin/bash
# 使用 ImageMagick 生成文章封面圖

OUTPUT_DIR="$HOME/.openclaw/workspace/jekyll-blog/assets/images/posts"
mkdir -p "$OUTPUT_DIR"

# 封面圖尺寸
WIDTH=1200
HEIGHT=630

echo "🎨 開始生成文章封面圖..."

# 文章1：被動收入入門（投資類）
convert -size ${WIDTH}x${HEIGHT} \
  -background "#1a365d" \
  -fill "#ffd700" \
  -font DejaVu-Sans-Bold \
  -pointsize 20 \
  -gravity NorthWest \
  -annotate +100+180 "#投資理財" \
  -fill "#ffffff" \
  -pointsize 48 \
  -annotate +100+260 "被動收入入門" \
  -pointsize 28 \
  -fill "#a0aec0" \
  -annotate +100+340 "從零開始建立你的第一個收入來源" \
  -fill "#ffd700" \
  -draw "rectangle 0,0 1200,8" \
  -draw "rectangle 60,200 68,430" \
  -fill "rgba(255,255,255,0.1)" \
  -draw "rectangle 0,570 1200,630" \
  "$OUTPUT_DIR/2026-03-25-被動收入入門-cover.png"

echo "✅ 已生成：2026-03-25-被動收入入門-cover.png"

# 文章2：提升工作效率（學習類）
convert -size ${WIDTH}x${HEIGHT} \
  -background "#2d3748" \
  -fill "#48bb78" \
  -font DejaVu-Sans-Bold \
  -pointsize 20 \
  -gravity NorthWest \
  -annotate +100+180 "#學習成長" \
  -fill "#ffffff" \
  -pointsize 48 \
  -annotate +100+260 "提升工作效率的五個技巧" \
  -pointsize 28 \
  -fill "#718096" \
  -annotate +100+340 "讓你的工作事半功倍" \
  -fill "#48bb78" \
  -draw "rectangle 0,0 1200,8" \
  -draw "rectangle 60,200 68,430" \
  -fill "rgba(255,255,255,0.1)" \
  -draw "rectangle 0,570 1200,630" \
  "$OUTPUT_DIR/2025-03-25-提升工作效率-cover.png"

echo "✅ 已生成：2025-03-25-提升工作效率-cover.png"

# 文章3：GitHub Pages 教學（技術類）
convert -size ${WIDTH}x${HEIGHT} \
  -background "#1a202c" \
  -fill "#4299e1" \
  -font DejaVu-Sans-Bold \
  -pointsize 20 \
  -gravity NorthWest \
  -annotate +100+180 "#技術教學" \
  -fill "#ffffff" \
  -pointsize 48 \
  -annotate +100+260 "GitHub Pages 部落格教學" \
  -pointsize 28 \
  -fill "#4a5568" \
  -annotate +100+340 "從零開始建立個人網站" \
  -fill "#4299e1" \
  -draw "rectangle 0,0 1200,8" \
  -draw "rectangle 60,200 68,430" \
  -fill "rgba(255,255,255,0.1)" \
  -draw "rectangle 0,570 1200,630" \
  "$OUTPUT_DIR/2026-03-20-github-pages-blog-cover.png"

echo "✅ 已生成：2026-03-20-github-pages-blog-cover.png"

echo ""
echo "✨ 完成！共生成 3 張封面圖"
echo "📁 存放位置：$OUTPUT_DIR"
ls -la "$OUTPUT_DIR"
