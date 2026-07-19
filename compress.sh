#!/bin/bash
cd /Users/siyuli/Seeyuuuuuu.github.io/assets

echo "Compressing images..."
find Project-* -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) | while read img; do
    echo "Processing $img..."
    base="${img%.*}"
    
    # Use macOS built-in sips to resize to max 1920px and convert to 85% quality JPEG
    sips -Z 1920 -s format jpeg -s formatOptions 85 "$img" --out "${base}.jpg" > /dev/null
    
    # Remove the original file if the extension was different
    if [[ "$img" != "${base}.jpg" ]]; then
        rm "$img"
    fi
done

cd /Users/siyuli/Seeyuuuuuu.github.io/
echo "Updating HTML references..."
find . -maxdepth 1 -name "*.html" -type f | while read html; do
    perl -pi -e 's/(Project-\d+_[a-zA-Z0-9]+)\.(png|PNG|jpg|JPG|jpeg|JPEG)/$1.jpg/g' "$html"
done

echo "Committing changes..."
git add .
git commit -m "Optimize massive images to fix slow loading and save bandwidth"
git push -u origin main
echo "Done!"
