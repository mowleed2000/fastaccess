import os
import urllib.parse
import shutil

dest_dir = r"C:\Users\fifia\.gemini\antigravity\scratch\fast-access"
os.makedirs(dest_dir, exist_ok=True)

# ----------------- Copy and Optimize Laptop Assets -----------------
SOURCE_DIR_LAPTOP = r"C:\Users\fifia\Downloads\Laptop repair reusable assets"

LAPTOP_MAPPING = {
    "`repair-hero.jpg`.jpg": "laptop-repair-hero.jpg",
    "technician.jpg (2).jpg": "laptop-technician.jpg",
    "circuit-board.jpg (2).jpg": "laptop-circuit-board.jpg",
    "broken-screen.jpg.jpg": "laptop-broken-screen.jpg",
    "slow-computer.jpg.jpg": "laptop-slow-computer.jpg",
    "virus-removal.jpg": "laptop-virus-removal.jpg",
    "data-recovery.jpg.jpg": "laptop-data-recovery.jpg",
    "ram-upgrade.jpg.jpg": "laptop-ram-upgrade.jpg",
    "keyboard-repair.jpg": "laptop-keyboard-repair.jpg",
    "water-damage.jpg": "laptop-water-damage.jpg",
    "Screen broken laptop image 1.jpg.jpg": "laptop-screen-broken.jpg",
    "Screen being repaired image 2.jpg.jpg": "laptop-screen-repairing.jpg",
    "Screen fixed image 3.jpg": "laptop-screen-fixed.jpg",
    "Slow computer image 1.jpg.jpg": "laptop-slow-before.jpg",
    "Performance tuneup image 2.jpg.jpg": "laptop-performance-repairing.jpg",
    "Fast computer fixed image 3.jpg.jpg": "laptop-performance-fixed.jpg",
    "Virus warning image 1.jpg.jpg": "laptop-virus-before.jpg",
    "Virus removal image 2.jpg.jpg": "laptop-virus-repairing.jpg",
    "Clean computer image 3.jpg": "laptop-virus-fixed.jpg",
    "Data loss image 1.jpg": "laptop-data-before.jpg",
    "Data recovery image 2.jpg": "laptop-data-repairing.jpg",
    "Data recovered image 3.jpg.jpg": "laptop-data-fixed.jpg",
    "Upgrade before image 1.jpg": "laptop-ram-before.jpg",
    "Upgrade install image 2.jpg": "laptop-ram-repairing.jpg",
    "Upgrade after image 3.jpg`.jpg": "laptop-ram-fixed.jpg",
    "Keyboard broken image 1.jpg": "laptop-keyboard-before.jpg",
    "Keyboard repair image 2.jpg": "laptop-keyboard-repairing.jpg",
    "Keyboard fixed image 3.jpg": "laptop-keyboard-fixed.jpg",
    "Water damage laptop image 1.jpg": "laptop-water-before.jpg",
    "Water damage repair image 2.jpg": "laptop-water-repairing.jpg",
    "Water damage fixed image 3.jpg.jpg": "laptop-water-fixed.jpg",
    "Power issue image 1.jpg": "laptop-power-before.jpg",
    "Power repair image 2.jpg": "laptop-power-repairing.jpg",
    "Power fixed image 3.jpg.jpg": "laptop-power-fixed.jpg"
}

# ----------------- Copy and Optimize Phone and Vape Assets -----------------
SOURCE_DIR_DOWNLOADS = r"C:\Users\fifia\Downloads"

PHONE_MAPPING = {
    "velo nicotine pouches.webp": "velo nicotine pouches.webp",
    # Custom Storefront
    r"Fast Access\Fast Access Exteriror.webp": "exterior.webp",
    
    # Phone assets
    "Screen broken screen repair page image 1.jpg": "Screen broken screen repair page image 1.jpg",
    "Screen being repaired image 2.jpg": "Screen being repaired image 2.jpg",
    "Screen fixed image 3.jpg": "Screen fixed image 3.jpg",
    "Battery Replacment page 1.jpg": "Battery dead image 1.jpg",
    "Battery replacment page 2.jpg": "Battery replacment page 2.jpg",
    "Battery fixed 100 percent.jpg": "Battery fixed 100 percent.jpg",
    "Water damage phone water damage image 1.jpg": "Water damage phone water damage image 1.jpg",
    "Water damage being repaired.jpg": "Water damage being repaired.jpg",
    "Water damage repaired.jpg": "Water damage repaired.jpg",
    "Charger port broken image 1.webp": "Charger port broken image 1.webp",
    "Charger port being fixed.jpg": "Charger port being fixed.jpg",
    "Charger port fixed.webp": "Charger port fixed.webp",
    "Phone sim not supported image 1 unlock.png": "Phone sim not supported image 1 unlock.png",
    "Phone being unblocked.jpg": "Phone being unblocked.jpg",
    "Use the provider you want image 3.jpg": "Use the provider you want image 3.jpg",
    "Tablet wont turn on.webp": "Tablet wont turn on.webp",
    "Laptop broken image 1.jpg": "Laptop broken image 1.jpg",
    "Laptop and tablet fixed.jpg": "Laptop and tablet fixed.jpg",
    "Nordic Reuse.webp": "Nordic Reuse.webp",
    "Velo reuse.jpg": "Velo reuse.jpg",
    "Pablo reuse.jpg": "Pablo reuse.jpg",
    "ZYN Pouches Reuse.webp": "ZYN Pouches Reuse.webp",
    "Lost Mary reuse.jpg": "Lost Mary reuse.jpg",
    "IVG Reuse 1.jpg": "IVG Reuse 1.jpg",
    "Elf reuse.jpg": "Elf reuse.jpg",
    "Iphone 17 pro max.webp": "Iphone 17 pro max.webp",
    "Iphone 17.webp": "Iphone 17.webp",
    "Samsung s26 ultra.webp": "Samsung s26 ultra.webp",
    "Samsung Flip 6.webp": "Samsung Flip 6.webp",
    "Google Pixel 10a.webp": "Google Pixel 10a.webp",
    "battery-repair.jpg.jpg": "battery-repair.jpg",
    "charging-port.jpg.jpg": "charging-port.jpg",
    "cracked-screen.jpg.jpg": "cracked-screen.jpg",
    "slow-computer.jpg.jpg": "slow-computer.jpg",
    "technician.jpg.jpg": "technician.jpg",
    "unlock-phone.jpg.jpg": "unlock-phone.jpg",
    "virus-removal.jpg": "virus-removal.jpg",
    "water-damage.jpg.jpg": "water-damage.jpg",
    "circuit-board.jpg.jpg": "circuit-board.jpg",
    "repair-hero.jpg.jpg": "repair-hero.jpg"
}

def copy_and_optimize_asset(src_path, dest_path):
    ext = os.path.splitext(dest_path.lower())[1]
    if ext in ['.jpg', '.jpeg', '.png', '.webp']:
        try:
            from PIL import Image
            img = Image.open(src_path)
            
            # Convert to RGB for JPEG compatibility
            if ext in ['.jpg', '.jpeg']:
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[3])
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
            
            # Resize
            max_dim = 1600 if ("hero" in dest_path or "storefront" in dest_path or "technician" in dest_path or "exterior" in dest_path) else 1200
            if img.width > max_dim or img.height > max_dim:
                img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
                
            # Compress and save
            if ext in ['.jpg', '.jpeg']:
                img.save(dest_path, 'JPEG', quality=75)
            elif ext == '.webp':
                img.save(dest_path, 'WEBP', quality=75)
            else:
                img.save(dest_path, optimize=True)
            return True
        except Exception as e:
            print(f"PIL compression failed for {src_path}: {e}. Falling back to copy.")
            
    # Fallback to direct copy
    shutil.copy2(src_path, dest_path)
    return True

# Copy laptop assets
for src_name, dest_name in LAPTOP_MAPPING.items():
    src_path = os.path.join(SOURCE_DIR_LAPTOP, src_name)
    if os.path.exists(src_path):
        dest_path = os.path.join(dest_dir, dest_name)
        copy_and_optimize_asset(src_path, dest_path)

# Copy phone and vape assets
for src_name, dest_name in PHONE_MAPPING.items():
    src_path = os.path.join(SOURCE_DIR_DOWNLOADS, src_name)
    if os.path.exists(src_path):
        dest_path = os.path.join(dest_dir, dest_name)
        copy_and_optimize_asset(src_path, dest_path)

# Copy final missing products from C:\Users\fifia\Downloads\Final missing products
SOURCE_DIR_MISSING = r"C:\Users\fifia\Downloads\Final missing products"

MISSING_MAPPING = {
    "Crystal 600.jpg": "SKE Crystal 600 Pro.jpg",
    "Elements rizla thin.jpg": "Elements Rice Papers.jpg",
    "Fizzy juice e liquid.jpg": "Fizzy Juice Strawberry.jpg",
    "Ipad mini 4.jpg": "iPad mini 4.jpg",
    "Nexlim.jpg": "OXVA Nexlim.jpg",
    "Pyne poo.jpg": "Pyne pod click.jpg",
    "Ramillion nic salts.jpg": "Ramillion nic salts.jpg",
    "Skruff nicotine pouches.jpg": "Skruf nicotine pouches.jpg",
    "T20 Coil.jpg": "Innokin T20 Coils.jpg"
}

for src_name, dest_name in MISSING_MAPPING.items():
    src_path = os.path.join(SOURCE_DIR_MISSING, src_name)
    if os.path.exists(src_path):
        # Save optimized image in the Fast acsess images folder
        dest_path_web = os.path.join(dest_dir, "Fast acsess images", dest_name)
        copy_and_optimize_asset(src_path, dest_path_web)
        
        # Keep workspace folder in sync
        dest_path_ws = os.path.join(r"C:\Users\fifia\.gemini\antigravity\scratch\Fast acsess images", dest_name)
        copy_and_optimize_asset(src_path, dest_path_ws)


# Copy final products 2 from C:\Users\fifia\Downloads\Final products 2
SOURCE_DIR_PRODUCTS_2 = r"C:\Users\fifia\Downloads\Final products 2"

PRODUCTS_2_MAPPING = {
    "Aspire vape kit.jpg": "Aspire PockeX Kit.jpg",
    "EE sim cards.png": "EE SIM Card.png",
    "Geek vape.jpg": "Geekvape Aegis Kit.jpg",
    "Giff Gaff sim cards.jpg": "Giffgaff SIM Card.jpg",
    "Lebara Sim cards.webp": "Lebara SIM Card.webp",
    "Lyca sim card.jpg": "Lycamobile SIM Card.jpg",
    "Smok TFV16.jpg": "SMOK TFV16 Tank.jpg",
    "Vaporesso gtx one.jpg": "Vaporesso GTX One Kit.jpg",
    "Vaporesso gtx pod 26.jpg": "Vaporesso GTX Pod 26.jpg",
    "Vodafone sim cards.webp": "Vodafone SIM Card.webp",
    "Vopoo Drag nano 2.jpg": "Voopoo Drag Nano 2 Kit.jpg",
    "efest lush.jpg": "Efest Lush Q2 Charger.jpg"
}

for src_name, dest_name in PRODUCTS_2_MAPPING.items():
    src_path = os.path.join(SOURCE_DIR_PRODUCTS_2, src_name)
    if os.path.exists(src_path):
        # Save optimized image in the Fast acsess images folder
        dest_path_web = os.path.join(dest_dir, "Fast acsess images", dest_name)
        copy_and_optimize_asset(src_path, dest_path_web)
        
        # Keep workspace folder in sync
        dest_path_ws = os.path.join(r"C:\Users\fifia\.gemini\antigravity\scratch\Fast acsess images", dest_name)
        copy_and_optimize_asset(src_path, dest_path_ws)

# Copy generated assets for printing and internet cafe
GEN_MAPPING = {
    r"C:\Users\fifia\.gemini\antigravity\brain\571e72ac-f890-4811-926b-8bab69fa346e\printing_service_1781715100044.png": "printing-service.jpg",
    r"C:\Users\fifia\.gemini\antigravity\brain\571e72ac-f890-4811-926b-8bab69fa346e\passport_photo_1781715110351.png": "passport-photo.jpg",
    r"C:\Users\fifia\.gemini\antigravity\brain\571e72ac-f890-4811-926b-8bab69fa346e\internet_cafe_1781715121841.png": "internet-cafe.jpg"
}
for gen_path, dest_name in GEN_MAPPING.items():
    if os.path.exists(gen_path):
        dest_path = os.path.join(dest_dir, dest_name)
        copy_and_optimize_asset(gen_path, dest_path)


# Copy new download assets from C:\Users\fifia\Downloads
SOURCE_DIR_DOWNLOADS = r"C:\Users\fifia\Downloads"
NEW_DOWNLOADS = [
    "45W Charger.jpg",
    "CBD Leaf.jpg",
    "CBD Royale.jpg",
    "Elf Bar 600.jpg",
    "Elfa Pro Kit.jpg",
    "Hayati Pro Max 4000.jpg",
    "Honor X6.jpg",
    "IVG 600.jpg",
    "Pixl 6000..jpg",
    "Podmate Nic Salts.jpg",
    "SKE Crystal Salts.jpg",
    "Security Camera.jpg",
    "Tuned In Cherry.jpg",
    "Vuse Go.jpg",
    "Vuse epod.jpg",
    "Wicked Haze.jpg",
    "Yesplus mini fan.webp",
    "MTK External Hard Drive.jpg",
    "MTK SSD.jpg",
    "Samsung Type-C Cable.png",
    "cola.jpg",
    "water.jpg",
    "Redbull.webp"
]

for name in NEW_DOWNLOADS:
    src_path = os.path.join(SOURCE_DIR_DOWNLOADS, name)
    if os.path.exists(src_path):
        dest_path_web = os.path.join(dest_dir, "Fast acsess images", name)
        copy_and_optimize_asset(src_path, dest_path_web)
        
        dest_path_ws = os.path.join(r"C:\Users\fifia\.gemini\antigravity\scratch\Fast acsess images", name)
        copy_and_optimize_asset(src_path, dest_path_ws)

print("All assets copied and optimized successfully.")

# ----------------- Write style.css -----------------
css_content = """/* Fast Access Vape & Mobile & Laptop Repair Stylesheet */
:root {
    --ink: #141414;
    --magenta: #E6157B;
    --magenta-deep: #B30E5F;
    --paper: #FFFFFF;
    --mist: #F5F5F7;
    --slate: #5A5A60;

    --bg-main: var(--paper);
    --bg-card: var(--paper);
    --bg-alternate: var(--mist);
    --text-main: var(--ink);
    --text-muted: var(--slate);
    --border-color: var(--mist);
    --primary: var(--magenta);
    --primary-hover: var(--magenta-deep);
    --primary-glow: rgba(230, 21, 123, 0.12);
    --shadow: 0 10px 30px rgba(20, 20, 20, 0.04);
    --font-sans: 'Inter', sans-serif;
    --font-heading: 'Inter', sans-serif;
    --nav-height: 80px;
}

/* Global Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body {
    width: 100%;
    overflow-x: hidden;
    background-color: var(--bg-main);
    color: var(--text-main);
    font-family: var(--font-sans);
    font-size: 1.0625rem;
    line-height: 1.6;
    scroll-behavior: smooth;
}

/* Layout Utilities */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
    width: 100%;
}

.text-center {
    text-align: center;
}

.primary-text {
    color: var(--primary);
}

.accent-divider {
    width: 50px;
    height: 4px;
    background-color: var(--primary);
    margin: 16px auto 0;
    border-radius: 2px;
}

.section-subtitle {
    display: inline-block;
    font-family: var(--font-heading);
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: var(--primary);
    margin-bottom: 12px;
}

/* Typography */
h1, h2, h3, h4 {
    font-family: var(--font-heading);
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.25;
}

/* Scroll Animations */
.reveal {
    opacity: 0;
    transform: translateY(10px);
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.reveal.active {
    opacity: 1;
    transform: translateY(0);
}

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 12px 28px;
    font-family: var(--font-sans);
    font-size: 0.95rem;
    font-weight: 600;
    text-decoration: none;
    border-radius: 4px;
    transition: all 0.25s ease;
    cursor: pointer;
    border: none;
}

.btn-primary {
    background-color: var(--primary);
    color: #ffffff;
    box-shadow: 0 4px 14px var(--primary-glow);
}

.btn-primary:hover {
    background-color: var(--primary-hover);
    transform: translateY(-1.5px);
    box-shadow: 0 6px 20px var(--primary-glow);
}

.btn-outline {
    background-color: transparent;
    color: var(--text-main);
    border: 1px solid var(--text-main);
}

.btn-outline:hover {
    background-color: var(--bg-alternate);
    border-color: var(--text-main);
    color: var(--text-main);
    transform: translateY(-1.5px);
}


.w-100 {
    width: 100%;
}

/* Navigation Bar */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: var(--nav-height);
    background-color: rgba(255, 255, 255, 0.98);
    border-bottom: 1px solid var(--border-color);
    z-index: 1000;
    display: flex;
    align-items: center;
}


.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.logo {
    display: flex;
    flex-direction: column;
    line-height: 1.1;
    text-decoration: none;
    margin-right: 15px;
}
.logo-main {
    font-family: var(--font-heading);
    font-size: 1.25rem;
    font-weight: 900;
    letter-spacing: -0.5px;
    color: var(--text-main);
}
.logo-sub {
    font-family: var(--font-sans);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.logo .primary-text {
    color: var(--primary);
}

.nav-links {
    display: flex;
    align-items: center;
    list-style: none;
    gap: 10px;
}

.nav-links a {
    color: var(--text-muted);
    text-decoration: none;
    font-size: 0.8rem;
    font-weight: 600;
    transition: color 0.2s ease;
    white-space: nowrap;
}

.nav-links a:hover {
    color: var(--primary);
}

.btn-nav-cta {
    background-color: transparent;
    color: var(--primary) !important;
    border: 1px solid var(--primary) !important;
    padding: 8px 18px !important;
    border-radius: 4px;
    font-family: var(--font-sans);
    font-size: 0.85rem;
    font-weight: 600;
}

.btn-nav-cta:hover {
    background-color: var(--primary) !important;
    color: #ffffff !important;
}

.hamburger {
    display: none;
    color: var(--text-main);
    font-size: 1.3rem;
    cursor: pointer;
}

/* Double Dropdown Menus */
.dropdown {
    position: relative;
}

.dropdown-menu {
    display: none;
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    box-shadow: var(--shadow);
    list-style: none;
    min-width: 250px;
    border-radius: 4px;
    padding: 8px 0;
    z-index: 100;
    text-align: left;
}

.dropdown-menu li a {
    display: block;
    padding: 8px 16px;
    color: var(--text-main);
    font-size: 0.9rem;
}

.dropdown-menu li a:hover {
    background-color: var(--bg-alternate);
    color: var(--primary);
}

.dropdown-menu .dropdown-header {
    padding: 8px 16px 4px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--primary);
    letter-spacing: 0.5px;
    pointer-events: none;
}

.dropdown-menu .dropdown-divider {
    height: 1px;
    background-color: var(--border-color);
    margin: 6px 0;
}

.dropdown:hover .dropdown-menu {
    display: block;
}

/* Hero Section */
.hero {
    padding: calc(var(--nav-height) + 60px) 0 80px;
    background-size: cover;
    background-position: center;
    position: relative;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0;
    align-items: center;
    max-width: 820px;
}

.hero-content .eyebrow {
    font-family: var(--font-sans);
    color: var(--primary);
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 16px;
    display: block;
}

.hero h1 {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 24px;
}

.hero-title-line-1 {
    font-size: clamp(2.75rem, 6vw, 4.5rem);
    line-height: 1.05;
    letter-spacing: -0.02em;
    font-family: var(--font-heading);
    font-weight: 800;
    color: var(--text-main);
}

.hero-title-line-2 {
    font-size: clamp(1.8rem, 4vw, 2.75rem);
    line-height: 1.1;
    font-family: var(--font-heading);
    font-weight: 500;
    color: var(--slate);
    letter-spacing: -0.01em;
}

.hero-tagline {
    font-size: 1.0625rem;
    line-height: 1.6;
    color: var(--text-muted);
    margin-bottom: 30px;
}

.hero-btns {
    display: flex;
    gap: 16px;
    margin-bottom: 32px;
}

.hero-trust-strip {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-top: 32px;
    flex-wrap: wrap;
}

.trust-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text-main);
}

.trust-item i {
    color: var(--magenta);
    font-size: 1.1rem;
}

.trust-divider {
    width: 1px;
    height: 20px;
    background-color: var(--border-color);
}

@media (max-width: 576px) {
    .hero-trust-strip {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
    }
    .trust-divider {
        display: none;
    }
}

.hero-image-wrapper {
    position: relative;
    width: 100%;
}

.hero-image-frame {
    position: relative;
    border: 1px solid var(--border-color);
    border-bottom: 4px solid var(--magenta);
    padding: 0;
    border-radius: 4px;
    background-color: var(--bg-card);
    box-shadow: 0 20px 50px -20px rgba(0,0,0,0.35);
    cursor: pointer;
    overflow: hidden;
}

.hero-image {
    width: 100%;
    border-radius: 4px;
    display: block;
    object-fit: cover;
    aspect-ratio: 1/1;
    transition: transform 0.4s ease;
}

.hero-image-frame:hover .hero-image {
    transform: scale(1.015);
}

.frame-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(20, 20, 20, 0.9);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
    color: #ffffff;
    opacity: 0;
    transition: opacity 0.25s ease;
    border-radius: 4px;
}

.hero-image-frame:hover .frame-overlay {
    opacity: 1;
}

.frame-overlay i {
    font-size: 1.5rem;
    color: var(--primary);
}

.frame-overlay span {
    font-family: var(--font-sans);
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Services Grid Section */
.services {
    padding: 80px 0;
    background-color: var(--bg-alternate);
    border-top: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
}

.services .section-header {
    margin-bottom: 40px;
}

.services .subheading {
    color: var(--text-muted);
    font-size: 1.05rem;
    margin-top: 8px;
}

.services-category-title {
    font-family: var(--font-heading);
    font-size: 1.6rem;
    margin-top: 40px;
    margin-bottom: 20px;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 12px;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
}

.services-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.services-grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    max-width: 800px;
    margin: 0 auto;
}

.service-card-link {
    text-decoration: none;
}

.service-card {
    height: 270px;
    border-radius: 8px;
    background-size: cover;
    background-position: center;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: flex-end;
    border: 1px solid var(--border-color);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.service-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
}

.service-badge {
    position: absolute;
    top: 20px;
    left: 20px;
    background-color: var(--primary);
    color: #ffffff;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-family: var(--font-heading);
    font-weight: 700;
}

.card-content {
    padding: 20px;
    color: #ffffff;
    width: 100%;
    z-index: 2;
    background: linear-gradient(to top, rgba(15, 23, 42, 0.95), rgba(15, 23, 42, 0.4) 70%, transparent);
}

.service-card-link .card-content {
    background: linear-gradient(to top, rgba(15, 23, 42, 0.95), rgba(15, 23, 42, 0.3) 70%, rgba(15, 23, 42, 0.1));
}

.service-card h3 {
    font-size: 1.25rem;
    margin-bottom: 6px;
    color: #ffffff;
}

.service-card p {
    font-size: 0.8rem;
    color: rgba(255, 255, 255, 0.85);
    margin-bottom: 10px;
    line-height: 1.4;
}

.learn-more {
    font-family: var(--font-heading);
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--primary);
}

/* Booking Section & Form */
.booking-section {
    padding: 80px 0;
}

.booking-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.contact-bullets {
    margin-top: 32px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.bullet-item {
    display: flex;
    gap: 16px;
    align-items: flex-start;
}

.bullet-item i {
    font-size: 1.25rem;
    color: var(--primary);
    margin-top: 3px;
}

.bullet-item strong {
    font-family: var(--font-heading);
    font-size: 1rem;
    margin-bottom: 4px;
    display: block;
}

.bullet-item p {
    font-size: 0.85rem;
    color: var(--text-muted);
}

.booking-form-wrapper {
    background-color: var(--bg-alternate);
    border: 1px solid var(--border-color);
    padding: 40px;
    border-radius: 8px;
    box-shadow: var(--shadow);
}

.native-booking-form {
    display: flex;
    flex-direction: column;
    gap: 18px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.form-group-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
}

.form-group label {
    font-family: var(--font-heading);
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text-main);
}

.form-group input, .form-group select, .form-group textarea {
    padding: 10px 14px;
    font-family: var(--font-sans);
    font-size: 0.9rem;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    background-color: #ffffff;
    color: var(--text-main);
    outline: none;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
    border-color: var(--primary);
    box-shadow: 0 0 0 3px var(--primary-glow);
}

.radio-group {
    display: flex;
    flex-direction: row;
    gap: 16px;
    margin-top: 8px;
    padding-left: 0;
}

@media (max-width: 768px) {
    .radio-group {
        flex-direction: column;
        gap: 10px;
    }
}

.radio-label {
    display: flex;
    align-items: center;
    gap: 10px;
    font-family: var(--font-sans);
    font-size: 0.85rem;
    color: var(--text-main);
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 10px 16px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    flex: 1;
}

.radio-label:hover {
    border-color: var(--primary);
    background-color: var(--bg-alternate);
}

.radio-label input {
    cursor: pointer;
    accent-color: var(--primary);
    margin: 0;
}

/* Why Us Section */
.why-us {
    padding: 80px 0;
    border-top: 1px solid var(--border-color);
}

.why-us-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    margin-top: 48px;
}

.why-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 32px;
    box-shadow: var(--shadow);
}

.why-icon {
    font-size: 2.2rem;
    color: var(--primary);
    margin-bottom: 20px;
}

.why-card h3 {
    font-size: 1.25rem;
    margin-bottom: 12px;
}

.why-card p {
    color: var(--text-muted);
    font-size: 0.9rem;
}

/* Phones Teaser (Handset Showcase) */
.phones-teaser {
    padding: 80px 0;
}

.phones-teaser-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 48px;
    align-items: center;
}

.phones-teaser-content h2 {
    font-size: 2.5rem;
    margin-bottom: 16px;
}

.phones-teaser-content p {
    color: var(--text-muted);
    margin-bottom: 24px;
    font-size: 1.05rem;
}

.phone-anchors-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}

.phone-item-card {
    text-align: center;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 16px;
    border-radius: 8px;
    box-shadow: var(--shadow);
}

.phone-item-card img {
    width: 100%;
    height: auto;
    max-height: 120px;
    object-fit: contain;
    margin-bottom: 10px;
}

.phone-item-card span {
    font-family: var(--font-heading);
    font-size: 0.8rem;
    font-weight: 600;
}

/* Reviews on Home */
.reviews {
    padding: 80px 0;
    background-color: var(--bg-alternate);
    border-top: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
}

.reviews-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 40px;
}

.review-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 32px;
    border-radius: 8px;
    box-shadow: var(--shadow);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.review-card .review-text {
    font-style: italic;
    font-size: 0.95rem;
    color: var(--text-muted);
    margin-bottom: 20px;
}

.review-author {
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 0.85rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.stars {
    color: #ffb400;
    font-size: 0.8rem;
}

/* Final CTA */
.final-cta {
    padding: 100px 0;
    background-size: cover;
    background-position: center;
    color: #ffffff;
}

.final-cta h2 {
    font-size: 2.8rem;
    margin-bottom: 16px;
    color: #ffffff;
}

.final-cta p {
    font-size: 1.1rem;
    color: rgba(255, 255, 255, 0.9);
    margin-bottom: 30px;
}

.btn-large {
    padding: 14px 40px;
    font-size: 1.05rem;
}

/* Service Page Styling */
.service-hero {
    padding: 125px 0 80px;
    background-size: cover;
    background-position: center;
    color: #ffffff;
}

.service-hero h1 {
    font-size: 3.2rem;
    color: #ffffff;
    margin-bottom: 16px;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.85);
}

.service-hero p {
    font-size: 1.15rem;
    color: rgba(255, 255, 255, 0.95);
    margin-bottom: 28px;
    text-shadow: 0 2px 6px rgba(0, 0, 0, 0.85);
}

.details-grid {
    display: grid;
    grid-template-columns: 1.05fr 0.95fr;
    gap: 60px;
    align-items: center;
}

.service-details {
    padding: 80px 0;
}

.details-text h2 {
    font-size: 2.2rem;
    margin-bottom: 20px;
}

.details-text p {
    color: var(--text-muted);
    font-size: 1.05rem;
    margin-bottom: 24px;
}

.symptoms-box {
    background-color: var(--bg-alternate);
    border: 1px solid var(--border-color);
    padding: 24px;
    border-radius: 6px;
}

.symptoms-box h3 {
    font-size: 1.1rem;
    margin-bottom: 16px;
}

.symptoms-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.symptoms-list li {
    font-size: 0.9rem;
    color: var(--text-muted);
    position: relative;
    padding-left: 28px;
    line-height: 1.6;
}

.symptoms-list li i {
    position: absolute;
    left: 0;
    top: 4px;
    color: var(--primary);
}

.in-process-img {
    width: 100%;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    box-shadow: var(--shadow);
}

.service-gallery {
    padding: 60px 0;
    background-color: var(--bg-alternate);
    border-top: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
}

.gallery-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 40px;
}

.gallery-item-wrapper {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 8px;
    cursor: pointer;
    text-align: center;
    box-shadow: var(--shadow);
    overflow: hidden;
}

.gallery-item-wrapper img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 4px;
    margin-bottom: 8px;
}

.gallery-item-wrapper span {
    font-family: var(--font-heading);
    font-size: 0.85rem;
    font-weight: 600;
}

/* Screenshot containment removed to prevent pillarboxing */

.service-cta {
    padding: 80px 0;
}

.service-cta h2 {
    font-size: 2.2rem;
    margin-bottom: 12px;
}

.service-cta p {
    color: var(--text-muted);
    margin-bottom: 24px;
}

.related-services {
    padding: 80px 0;
    background-color: var(--bg-alternate);
    border-top: 1px solid var(--border-color);
}

.related-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 40px;
}

.related-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 28px;
    border-radius: 6px;
    box-shadow: var(--shadow);
}

.related-card h3 {
    font-size: 1.2rem;
    margin-bottom: 10px;
}

.related-card p {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-bottom: 16px;
}

/* Page Hero Template */
.page-hero {
    padding: calc(var(--nav-height) + 40px) 0 40px;
    border-bottom: 1px solid var(--border-color);
    background-color: var(--bg-alternate);
}

.page-hero h1 {
    font-size: 2.8rem;
    margin-bottom: 8px;
}

.page-hero p {
    font-size: 1.05rem;
    color: var(--text-muted);
}

/* Phones/Vapes Page Specific */
.phones-section {
    padding: 80px 0;
}

.intro-paragraph {
    max-width: 700px;
    margin: 0 auto 48px;
    font-size: 1.05rem;
    color: var(--text-muted);
}

.phones-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 24px;
}

.phone-product-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 24px;
    border-radius: 8px;
    text-align: center;
    box-shadow: var(--shadow);
}

.phone-product-card img {
    width: 100%;
    height: 180px;
    object-fit: contain;
    margin-bottom: 16px;
}

.phone-product-card h3 {
    font-size: 1.15rem;
    margin-bottom: 8px;
}

.avail-badge {
    display: inline-block;
    font-family: var(--font-heading);
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--primary);
    background-color: var(--primary-glow);
    padding: 4px 12px;
    border-radius: 20px;
}

/* Blog Page Specific */
.blog-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    margin-top: 48px;
}

@media (max-width: 1200px) {
    .blog-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .blog-grid {
        grid-template-columns: 1fr;
    }
}

.blog-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    overflow: hidden;
    box-shadow: var(--shadow);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    display: flex;
    flex-direction: column;
}

.blog-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
}

.blog-card-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.blog-card-content {
    padding: 24px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}

.blog-card-meta {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-bottom: 12px;
}

.blog-card h3 {
    font-size: 1.25rem;
    margin-bottom: 12px;
    line-height: 1.4;
    color: var(--text-main);
}

.blog-card p {
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 20px;
    line-height: 1.6;
    flex-grow: 1;
}

.blog-post-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 80px 24px;
}

.blog-post-header {
    text-align: center;
    margin-bottom: 40px;
}

.blog-post-header h1 {
    font-size: 3rem;
    margin-bottom: 20px;
}

.blog-post-meta {
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 40px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 20px;
}

.blog-post-content p {
    font-size: 1.05rem;
    color: var(--text-muted);
    line-height: 1.8;
    margin-bottom: 24px;
}

.blog-post-content h2, .blog-post-content h3 {
    margin-top: 40px;
    margin-bottom: 16px;
    color: var(--text-main);
}

/* Contact Page Specific */
.contact-details-section {
    padding: 80px 0;
}

.contact-grid-page {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: flex-start;
}

.contact-left-info h2 {
    font-size: 2.2rem;
    margin-bottom: 12px;
}

.phone-large {
    font-family: var(--font-heading);
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 30px;
}

.phone-large a {
    color: var(--primary);
    text-decoration: none;
}

.hours-box h3 {
    font-size: 1.1rem;
    margin-bottom: 16px;
}

.contact-hours-table {
    width: 100%;
    border-collapse: collapse;
}

.contact-hours-table tr {
    border-bottom: 1px solid var(--border-color);
}

.contact-hours-table tr:last-child {
    border-bottom: none;
}

.contact-hours-table td {
    padding: 10px 0;
    font-size: 0.95rem;
    color: var(--text-muted);
}

.contact-hours-table td:last-child {
    text-align: right;
    font-weight: 600;
    color: var(--text-main);
}

.contact-map-wrapper iframe {
    display: block;
    box-shadow: var(--shadow);
    border: 1px solid var(--border-color) !important;
    margin-top: 40px;
    border-radius: 8px;
}

.contact-images-section {
    padding: 60px 0;
    background-color: var(--bg-alternate);
    border-top: 1px solid var(--border-color);
}

.contact-image-container {
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

.contact-image-container img {
    border-radius: 8px;
    box-shadow: var(--shadow);
    max-height: 450px;
    object-fit: contain;
    width: 100%;
    margin-bottom: 15px;
}

.contact-image-caption {
    font-family: var(--font-heading);
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-muted);
}

/* Footer Styling */
.footer {
    padding: 60px 0 40px;
    background-color: #0f172a; /* Slate 900 */
    color: #ffffff;
}

.footer-grid {
    display: grid;
    grid-template-columns: 2fr 1.5fr 1.25fr 1.25fr;
    gap: 32px;
}

.footer-brand p {
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.6);
    margin-top: 12px;
}

.footer-logo {
    font-family: var(--font-heading);
    font-size: 1.3rem;
    font-weight: 800;
    color: #ffffff;
    text-decoration: none;
    letter-spacing: -0.5px;
    display: flex;
    flex-direction: column;
    line-height: 1.2;
}

.footer-logo .logo-main {
    color: #ffffff !important;
    font-size: 1.3rem;
    font-weight: 900;
}

.footer-logo .primary-text {
    color: var(--primary);
}

.footer-links h4, .footer-hours h4, .footer-contact h4 {
    font-size: 0.9rem;
    font-family: var(--font-heading);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #ffffff;
    margin-bottom: 16px;
}

.footer-services-list {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px 16px;
    list-style: none;
    padding: 0;
    margin: 0;
}

.footer-services-list li a {
    color: rgba(255, 255, 255, 0.6);
    text-decoration: none;
    font-size: 0.85rem;
    transition: color 0.2s ease;
}

.footer-services-list li a:hover {
    color: var(--primary);
}

.footer-hours ul {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.6);
}

.footer-contact p {
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.6);
    margin-bottom: 6px;
}

.footer-contact p.phone-num a {
    font-family: var(--font-heading);
    font-weight: 700;
    color: var(--primary);
    font-size: 1.1rem;
    text-decoration: none;
}

.footer-contact p.address-num {
    font-size: 0.8rem;
    color: rgba(255, 255, 255, 0.5);
    margin-top: 10px;
}

.footer-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    padding-top: 30px;
    margin-top: 48px;
    color: rgba(255, 255, 255, 0.4);
    font-size: 0.8rem;
    flex-wrap: wrap;
    gap: 16px;
}

/* Lightbox Modal */
.lightbox {
    display: none;
    position: fixed;
    z-index: 2000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(15, 23, 42, 0.98);
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.lightbox.active {
    display: flex;
}

.lightbox-content {
    margin: auto;
    display: block;
    max-width: 90%;
    max-height: 80vh;
    border-radius: 8px;
}

.lightbox-caption {
    margin: 15px auto;
    width: 80%;
    text-align: center;
    color: #ffffff;
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 1.1rem;
}

.lightbox-close {
    position: absolute;
    top: 24px;
    right: 32px;
    color: #ffffff;
    font-size: 2.5rem;
    font-weight: bold;
    cursor: pointer;
}

.lightbox-close:hover {
    color: var(--primary);
}

/* Native Booking Modal Styles */
.booking-modal {
    display: none;
    position: fixed;
    z-index: 3000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(15, 23, 42, 0.75);
    align-items: center;
    justify-content: center;
}

.booking-modal.active {
    display: flex;
}

.booking-modal-content {
    background-color: #ffffff;
    padding: 40px;
    border-radius: 8px;
    max-width: 480px;
    width: 90%;
    text-align: center;
    position: relative;
    box-shadow: 0 20px 50px rgba(15, 23, 42, 0.15);
}

.booking-modal-close {
    position: absolute;
    top: 15px;
    right: 20px;
    color: var(--text-muted);
    font-size: 1.8rem;
    font-weight: bold;
    cursor: pointer;
}

.booking-modal-close:hover {
    color: var(--text-main);
}

.modal-success-icon {
    font-size: 4rem;
    color: #10b981; /* Success Green */
    margin-bottom: 20px;
}

.booking-modal-content h2 {
    font-size: 1.8rem;
    margin-bottom: 12px;
    color: var(--text-main);
}

.booking-modal-content p {
    font-size: 0.95rem;
    color: var(--text-muted);
    margin-bottom: 24px;
    line-height: 1.5;
}

/* Continuous Country Marquee */
.country-marquee-section {
    padding: 30px 0;
    background-color: var(--bg-alternate);
    border-top: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
    overflow: hidden;
}

.marquee-title {
    font-family: var(--font-heading);
    font-size: 1.1rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--text-muted);
    margin-bottom: 20px;
}

.marquee-wrapper {
    width: 100%;
    overflow: hidden;
    position: relative;
}

.marquee-content {
    display: flex;
    gap: 30px;
    width: max-content;
    animation: scroll-marquee 25s linear infinite;
    will-change: transform;
}

.marquee-content:hover {
    animation-play-state: paused;
}

.marquee-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 1.05rem;
    color: var(--text-main);
    background-color: var(--bg-card);
    padding: 10px 20px;
    border-radius: 30px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
    white-space: nowrap;
}

.flag-icon {
    font-size: 1.3rem;
}

@keyframes scroll-marquee {
    0% {
        transform: translateX(0);
    }
    100% {
        transform: translateX(-50%);
    }
}

/* Process / How It Works Styles */
.process-section {
    padding: 80px 0;
    background-color: var(--bg-alternate);
}

.process-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 40px;
}

.process-step {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 40px 30px;
    border-radius: 8px;
    text-align: center;
    box-shadow: var(--shadow);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
}

.process-step:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(79, 70, 229, 0.08);
}

.process-number {
    position: absolute;
    top: 20px;
    right: 20px;
    font-family: var(--font-heading);
    font-size: 2.5rem;
    font-weight: 800;
    color: rgba(79, 70, 229, 0.06);
    line-height: 1;
}

.process-icon {
    font-size: 2.5rem;
    color: var(--primary);
    margin-bottom: 24px;
}

.process-step h3 {
    font-size: 1.25rem;
    margin-bottom: 12px;
    color: var(--text-main);
}

.process-step p {
    font-size: 0.95rem;
    color: var(--text-muted);
}

/* Compliance Badges Grid */
.compliance-badges-section {
    padding: 60px 0;
    background-color: var(--bg-main);
}

.badges-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
}

.badges-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}

.compliance-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 30px 20px;
    border-radius: 8px;
    text-align: center;
    box-shadow: var(--shadow);
    transition: transform 0.3s ease;
}

.compliance-card:hover {
    transform: translateY(-3px);
}

.compliance-icon {
    font-size: 2.2rem;
    color: var(--primary);
    margin-bottom: 16px;
}

.compliance-card h3 {
    font-size: 1.1rem;
    margin-bottom: 8px;
    color: var(--text-main);
}

.compliance-card p {
    font-size: 0.85rem;
    color: var(--text-muted);
    line-height: 1.5;
}

/* Review Slider Styles */
.reviews-slider-container {
    max-width: 800px;
    margin: 40px auto 0;
    position: relative;
    overflow: hidden;
    padding: 20px;
}

.reviews-wrapper {
    position: relative;
    min-height: 220px;
}

.review-slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    opacity: 0;
    transform: translateX(50px);
    transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    visibility: hidden;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 40px;
    border-radius: 8px;
    box-shadow: var(--shadow);
    text-align: center;
}

.review-slide.active {
    position: relative;
    opacity: 1;
    transform: translateX(0);
    visibility: visible;
}

.review-text {
    font-size: 1.1rem;
    font-style: italic;
    color: var(--text-main);
    margin-bottom: 24px;
    line-height: 1.6;
}

.review-author {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 16px;
    font-family: var(--font-heading);
    font-weight: 600;
}

.stars {
    color: #fbbf24;
    font-size: 0.9rem;
}

.slider-dots {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-top: 24px;
}

.dot {
    width: 10px;
    height: 10px;
    background-color: var(--border-color);
    border-radius: 50%;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.dot.active {
    background-color: var(--primary);
    transform: scale(1.2);
}

/* Responsive Rules */
@media (max-width: 1250px) {
    .hamburger { display: block; }
    .nav-links {
        display: none;
        flex-direction: column;
        position: absolute;
        top: var(--nav-height);
        left: 0;
        width: 100%;
        background-color: var(--bg-card);
        z-index: 1100;
        border-bottom: 1px solid var(--border-color);
        padding: 30px;
        gap: 20px;
        align-items: center;
        box-shadow: var(--shadow);
    }
    .nav-links.active { display: flex; }
    .dropdown {
        width: 100%;
        text-align: center;
    }
    .dropdown-trigger {
        display: block;
        width: 100%;
        text-align: center;
        padding: 10px 0;
    }
    .dropdown:hover .dropdown-menu {
        display: none;
    }
    .dropdown-menu { 
        display: none !important; 
        position: static; 
        box-shadow: none; 
        border: none; 
        text-align: center; 
        padding: 0; 
        transform: none; 
        width: 100%;
    }
    .dropdown-menu.active {
        display: block !important;
    }
}

@media (max-width: 992px) {
    h1 { font-size: 2.8rem !important; }
    h2 { font-size: 1.8rem !important; }
    .hero-grid { grid-template-columns: 1fr; text-align: center; }
    .hero-btns { justify-content: center; }
    .walk-ins-tag { justify-content: center; }
    .services-grid { grid-template-columns: repeat(2, 1fr); }
    .services-grid-3 { grid-template-columns: repeat(2, 1fr); }
    .services-grid-2 { grid-template-columns: repeat(2, 1fr); max-width: 100%; }
    .booking-grid { grid-template-columns: 1fr; }
    .why-us-grid { grid-template-columns: 1fr; gap: 20px; }
    .phones-teaser-grid, .contact-grid-page, .details-grid { grid-template-columns: 1fr; text-align: center; }
    .phone-anchors-grid { max-width: 500px; margin: 0 auto; }
    .reviews-grid, .related-grid, .phones-grid, .blog-grid { grid-template-columns: 1fr; }
    .footer-grid { grid-template-columns: repeat(2, 1fr); }
    .process-grid { grid-template-columns: 1fr; }
    .badges-grid, .badges-grid-3 { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
    .details-image {
        display: none !important;
    }
    .footer-grid { grid-template-columns: 1fr; text-align: center; }
    .footer-hours ul { align-items: center; }
    .footer-bottom { flex-direction: column; text-align: center; }
    .footer-services-list { grid-template-columns: 1fr; gap: 8px; justify-items: center; }
    .form-group-grid { grid-template-columns: 1fr; }
    .services-grid { grid-template-columns: 1fr; }
    .services-grid-3 { grid-template-columns: 1fr; }
    .services-grid-2 { grid-template-columns: 1fr; max-width: 400px; }
}

@media (max-width: 576px) {
    .badges-grid, .badges-grid-3 { grid-template-columns: 1fr; }
}

/* ==========================================================================
   Product Showcase & Filter Styling
   ========================================================================== */
.product-showcase-section {
    padding: 80px 0;
    background-color: var(--bg-main);
}

.product-filter-bar {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-bottom: 40px;
    padding: 0 15px;
}

.filter-btn {
    padding: 10px 20px;
    border-radius: 30px;
    border: 1px solid var(--border-color);
    background-color: var(--bg-alternate);
    color: var(--text-main);
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    outline: none;
}

.filter-btn:hover {
    border-color: var(--primary);
    color: var(--primary);
    transform: translateY(-2px);
}

.filter-btn.active {
    background-color: var(--primary);
    border-color: var(--primary);
    color: white;
}

.showcase-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
    padding: 0 15px;
}

@media (max-width: 1200px) {
    .showcase-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

@media (max-width: 992px) {
    .showcase-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 576px) {
    .showcase-grid {
        grid-template-columns: 1fr;
        max-width: 400px;
        margin: 0 auto;
    }
}

.product-card {
    display: flex;
    flex-direction: column;
    background-color: var(--bg-card);
    border-radius: 12px;
    border: 1px solid var(--border-color);
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    position: relative;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
    border-color: var(--primary);
}

.product-image-wrapper {
    position: relative;
    width: 100%;
    padding-top: 100%; /* 1:1 Aspect Ratio */
    background-color: #ffffff;
    overflow: hidden;
    border-bottom: 1px solid var(--border-color);
}

.product-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
    padding: 15px;
    transition: transform 0.5s ease;
}

.product-card:hover .product-image {
    transform: scale(1.05);
}

.product-category-badge {
    position: absolute;
    top: 12px;
    left: 12px;
    background-color: rgba(255, 255, 255, 0.9);
    color: var(--text-main);
    font-size: 0.7rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border: 1px solid var(--border-color);
    z-index: 2;
}

.product-details {
    padding: 20px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}

.product-title {
    font-family: var(--font-heading);
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 8px;
    line-height: 1.4;
}

.product-specs {
    font-size: 0.85rem;
    color: var(--text-muted);
    line-height: 1.5;
    margin-bottom: 15px;
    flex-grow: 1;
}

.product-price-row {
    margin-top: auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.base-price {
    font-family: var(--font-heading);
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--primary);
}

.contact-price {
    font-size: 0.85rem;
    font-weight: 700;
    color: #10b981;
    background-color: rgba(16, 185, 129, 0.08);
    padding: 4px 12px;
    border-radius: 20px;
    border: 1px solid rgba(16, 185, 129, 0.15);
}

/* Search section styles */
.search-section {
    padding: 60px 0 20px 0;
    background-color: var(--bg-main);
}

.search-box-wrapper {
    position: relative;
    max-width: 600px;
    margin: 0 auto;
    padding: 0 15px;
}

.search-box-wrapper .search-icon {
    position: absolute;
    left: 35px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-muted);
    font-size: 1.2rem;
}

.search-box-wrapper input {
    width: 100%;
    padding: 16px 20px 16px 55px;
    border-radius: 40px;
    border: 1px solid var(--border-color);
    background-color: var(--bg-alternate);
    color: var(--text-main);
    font-size: 1.05rem;
    font-weight: 500;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.02);
}

.search-box-wrapper input:focus {
    outline: none;
    border-color: var(--primary);
    background-color: var(--bg-main);
    box-shadow: 0 4px 20px rgba(230, 21, 123, 0.08);
}

.category-filters-container {
    padding: 10px 0 40px 0;
    background-color: var(--bg-main);
}

.category-filters-container .product-filter-bar {
    margin-bottom: 0;
}

/* Pricing Grid & Table Styles */
.pricing-section {
    padding: 80px 0;
    background-color: var(--bg-main);
}
.pricing-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 30px;
    margin-top: 40px;
}
.pricing-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 30px;
    box-shadow: var(--shadow);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.pricing-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.06);
}
.pricing-card h3 {
    font-family: var(--font-heading);
    color: var(--text-main);
    font-size: 1.5rem;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.pricing-card h3 i {
    color: var(--primary);
}
.pricing-table-wrapper {
    overflow-x: auto;
}
.pricing-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}
.pricing-table th, .pricing-table td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
}
.pricing-table th {
    font-weight: 600;
    color: var(--text-muted);
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.pricing-table td {
    font-size: 1rem;
    color: var(--text-main);
}
.pricing-table tr:last-child td {
    border-bottom: none;
}
.price-highlight {
    font-weight: 700;
    color: var(--primary);
}
.price-note {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-top: 15px;
    font-style: italic;
}

/* Floating Theme Toggle button */
.floating-theme-toggle {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    cursor: pointer;
    z-index: 9999;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.floating-theme-toggle:hover {
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}
.floating-theme-toggle:active {
    transform: scale(0.95);
}

@media (max-width: 768px) {
    .floating-theme-toggle {
        bottom: 20px;
        right: 20px;
        width: 44px;
        height: 44px;
        font-size: 1.1rem;
    }
}

/* Dark Mode overrides */
[data-theme="dark"] {
    --ink: #FAF9F6;
    --paper: #0B0B0C;
    --mist: #161619;
    --slate: #A1A1AA;

    --bg-main: var(--paper);
    --bg-card: #121215;
    --bg-alternate: var(--mist);
    --text-main: var(--ink);
    --text-muted: var(--slate);
    --border-color: #202024;
    --shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    
    --primary: #F04B9E;
    --primary-hover: #E6157B;
    --primary-glow: rgba(240, 75, 158, 0.15);
}
[data-theme="dark"] .navbar {
    background-color: rgba(11, 11, 12, 0.97);
}

/* ── Dark Mode Hero Overrides ── */
[data-theme="dark"] .hero {
    background-image: linear-gradient(rgba(11, 11, 12, 0.88), rgba(11, 11, 12, 0.95)), url('printing-service.jpg') !important;
    background-size: cover;
    background-position: center;
}

[data-theme="dark"] .hero-title-line-1 {
    color: #ffffff !important;
}

[data-theme="dark"] .hero-title-line-2 {
    color: rgba(255, 255, 255, 0.7) !important;
}

[data-theme="dark"] .hero-tagline {
    color: rgba(255, 255, 255, 0.65) !important;
}

[data-theme="dark"] .trust-item {
    color: rgba(255, 255, 255, 0.9) !important;
}

[data-theme="dark"] .trust-item i {
    color: var(--primary) !important;
}

[data-theme="dark"] .trust-divider {
    background-color: rgba(255, 255, 255, 0.15) !important;
}

[data-theme="dark"] .btn-outline {
    color: #ffffff !important;
    border-color: rgba(255, 255, 255, 0.5) !important;
}

[data-theme="dark"] .btn-outline:hover {
    background-color: rgba(255, 255, 255, 0.1) !important;
}

/* ── Dark Mode: Page Hero sections (inner pages) ── */
[data-theme="dark"] .page-hero {
    background-color: var(--bg-alternate) !important;
}

[data-theme="dark"] .page-hero h1,
[data-theme="dark"] .page-hero p {
    color: var(--text-main) !important;
}

/* ── Dark Mode: Trust Bar ── */
[data-theme="dark"] .trust-bar {
    background-color: var(--bg-card) !important;
    border-bottom: 1px solid var(--border-color) !important;
}

/* ── Dark Mode: service cards already dark via gradient overlay, fine ── */
/* ── Dark Mode: why-us section ── */
[data-theme="dark"] .why-us {
    background-color: var(--bg-card);
}

/* ── Dark Mode: reviews section ── */
[data-theme="dark"] .reviews {
    background-color: var(--bg-alternate);
}
[data-theme="dark"] .product-image-wrapper {
    background-color: #FAF9F6;
}
[data-theme="dark"] .product-category-badge {
    background-color: rgba(20, 20, 20, 0.85) !important;
    color: rgba(255, 255, 255, 0.95) !important;
    border-color: rgba(255, 255, 255, 0.15) !important;
}
[data-theme="dark"] .dropdown-menu {
    background-color: #121215;
    border-color: #202024;
}
[data-theme="dark"] .dropdown-menu a:hover {
    background-color: #161619;
}
[data-theme="dark"] .badge {
    background-color: rgba(255, 255, 255, 0.05);
    color: #fff;
    border-color: rgba(255, 255, 255, 0.1);
}
[data-theme="dark"] .flavour-item {
    background-color: #161619 !important;
    border-color: #202024 !important;
}
[data-theme="dark"] .booking-modal-content {
    background-color: #121215 !important;
    border-color: #202024 !important;
}
[data-theme="dark"] input, 
[data-theme="dark"] select, 
[data-theme="dark"] textarea {
    background-color: #161619 !important;
    border-color: #202024 !important;
    color: #fff !important;
}
[data-theme="dark"] .filter-btn:not(.active) {
    background-color: #161619;
    border-color: #202024;
    color: #A1A1AA;
}
[data-theme="dark"] .filter-btn:not(.active):hover {
    background-color: #202024;
    color: #fff;
}
[data-theme="dark"] #catalogueSearch {
    background-color: #121215;
    border-color: #202024;
    color: #fff;
}

/* Mobile Optimization & Custom UI overrides */
.form-group input, .form-group select, .form-group textarea {
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
}

[data-theme="dark"] .form-group input,
[data-theme="dark"] .form-group select,
[data-theme="dark"] .form-group textarea {
    background-color: var(--bg-card);
    color: var(--text-main);
    border-color: var(--border-color);
}

@media (max-width: 576px) {
    .booking-form-wrapper {
        padding: 20px 16px !important;
    }
}

/* Screenshot containment removed for unlocking and power */

/* Sidebar and Two-Column Catalogue Layout */
.catalogue-layout {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 40px;
    align-items: flex-start;
}

.catalogue-sidebar {
    position: sticky;
    top: calc(var(--nav-height) + 20px);
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 24px;
    box-shadow: var(--shadow);
}

.sidebar-title {
    font-family: var(--font-heading);
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid var(--primary);
    color: var(--text-main);
}

.catalogue-sidebar .product-filter-bar {
    display: flex;
    flex-direction: column;
    gap: 8px;
    border: none;
    padding: 0;
    margin: 0;
    background: transparent;
    width: 100%;
}

.catalogue-sidebar .filter-btn {
    display: flex;
    align-items: center;
    gap: 12px;
    width: 100%;
    text-align: left;
    padding: 10px 14px;
    background-color: transparent;
    border: 1px solid transparent;
    border-radius: 6px;
    color: var(--text-muted);
    font-family: var(--font-sans);
    font-weight: 600;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.catalogue-sidebar .filter-btn i {
    width: 16px;
    font-size: 1rem;
    text-align: center;
    color: var(--text-muted);
    transition: color 0.2s ease;
}

.catalogue-sidebar .filter-btn:hover {
    background-color: var(--bg-alternate);
    color: var(--primary);
}

.catalogue-sidebar .filter-btn:hover i {
    color: var(--primary);
}

.catalogue-sidebar .filter-btn.active {
    background-color: var(--primary-glow);
    color: var(--primary);
    border-color: rgba(230, 21, 123, 0.15);
}

.catalogue-sidebar .filter-btn.active i {
    color: var(--primary);
}

/* Ensure native booking form buttons are left aligned */
.native-booking-form button[type="submit"] {
    align-self: flex-start;
    width: auto;
    min-width: 200px;
}

/* Image containment adjustments to prevent pillarboxing */
.product-image-wrapper {
    height: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background-color: var(--bg-alternate);
    border-bottom: 1px solid var(--border-color);
}

.product-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.product-card:hover .product-image {
    transform: scale(1.05);
}

/* For specific product images that should not be cropped, use contain with padded background */
.product-card[data-category="Smartphones"] .product-image,
.product-card[data-category="Tablets"] .product-image,
.product-card[data-category="Laptops"] .product-image,
.product-card[data-category="Vape Kits"] .product-image {
    object-fit: contain;
    padding: 10px;
}

/* Fix mobile responsive catalogue layout */
@media (max-width: 992px) {
    .catalogue-layout {
        grid-template-columns: 220px 1fr;
        gap: 24px;
    }
}

@media (max-width: 768px) {
    .catalogue-layout {
        display: flex;
        flex-direction: column;
        gap: 24px;
    }
    
    .catalogue-sidebar {
        position: static;
        width: 100%;
        padding: 16px;
    }
    
    .catalogue-sidebar .product-filter-bar {
        flex-direction: row;
        overflow-x: auto;
        white-space: nowrap;
        padding-bottom: 8px;
        -webkit-overflow-scrolling: touch;
    }
    
    .catalogue-sidebar .filter-btn {
        width: auto;
        display: inline-flex;
    }
    
    .native-booking-form button[type="submit"] {
        width: 100%;
    }
}

/* Inline Product Variants Styling */
.product-variant-group {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    text-align: left;
}
.variant-label {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-muted);
}
.variant-select {
    width: 100%;
    padding: 8px 10px;
    font-size: 0.85rem;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    background-color: var(--bg-alternate);
    color: var(--text-main);
    outline: none;
    cursor: pointer;
    transition: border-color 0.2s ease;
}
.variant-select:focus {
    border-color: var(--primary);
}
.color-swatches {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 2px;
}
.color-swatch {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid transparent;
    box-shadow: 0 0 0 1px var(--border-color);
    transition: all 0.2s ease;
    position: relative;
}
.color-swatch:hover {
    transform: scale(1.1);
}
.color-swatch.active {
    border-color: var(--bg-card);
    box-shadow: 0 0 0 2px var(--primary);
    transform: scale(1.1);
}
.storage-pills {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 2px;
}
.storage-pill {
    padding: 4px 10px;
    font-size: 0.75rem;
    font-weight: 600;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    cursor: pointer;
    background-color: var(--bg-alternate);
    color: var(--text-main);
    transition: all 0.2s ease;
}
.storage-pill:hover {
    background-color: var(--border-color);
}
.storage-pill.active {
    background-color: var(--primary);
    border-color: var(--primary);
    color: #ffffff;
}
.product-price-row {
    margin-top: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.product-cta-btn {
    width: 100%;
    margin-top: 12px;
    padding: 10px;
    font-size: 0.85rem;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* ── Mobile Performance Overrides ──────────────────── */
@media (max-width: 768px) {
    /* Remove box-shadow on scroll-heavy elements - causes full repaint */
    .product-card,
    .service-card,
    .why-card,
    .review-card,
    .blog-card,
    .phone-item-card,
    .phone-product-card {
        box-shadow: none;
        border: 1px solid var(--border-color);
    }

    /* Reduce hero section image complexity */
    .hero-section {
        background-attachment: scroll !important;
    }

    /* Simplify marquee on very small screens */
    .marquee-item {
        box-shadow: none;
    }
}
"""

with open(os.path.join(dest_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

print("style.css written successfully.")


def get_header(title, description, is_home=False):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Fast Access | Hounslow Printing, Vape and Tech Repairs</title>
    <meta name="description" content="{description}">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- CSS Stylesheet -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Sticky Navigation Bar -->
    <nav class="navbar">
        <div class="container nav-container">
            <a href="./" class="logo"><span class="logo-main">FAST ACCESS</span><span class="logo-sub primary-text">PRINT, VAPE AND REPAIR</span></a>
            <ul class="nav-links" id="navLinks">
                <li><a href="./">Home</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-trigger">Phone Repairs <i class="fa-solid fa-chevron-down"></i></a>
                    <ul class="dropdown-menu">
                        <li><a href="screenrepair">Screen Repair</a></li>
                        <li><a href="batteryreplacement">Battery Replacement</a></li>
                        <li><a href="chargingport">Charging Port Repair</a></li>
                        <li><a href="waterdamage">Water Damage Repair</a></li>
                        <li><a href="phoneunlocking">Phone Unlocking</a></li>
                    </ul>
                </li>
                <li class="dropdown">
                    <a href="#" class="dropdown-trigger">Laptop Repairs <i class="fa-solid fa-chevron-down"></i></a>
                    <ul class="dropdown-menu">
                        <li><a href="laptopscreen">Screen Repair</a></li>
                        <li><a href="powercharging">Power and Battery</a></li>
                        <li><a href="ramstorage">SSD and RAM Upgrades</a></li>
                        <li><a href="slowperformance">Performance Tuneups</a></li>
                        <li><a href="virusmalware">Virus and Malware Removal</a></li>
                        <li><a href="datarecovery">Data Recovery</a></li>
                        <li><a href="keyboardports">Keyboard and Ports Repair</a></li>
                        <li><a href="liquidspill">Liquid Spill Recovery</a></li>
                        <li><a href="laptoptablet">Tablet and General Repairs</a></li>
                    </ul>
                </li>
                <li><a href="passportphotos">Passport Photos</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-trigger">Print and Cafe <i class="fa-solid fa-chevron-down"></i></a>
                    <ul class="dropdown-menu">
                        <li><a href="documentprinting">Printing and Copying</a></li>
                        <li><a href="internetcafe">Internet Cafe Access</a></li>
                    </ul>
                </li>
                <li><a href="catalogue">Catalogue</a></li>
                <li><a href="blog">Blog</a></li>
                <li><a href="contact">Contact</a></li>
                <li><a href="tel:07466540111" class="btn-nav-cta"><i class="fa-solid fa-phone"></i> Call Shop</a></li>
            </ul>
            <div class="hamburger" id="hamburger">
                <i class="fa-solid fa-bars"></i>
            </div>
        </div>
    </nav>
'''


def get_footer():
    return '''    <!-- Options (Colors & Storage) Modal -->
    <div id="optionsModal" class="booking-modal" onclick="closeOptionsModal()">
        <div class="booking-modal-content" onclick="event.stopPropagation()" style="max-width: 500px; text-align: left; padding: 30px; border-radius: 8px;">
            <span class="booking-modal-close" onclick="closeOptionsModal()">&times;</span>
            <h2 id="options-modal-title" style="font-size: 1.4rem; margin-bottom: 16px; color: var(--text-main); font-family: var(--font-heading); font-weight: 700; border-bottom: 2px solid var(--primary); padding-bottom: 8px;">Available Options</h2>
            <div id="options-modal-body" style="margin-bottom: 20px;">
                <!-- Options will be inserted here -->
            </div>
            <button class="btn btn-primary" onclick="closeOptionsModal()" style="width: 100%;">Close</button>
        </div>
    </div>

    <!-- Shared Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="./" class="footer-logo"><span class="logo-main">FAST ACCESS</span><span class="logo-sub primary-text">PRINT, VAPE AND REPAIR</span></a>
                    <p>Serving Hounslow for 25 years. We provide professional printing (A4, A5) with lamination, government-compliant passport photos, high-speed internet cafe stations, and expert device repairs.</p>
                    <div style="margin-top: 15px;">
                        <span class="badge" style="background: rgba(255,255,255,0.05); color: #fff; border-color: rgba(255,255,255,0.1);"><i class="fa-solid fa-award"></i> Established 25 Years</span>
                    </div>
                </div>
                <div class="footer-links">
                    <h4>Services</h4>
                    <ul class="footer-services-list">
                        <li><a href="documentprinting">A4/A5 Print and Copy</a></li>
                        <li><a href="passportphotos">Passport Photos</a></li>
                        <li><a href="internetcafe">Internet Cyber Cafe</a></li>
                        <li><a href="screenrepair">Phone Screen Repair</a></li> 
                        <li><a href="batteryreplacement">Phone Battery</a></li> 
                        <li><a href="laptopscreen">Laptop Screen</a></li> 
                        <li><a href="slowperformance">Laptop Tuneup</a></li> 
                        <li><a href="phoneunlocking">Phone Unlocking</a></li>
                    </ul>
                </div>
                <div class="footer-hours">
                    <h4>Opening Hours</h4>
                    <ul>
                        <li>Monday - Saturday: 9:00 am &ndash; 8:00 pm</li>
                        <li>Sunday: 10:00 am &ndash; 7:00 pm</li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Speak with Us</h4>
                    <p class="phone-num"><a href="tel:07466540111">07466 540111</a></p>
                    <p style="font-size: 0.85rem; color: rgba(255,255,255,0.6); margin-bottom: 8px;">
                        <i class="fa-solid fa-envelope" style="color: var(--primary); margin-right: 6px;"></i>
                        <a href="mailto:fastinternetaccess@gmail.com" style="color: rgba(255,255,255,0.6); text-decoration: none;">fastinternetaccess@gmail.com</a>
                    </p>
                    <p class="address-num">80 High St, Hounslow, TW3 1NH</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; Fast Access 2026. All rights reserved. Serving the High Street since 2001.</p>
            </div>
        </div>
    </footer>

    <!-- Lightbox Modal -->
    <div id="lightbox" class="lightbox" onclick="closeLightbox()">
        <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
        <img id="lightbox-img" class="lightbox-content" src="" alt="Enlarged gallery view">
        <div id="lightbox-caption" class="lightbox-caption"></div>
    </div>

    <!-- Flavours Modal -->
    <div id="flavoursModal" class="booking-modal" onclick="closeFlavoursModal()">
        <div class="booking-modal-content" onclick="event.stopPropagation()" style="max-width: 500px; text-align: left; padding: 30px; border-radius: 8px;">
            <span class="booking-modal-close" onclick="closeFlavoursModal()">&times;</span>
            <h2 id="flavours-modal-title" style="font-size: 1.4rem; margin-bottom: 16px; color: var(--text-main); font-family: var(--font-heading); font-weight: 700; border-bottom: 2px solid var(--primary); padding-bottom: 8px;">Available Flavours</h2>
            <div id="flavours-modal-list" style="max-height: 300px; overflow-y: auto; display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 20px; padding: 5px;">
                <!-- Flavours will be inserted here -->
            </div>
            <button class="btn btn-primary" onclick="closeFlavoursModal()" style="width: 100%;">Close</button>
        </div>
    </div>

    <!-- Booking Confirmation Modal -->
    <div id="bookingModal" class="booking-modal" onclick="closeBookingModal()">
        <div class="booking-modal-content" onclick="event.stopPropagation()">
            <span class="booking-modal-close" onclick="closeBookingModal()">&times;</span>
            <div class="modal-success-icon"><i class="fa-solid fa-circle-check"></i></div>
            <h2>Enquiry Received!</h2>
            <p>Thank you for reaching out to Fast Access. We have received your enquiry details and will call you shortly on your provided phone number to confirm details.</p>
            <button class="btn btn-primary" onclick="closeBookingModal()">Got it, thanks!</button>
        </div>
    </div>

    <!-- Core JavaScript -->
    <script>
        // Hamburger toggle
        
        // Premium Dark/Light Mode Theme Toggle
        (function() {
            const toggleBtn = document.createElement('button');
            toggleBtn.id = 'theme-toggle-btn';
            toggleBtn.className = 'floating-theme-toggle';
            toggleBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';
            toggleBtn.title = 'Toggle Light/Dark Theme';
            document.body.appendChild(toggleBtn);

            const savedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
            document.documentElement.setAttribute('data-theme', savedTheme);
            updateToggleIcon(savedTheme);

            toggleBtn.addEventListener('click', () => {
                const currentTheme = document.documentElement.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
                updateToggleIcon(newTheme);
                
                toggleBtn.style.transform = 'scale(0.8)';
                setTimeout(() => toggleBtn.style.transform = 'scale(1)', 150);
            });

            function updateToggleIcon(theme) {
                const icon = toggleBtn.querySelector('i');
                if (theme === 'dark') {
                    icon.className = 'fa-solid fa-sun';
                    toggleBtn.style.backgroundColor = '#FAF9F6';
                    toggleBtn.style.color = '#1C1C1E';
                } else {
                    icon.className = 'fa-solid fa-moon';
                    toggleBtn.style.backgroundColor = '#1C1C1E';
                    toggleBtn.style.color = '#FAF9F6';
                }
            }
        })();

        const hamburger = document.getElementById('hamburger');
        const navLinks = document.getElementById('navLinks');
        
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.querySelector('i').classList.toggle('fa-bars');
            hamburger.querySelector('i').classList.toggle('fa-xmark');
        });

        // Close menu immediately when clicking any link inside it
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', (e) => {
                if (link.classList.contains('dropdown-trigger')) return;
                navLinks.classList.remove('active');
                const icon = hamburger.querySelector('i');
                if (icon) {
                    icon.className = 'fa-solid fa-bars';
                }
            });
        });

        // Inline selection and Enquire link updater for Product Catalogue
        function selectColor(el) {
            const parent = el.parentNode;
            parent.querySelectorAll('.color-swatch').forEach(sw => sw.classList.remove('active'));
            el.classList.add('active');
            updateCardEnquiryLink(el.closest('.product-card'));
        }

        function selectStorage(el) {
            const parent = el.parentNode;
            parent.querySelectorAll('.storage-pill').forEach(pill => pill.classList.remove('active'));
            el.classList.add('active');
            updateCardEnquiryLink(el.closest('.product-card'));
        }

        function updateCardEnquiryLink(card) {
            const btn = card.querySelector('.enquire-btn');
            if (!btn) return;
            
            const productName = btn.getAttribute('data-product');
            const flavourSelect = card.querySelector('.flavour-select');
            const activeColor = card.querySelector('.color-swatch.active');
            const activeStorage = card.querySelector('.storage-pill.active');
            
            let queryParams = new URLSearchParams();
            queryParams.append('product', productName);
            
            if (flavourSelect && flavourSelect.value) {
                queryParams.append('flavor', flavourSelect.value);
            }
            if (activeColor) {
                queryParams.append('color', activeColor.getAttribute('data-color'));
            }
            if (activeStorage) {
                queryParams.append('storage', activeStorage.getAttribute('data-storage'));
            }
            
            btn.href = 'contact.html?' + queryParams.toString();
        }

        // Initialize selectors and handle form pre-filling on contact / index pages
        document.addEventListener('DOMContentLoaded', () => {
            // Set up flavor select event listener
            document.querySelectorAll('.flavour-select').forEach(select => {
                select.addEventListener('change', (e) => {
                    updateCardEnquiryLink(e.target.closest('.product-card'));
                });
            });
            
            // Auto-select first color/storage and compute initially
            document.querySelectorAll('.product-card').forEach(card => {
                const btn = card.querySelector('.enquire-btn');
                if (!btn) return; // Skip cards without enquiry button (e.g. catalogue grid cards)
                
                const firstColor = card.querySelector('.color-swatch');
                if (firstColor) firstColor.classList.add('active');
                
                const firstStorage = card.querySelector('.storage-pill');
                if (firstStorage) firstStorage.classList.add('active');
                
                updateCardEnquiryLink(card);
            });

            // Parse URL parameters and pre-fill form fields
            const params = new URLSearchParams(window.location.search);
            const product = params.get('product');
            const flavor = params.get('flavor');
            const color = params.get('color');
            const storage = params.get('storage');
            
            if (product) {
                let detailsText = `Enquiry about: ${product}`;
                let parts = [];
                if (flavor) parts.push(`Flavor: ${flavor}`);
                if (color) parts.push(`Color: ${color}`);
                if (storage) parts.push(`Storage: ${storage}`);
                if (parts.length > 0) {
                    detailsText += ` (${parts.join(', ')})`;
                }
                
                // Form details textarea fields
                const contactDetails = document.getElementById('contactDetails');
                if (contactDetails) contactDetails.value = detailsText;
                
                const issueDetails = document.getElementById('issueDetails');
                if (issueDetails) issueDetails.value = detailsText;
                
                // Form product/service select fields
                const contactService = document.getElementById('contactService');
                if (contactService) {
                    if (product.toLowerCase().includes('iphone') || product.toLowerCase().includes('samsung') || product.toLowerCase().includes('galaxy') || product.toLowerCase().includes('honor')) {
                        contactService.value = 'phones';
                    } else if (product.toLowerCase().includes('pouch') || product.toLowerCase().includes('vape') || product.toLowerCase().includes('elux') || product.toLowerCase().includes('juice') || product.toLowerCase().includes('salt') || product.toLowerCase().includes('mary') || product.toLowerCase().includes('pro max')) {
                        contactService.value = 'vapes';
                    } else {
                        contactService.value = 'phones';
                    }
                }
                
                const serviceType = document.getElementById('serviceType');
                if (serviceType) {
                    if (product.toLowerCase().includes('iphone') || product.toLowerCase().includes('samsung') || product.toLowerCase().includes('galaxy') || product.toLowerCase().includes('honor')) {
                        serviceType.value = 'phones';
                    } else if (product.toLowerCase().includes('pouch') || product.toLowerCase().includes('vape') || product.toLowerCase().includes('elux') || product.toLowerCase().includes('juice') || product.toLowerCase().includes('salt') || product.toLowerCase().includes('mary') || product.toLowerCase().includes('pro max')) {
                        serviceType.value = 'vapes';
                    } else {
                        serviceType.value = 'consultation';
                    }
                }
                
                // Form device model text input fields
                const deviceModel = document.getElementById('deviceModel');
                if (deviceModel) deviceModel.value = product;
            }
        });

        // Mobile dropdown toggle
        document.querySelectorAll('.dropdown-trigger').forEach(trigger => {
            trigger.addEventListener('click', (e) => {
                if (window.innerWidth <= 1250) {
                    e.preventDefault();
                    const menu = trigger.nextElementSibling;
                    menu.classList.toggle('active');
                }
            });
        });

        // Intersection Observer Scroll Animations with Fallbacks
        const revealElements = document.querySelectorAll('.reveal');
        
        const checkReveal = () => {
            revealElements.forEach(el => {
                const rect = el.getBoundingClientRect();
                if (rect.top < window.innerHeight * 0.95 && rect.bottom > 0) {
                    el.classList.add('active');
                }
            });
        };

        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries, obs) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        obs.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.02 });
            revealElements.forEach(el => observer.observe(el));
            
            window.addEventListener('load', checkReveal);
            document.addEventListener('DOMContentLoaded', checkReveal);
        } else {
            revealElements.forEach(el => el.classList.add('active'));
        }

        // Failsafe: force reveal all elements after a short timeout so pages never hang
        setTimeout(() => {
            revealElements.forEach(el => el.classList.add('active'));
        }, 400);

        // Lightbox functionality
        function openLightbox(src, caption) {
            const lightbox = document.getElementById('lightbox');
            const img = document.getElementById('lightbox-img');
            const cap = document.getElementById('lightbox-caption');
            
            img.src = src;
            cap.innerHTML = caption;
            lightbox.classList.add('active');
            
            document.body.style.overflow = 'hidden';
        }

        // Handle escape key for lightbox
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeLightbox();
                closeBookingModal();
            }
        });

        function closeLightbox() {
            const lightbox = document.getElementById('lightbox');
            lightbox.classList.remove('active');
            document.body.style.overflow = '';
        }

        // Flavours Modal Functions
        function openFlavoursModal(productName, flavoursList) {
            const modal = document.getElementById('flavoursModal');
            const title = document.getElementById('flavours-modal-title');
            const list = document.getElementById('flavours-modal-list');
            
            title.textContent = productName + " Flavours";
            list.innerHTML = "";
            
            flavoursList.forEach(flavour => {
                const item = document.createElement('div');
                item.className = 'flavour-item';
                item.style.padding = '10px 14px';
                item.style.backgroundColor = 'var(--bg-alternate)';
                item.style.borderRadius = '6px';
                item.style.fontSize = '0.85rem';
                item.style.border = '1px solid var(--border-color)';
                item.style.fontWeight = '600';
                item.style.color = 'var(--text-main)';
                item.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.02)';
                item.textContent = flavour;
                list.appendChild(item);
            });
            
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeFlavoursModal() {
            const modal = document.getElementById('flavoursModal');
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }

        // Options Modal Functions
        function openOptionsModal(productName, colorsList, storagesList) {
            const modal = document.getElementById('optionsModal');
            const title = document.getElementById('options-modal-title');
            const body = document.getElementById('options-modal-body');
            
            title.textContent = productName + " Options";
            body.innerHTML = "";
            
            const colorHex = {
                "Natural": "#BEB2A2",
                "Black": "#1C1C1E",
                "White": "#F5F5F7",
                "Natural/Grey": "#8E8E93",
                "Red": "#E31837",
                "Light Pink/Purple": "#E8D8F8",
                "Pink": "#FFC0CB",
                "Gold": "#F4D068",
                "Phantom Black": "#1A1A1A",
                "Awesome Violet / Light Purple": "#E2D3F5",
                "Awesome White": "#FAF9F6",
                "Aurora / Breathing Crystal (Light Blue/Silver Gradient)": "linear-gradient(135deg, #E0F2FE 0%, #E2E8F0 50%, #C084FC 100%)",
                "Awesome Black": "#1E1E1F",
                "Purple": "#4E365E",
                "Dark Titanium/Black": "#2E3033",
                "Graphite/Black": "#3E3E40",
                "White/Silver": "#F0F0F2",
                "Awesome Black": "#1E1E1F"
            };

            if (storagesList && storagesList.length > 0) {
                const storageTitle = document.createElement('h3');
                storageTitle.style.fontSize = '1.05rem';
                storageTitle.style.margin = '15px 0 10px 0';
                storageTitle.style.color = 'var(--text-main)';
                storageTitle.style.fontWeight = '700';
                storageTitle.textContent = "Available Storage Variations:";
                body.appendChild(storageTitle);
                
                const storageContainer = document.createElement('div');
                storageContainer.style.display = 'flex';
                storageContainer.style.gap = '8px';
                storageContainer.style.flexWrap = 'wrap';
                storageContainer.style.marginBottom = '20px';
                
                storagesList.forEach(s => {
                    const badge = document.createElement('span');
                    badge.className = 'storage-badge';
                    badge.style.backgroundColor = 'var(--bg-alternate)';
                    badge.style.border = '1px solid var(--border-color)';
                    badge.style.padding = '4px 12px';
                    badge.style.borderRadius = '4px';
                    badge.style.fontWeight = '600';
                    badge.style.fontSize = '0.85rem';
                    badge.textContent = s;
                    storageContainer.appendChild(badge);
                });
                body.appendChild(storageContainer);
            }
            
            if (colorsList && colorsList.length > 0) {
                const colorTitle = document.createElement('h3');
                colorTitle.style.fontSize = '1.05rem';
                colorTitle.style.margin = '15px 0 10px 0';
                colorTitle.style.color = 'var(--text-main)';
                colorTitle.style.fontWeight = '700';
                colorTitle.textContent = "Available Colors:";
                body.appendChild(colorTitle);
                
                const colorContainer = document.createElement('div');
                colorContainer.style.display = 'flex';
                colorContainer.style.alignItems = 'center';
                colorContainer.style.gap = '12px';
                colorContainer.style.flexWrap = 'wrap';
                
                colorsList.forEach(c => {
                    const swatchWrapper = document.createElement('div');
                    swatchWrapper.style.display = 'flex';
                    swatchWrapper.style.alignItems = 'center';
                    swatchWrapper.style.gap = '8px';
                    swatchWrapper.style.padding = '6px 12px';
                    swatchWrapper.style.backgroundColor = 'var(--bg-alternate)';
                    swatchWrapper.style.border = '1px solid var(--border-color)';
                    swatchWrapper.style.borderRadius = '20px';
                    
                    const swatch = document.createElement('span');
                    const hexVal = colorHex[c] || "#cccccc";
                    swatch.style.background = hexVal;
                    swatch.style.width = '14px';
                    swatch.style.height = '14px';
                    swatch.style.borderRadius = '50%';
                    swatch.style.display = 'inline-block';
                    swatch.style.border = '1px solid rgba(0,0,0,0.15)';
                    
                    const label = document.createElement('span');
                    label.style.fontSize = '0.85rem';
                    label.style.fontWeight = '600';
                    label.style.color = 'var(--text-main)';
                    label.textContent = c;
                    
                    swatchWrapper.appendChild(swatch);
                    swatchWrapper.appendChild(label);
                    colorContainer.appendChild(swatchWrapper);
                });
                body.appendChild(colorContainer);
            }
            
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeOptionsModal() {
            const modal = document.getElementById('optionsModal');
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }

        // Native Booking Form Submission Handler
        function handleBookingSubmit(event) {
            event.preventDefault();
            const modal = document.getElementById('bookingModal');
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
            event.target.reset();
            return false;
        }

        function closeBookingModal() {
            const modal = document.getElementById('bookingModal');
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }

        // Testimonial Review Slider
        let currentSlideIndex = 0;
        const slides = document.querySelectorAll('.review-slide');
        const dots = document.querySelectorAll('.dot');
        
        function showSlide(index) {
            if (slides.length === 0) return;
            slides.forEach(slide => slide.classList.remove('active'));
            dots.forEach(dot => dot.classList.remove('active'));
            
            currentSlideIndex = (index + slides.length) % slides.length;
            slides[currentSlideIndex].classList.add('active');
            if (dots[currentSlideIndex]) {
                dots[currentSlideIndex].classList.add('active');
            }
        }
        
        function currentSlide(index) {
            showSlide(index);
        }
        
        if (slides.length > 0) {
            let slideInterval = setInterval(() => {
                showSlide(currentSlideIndex + 1);
            }, 5000);
            
            document.querySelectorAll('.dot').forEach(dot => {
                dot.addEventListener('click', () => {
                    clearInterval(slideInterval);
                    slideInterval = setInterval(() => {
                        showSlide(currentSlideIndex + 1);
                    }, 5000);
                });
            });
        }

        // Product Showcase Filter Function (legacy/fallback)
        function filterShowcase(category) {
            const buttons = document.querySelectorAll('.filter-btn');
            buttons.forEach(btn => {
                if (btn.textContent.trim() === category || (category === 'All' && btn.textContent.trim() === 'All Products')) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });

            const cards = document.querySelectorAll('.product-card');
            cards.forEach(card => {
                const cardCat = card.getAttribute('data-category');
                if (category === 'All' || cardCat === category) {
                    card.style.display = 'flex';
                    setTimeout(() => {
                        card.classList.add('active');
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    card.style.display = 'none';
                }
            });
        }

        // Hash-based category filtering on page load or hash change
        function handleHashFilter() {
            const hash = window.location.hash;
            if (hash && hash.startsWith('#category-')) {
                const category = decodeURIComponent(hash.replace('#category-', '')).replace(/-/g, ' ');
                filterShowcase(category);
                
                const target = document.getElementById('products-showcase');
                if (target) {
                    setTimeout(() => {
                        target.scrollIntoView({ behavior: 'smooth' });
                    }, 150);
                }
            }
        }

        window.addEventListener('DOMContentLoaded', handleHashFilter);
        window.addEventListener('hashchange', handleHashFilter);
    </script>
</body>
</html>'''

def build_service_page(filename, service_name, one_liner, body_copy, symptoms, images, is_laptop=False, hero_image=None):
    hero_bg = hero_image if hero_image else images[0]
    
    if "virus" in filename or "virus" in service_name.lower():
        overlay = "linear-gradient(rgba(17, 17, 17, 0.25), rgba(17, 17, 17, 0.45))"
    else:
        overlay = "linear-gradient(rgba(17, 17, 17, 0.35), rgba(17, 17, 17, 0.55))"
    
    symptoms_html = ""
    for s in symptoms:
        symptoms_html += f"<li><i class='fa-solid fa-circle-exclamation'></i> {s}</li>"
        
    gallery_html = ""
    if "unlocking" in filename:
        steps = ["Before Unlocking", "Unlocking In Progress", "Unblocked Device"]
    else:
        steps = ["Before Repair", "Repair In Progress", "Repaired Device"]
    for img, step in zip(images, steps):
        gallery_html += f'''
                <div class="gallery-item-wrapper" onclick="openLightbox('{img}', '{step} - {service_name}')">
                    <img src="{img}" alt="{step}">
                    <span>{step}</span>
                </div>'''

    html_content = get_header(service_name, one_liner) + f'''
    <!-- Service Hero -->
    <section class="service-hero" style="background-image: {overlay}, url('{hero_bg}');">
        <div class="container text-center reveal">
            <h1>{service_name}</h1>
            <p>{one_liner}</p>
            <a href="tel:07466540111" class="btn btn-primary"><i class="fa-solid fa-phone"></i> Call Fast Access</a>
        </div>
    </section>

    <!-- What's Involved -->
    <section class="service-details">
        <div class="container details-grid">
            <div class="details-text reveal">
                <h2>What's Involved</h2>
                <p>{body_copy}</p>
                
                <div class="symptoms-box">
                    <h3>Signs You Need This Service</h3>
                    <ul class="symptoms-list">
                        {symptoms_html}
                    </ul>
                </div>
            </div>
            <div class="details-image reveal">
                <img src="{images[1]}" alt="Repair service process" class="in-process-img">
            </div>
        </div>
    </section>

    <!-- Gallery Row -->
    <section class="service-gallery">
        <div class="container">
            <div class="section-header text-center reveal">
                <h2>Our Process and Results</h2>
                <div class="accent-divider"></div>
            </div>
            <div class="gallery-row reveal">
                {gallery_html}
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="service-cta text-center reveal">
        <div class="container">
            <h2>Get a Free Diagnostic Assessment</h2>
            <p>Speak to our technicians directly to describe the issue and schedule your repair today.</p>
            <a href="tel:07466540111" class="btn btn-primary"><i class="fa-solid fa-phone"></i> Call Fast Access</a>
        </div>
    </section>

    <!-- Related Services -->
    <section class="related-services">
        <div class="container">
            <div class="section-header text-center reveal">
                <h2>Other Repair Services</h2>
                <div class="accent-divider"></div>
            </div>
            <div class="related-grid reveal">
                <div class="related-card">
                    <h3>Screen Repair</h3>
                    <p>Smashed displays, bleeding LCDs, and unresponsive touch screens replaced.</p>
                    <a href="{"laptopscreen" if is_laptop else "screenrepair"}" class="learn-more">Learn More &rarr;</a>
                </div>
                <div class="related-card">
                    <h3>Battery and Charging</h3>
                    <p>Swapping depleted cells and repairing charging ports.</p>
                    <a href="{"powercharging" if is_laptop else "batteryreplacement"}" class="learn-more">Learn More &rarr;</a>
                </div>
                <div class="related-card">
                    <h3>Liquid Spill Recovery</h3>
                    <p>Logic board diagnostic and chemical corrosion cleaning.</p>
                    <a href="{"liquidspill" if is_laptop else "waterdamage"}" class="learn-more">Learn More &rarr;</a>
                </div>
            </div>
        </div>
    </section>
''' + get_footer()

    with open(os.path.join(dest_dir, filename), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Service page {filename} written.")

# ----------------- Write index.html -----------------
PRODUCTS = [
    {
        'category': 'Gaming',
        'title': 'PlayStation 4 500GB Slim',
        'specs': '500GB, Disk Edition, Includes 1x Wireless Controller',
        'price': '£129.00',
        'image_file': '1000048114.png',
    },
    {
        'category': 'Laptops',
        'title': 'Dell Inspiron 15 Laptop',
        'specs': 'Intel Core Processor, 1TB HDD, Windows 10 Home',
        'price': '£149.00',
        'image_file': '1000048109.png',
    },
    {
        'category': 'Laptops',
        'title': 'Dell Latitude 7280',
        'specs': 'Intel Core, 8GB RAM, 256GB SSD, MS Office Included',
        'price': '£199.00',
        'image_file': '1000048106.png',
    },
    {
        'category': 'Laptops',
        'title': 'Toshiba Satellite Laptop',
        'specs': '4GB RAM,  450GB SSD,  MS Office Package Installed',
        'price': '£149.00',
        'image_file': '1000048106_2.png',
    },
    {
        'category': 'Laptops',
        'title': 'Dell Latitude E5470',
        'specs': '8GB RAM,  256GB SSD,  Windows 10 Pro Architecture',
        'price': '£219.00',
        'image_file': '1000048106_3.png',
    },
    {
        'category': 'Laptops',
        'title': 'Dell Inspiron i5',
        'specs': 'Intel i5-1035G1, 8GB RAM, 1TB HDD + 256GB SSD, Win 10',
        'price': '£269.00',
        'image_file': '1000048108.png',
    },
    {
        'category': 'Laptops',
        'title': 'Dell Latitude 7490',
        'specs': '16GB RAM,  256GB SSD,  Windows 10 Pro Business Setup',
        'price': '£220.00',
        'image_file': '1000048108_2.png',
    },
    {
        'category': 'Laptops',
        'title': 'Acer Chromebook 14',
        'specs': '14 Inch HD Anti-Glare Display, Entry-level Cloud OS',
        'price': '£109.00',
        'image_file': '1000048108_3.png',
    },
    {
        'category': 'Laptops',
        'title': 'Acer Aspire ES1',
        'specs': 'Intel Pentium R, 8GB RAM, 2TB HDD, Win 10, MS Office',
        'price': '£159.00',
        'image_file': '1000048108_4.png',
    },
    {
        'category': 'Laptops',
        'title': 'HP Victus Gaming Laptop',
        'specs': '8GB RAM, 500GB SSD, NVIDIA GTX 3050Ti Performance Graphics',
        'price': '£495.00',
        'image_file': '1000048107.png',
    },
    {
        'category': 'Gaming',
        'title': 'Nintendo Switch + Split Pad Pro Bundle',
        'specs': 'Handheld Ergonomic Console Layout, Includes 3 Games Bundle',
        'price': '£249.00',
        'image_file': '1000048107_2.png',
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 11',
        'specs': '64GB / 128GB Available, Factory Unlocked iOS Smartphone',
        'price': 'In stock',
        'image_file': 'iphone_11.png',
        'storages': ['64 GB', '128 GB'],
        'colors': ['Black'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 12',
        'specs': '64GB / 256GB Settings, Dual Super Retina XDR Display 5G',
        'price': 'In stock',
        'image_file': 'iphone_12.png',
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 15 Pro Max',
        'specs': '256GB Premium Storage, Titanium Frame, Flagship Camera Setup',
        'price': 'In stock',
        'image_file': 'iphone_15_promax.png',
        'storages': ['256 GB'],
        'colors': ['White', 'Natural/Grey', 'Black'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 16 Pro Max',
        'specs': '256GB Storage Tier,  Latest Generation Apple Flagship Device',
        'price': 'In stock',
        'image_file': 'iphone_16_promax.png',
        'storages': ['256 GB'],
        'colors': ['Natural', 'Black'],
    },
    {
        'category': 'Smartphones',
        'title': 'Samsung Galaxy S22 Ultra',
        'specs': '256GB / 512GB Options, Pro-Grade Quad Camera with Built-in S-Pen',
        'price': 'In stock',
        'image_file': 'galaxy_s22_ultra.png',
        'storages': ['256 GB', '512 GB'],
        'colors': ['Phantom Black'],
    },
    {
        'category': 'Smartphones',
        'title': 'Samsung Galaxy A54 5G',
        'specs': '128GB System,  High-Refresh AMOLED Display Unlocked Android',
        'price': 'In stock',
        'image_file': 'galaxy_a54.png',
        'storages': ['128 GB'],
        'colors': ['Awesome Violet / Light Purple'],
    },
    {
        'category': 'Smartphones',
        'title': 'Samsung Galaxy A17 5G',
        'specs': 'Reliable Long-Life Battery, Unlocked Everyday Android Device',
        'price': 'In stock',
        'image_file': 'galaxy_a17.png',
    },
    {
        'category': 'Smartphones',
        'title': 'Samsung Galaxy A36 5G',
        'specs': 'High-Efficiency Core Setup,  Modern Infinity Display Framework',
        'price': 'In stock',
        'image_file': 'galaxy_a36.png',
    },
    {
        'category': 'Tablets',
        'title': 'Apple iPad Air (4th Gen)',
        'specs': '64GB Capacity, Liquid Retina All-Screen Display, Wi-Fi Built-in',
        'price': 'In stock',
        'image_file': 'ipad_air_4.png',
    },
    {
        'category': 'Smartphones',
        'title': 'Zanco Big Button Mobile Phone',
        'specs': 'Senior-Friendly Interface, Explicit Hardware SOS Trigger, Integrated Torch',
        'price': 'In stock',
        'image_file': 'zanco_big_button.png',
    },
    {
        'category': 'Vape Kits',
        'title': 'Hayati Pro Ultra+ 25K (Starter Kit)',
        'specs': '25,000+ Puffs Capacity, 20mg Nic Salt, Dual Tank Swappable System',
        'price': 'In stock',
        'image_file': 'hayati_pro_25k.png',
        'flavours': ['Strawberry Cherry / Raspberry Ice', 'Sour Apple / Juicy Peach', 'Blue Razz Pineapple / Strawberry Ice', 'Raspberry Cola', "Blueberry N' Bubba / Watermelon N' Bubba", 'Lemon & Lime / Summer Dream'],
    },
    {
        'category': 'Vape Kits',
        'title': 'Crown Bar Al Fakher 30K Hypermax Advanced',
        'specs': '30, 000 Puffs Massive Output DTL Sub-Ohm Disposable Mod Line',
        'price': 'In stock',
        'image_file': 'alfakher_30k.png',
        'flavours': ['Blueberry Sour Raspberry', 'Blueberry Gum', 'Grape', 'Blackcurrant Mint', 'Peach Ice', 'Cherry Ice', 'Strawberry Punch', 'Menthol', 'Two Apple', 'Cool Mango', 'Berry Blue', 'Blueberry Lemonade', 'Hubba'],
    },
    {
        'category': 'Vape Kits',
        'title': 'Vaporesso Dojo Blast 10K Starter Kit',
        'specs': '10, 000 Puffs Rechargeable Reusable Base Hardware Unit',
        'price': 'In stock',
        'image_file': 'dojo_blast_kit.png',
        'flavours': ['Strawberry Raspberry Cherry Ice', 'Triple Mango', 'Black Grape', 'Lemon Lime', 'Double Apple', 'Classic Tobacco', 'Ten Tangerines', 'Fizzy Cherry', 'Watermelon Ice', 'Sweet Peach', 'Pineapple Ice', 'Blueberry', 'Blue Razz Lemonade', 'Bubba', 'Lychee Ice', 'Sour Berry', 'Kiwi Passion Fruit Guava', 'Sour Peach Gummy', 'Banana Ice'],
    },
    {
        'category': 'Vape Refills',
        'title': 'Vaporesso Dojo Blast 10K Replacement Pods',
        'specs': 'Replacement Prefilled Mesh Coil Big Puff Pod Cartridges',
        'price': 'In stock',
        'image_file': 'dojo_blast_pods.png',
        'flavours': ['Strawberry Raspberry Cherry Ice', 'Triple Mango', 'Black Grape', 'Lemon Lime', 'Double Apple', 'Classic Tobacco', 'Ten Tangerines', 'Fizzy Cherry', 'Watermelon Ice', 'Sweet Peach', 'Pineapple Ice', 'Blueberry', 'Blue Razz Lemonade', 'Bubba', 'Lychee Ice', 'Sour Berry', 'Kiwi Passion Fruit Guava', 'Sour Peach Gummy', 'Banana Ice'],
    },
    {
        'category': 'Vape Kits',
        'title': 'IVG Pro 10K Starter Kit',
        'specs': '10, 000 Puffs High-Volume Intelligent Smart Battery Station',
        'price': 'In stock',
        'image_file': 'ivg_pro_10k_kit.png',
        'flavours': ['Strawberry Ice', 'Kiwi Passionfruit Guava', 'Sour Cherry Watermelon', 'Tobacco', 'Blue Raspberry Ice', 'Blueberry Mint', 'Pineapple Ice', 'Strawberry Raspberry Cherry', 'Fresh Menthol Mojito', 'Pink Lemonade', 'Blue Razz Lemonade'],
    },
    {
        'category': 'Vape Refills',
        'title': 'IVG Pro Pod 10K Replacement Pods',
        'specs': 'Click-in Replacement Big Puff Empty-to-Full Flavor Modules',
        'price': 'In stock',
        'image_file': 'IVG Pro Pod 10K (Replacement Pods).webp',
        'flavours': ['Blueberry Raspberry', 'Cola Cherry', 'Pink Lemonade', 'Blue Razz Lemonade', 'Sour Cherry Watermelon'],
    },
    {
        'category': 'Vape Kits',
        'title': 'Lost Mary 30K',
        'specs': '30,000 Puffs Smart Screen Indicator, Dual-Mesh Adjustable Wattage',
        'price': 'In stock',
        'image_file': 'Lost mary 30k.jpg',
        'flavours': ['Cola', 'Blackberry Raspberry', 'Watermelon Ice', 'Strawberry Blueberry Cherry', 'Pineapple Ice', 'Strawberry Kiwi', 'Triple Mango', 'Blueberry Ice'],
    },
    {
        'category': 'Vape Refills',
        'title': 'Lost Mary ECO 15K/6K Pod System',
        'specs': 'Eco-conscious Modular Replacement Prefilled Cartridge Cartridges',
        'price': 'In stock',
        'image_file': 'lost_mary_pods.png',
        'flavours': ['Watermelon Ice', 'Blueberry Sour Raspberry', 'Blue Razz Lemonade', 'Strawberry Ice', 'Double Apple', 'Cherry Ice'],
    },
    {
        'category': 'E-Liquids',
        'title': 'Elux Legend Nic Salts 10ml',
        'specs': '10mg / 20mg Concentrations, Small-Pod Optimized Fluid Nicotine',
        'price': 'In stock',
        'image_file': 'elux_salts_10ml.png',
        'flavours': ['Blueberry Sour Raspberry', 'Mr Blue', 'Fizzy Cherry', 'Lemon & Lime', 'Strawberry Watermelon Bubblegum', 'Gummy Bear', 'Watermelon Ice'],
    },
    {
        'category': 'E-Liquids',
        'title': 'Bar Juice 5000 (10ml Nic Salts)',
        'specs': 'Disposable-Style Concentrated Taste Refill Liquid Profiles',
        'price': '£2.99',
        'image_file': 'bar_juice_10ml.png',
        'flavours': ['Strawberry Sour Raspberry', 'Orange Zest', 'Pink Bubba', 'Blue Bubba', 'Blueberry Watermelon', 'Strawberry Ice', 'Sour Rainbow', 'Double Apple Shisha', 'Pear Banana', 'Blue Razz Lemonade', 'Pink Lemonade', 'Lemon & Lime', 'Watermelon', 'Strawberry Kiwi', 'Red Apple Ice', 'Blueberry Pomegranate', 'Berry Crush', 'Fizzy Cherry', 'Cherry Ice', 'Blue Ice', 'Strawberry Watermelon', 'Peach', 'Triple Mango', 'Blackberry Raspberry', 'Blueberry'],
    },
    {
        'category': 'E-Liquids',
        'title': 'Tasty CBD 100ml Shortfill E-Liquid',
        'specs': '1000mg-3500mg Range,  Thick High-VG Cloud Tank Wellness Blend',
        'price': 'In stock',
        'image_file': 'tasty_cbd_100ml.png',
        'flavours': ['Cherry Drop', 'Mango Ice', 'Bubblegum', 'Chilled Berry', 'Sour Apple'],
    },
    {
        'category': 'Nicotine Pouches',
        'title': 'Nordic Spirit Nicotine Pouches',
        'specs': 'Premium Spit-Free Nicotine Pouches (All Strengths)',
        'price': 'In stock',
        'image_file': 'nordic spirit.jpg',
        'flavours': ['Spearmint', 'Sweet Mint', 'Wild Berry / Elderflower'],
    },
    {
        'category': 'Nicotine Pouches',
        'title': 'ZYN Nicotine Pouches',
        'specs': 'Premium Spit-Free Nicotine Pouches (All Strengths)',
        'price': 'In stock',
        'image_file': 'ZYN Pouches Reuse.webp',
        'flavours': ['ZYN Espressino', 'Cool Mint', 'Citrus'],
    },
    {
        'category': 'Nicotine Pouches',
        'title': 'Velo Nicotine Pouches',
        'specs': 'Premium Spit-Free Nicotine Pouches (All Strengths)',
        'price': 'In stock',
        'image_file': 'velo nicotine pouches.webp',
        'flavours': ['Freezing Peppermint / Peppermint Storm', 'Crispy Peppermint', 'Bright Spearmint', 'Spicy Papaya', 'Mango Flame', 'Ruby Berry / Blush Berry'],
    },
    {
        'category': 'Tech Accessories',
        'title': 'Maxmate MMH15 Wireless Headphones',
        'specs': 'Over-Ear Cushioned Bluetooth Unit, Built-in Microphone, 6D Audio',
        'price': 'In stock',
        'image_file': 'maxmate_headphones.png',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Koleer H68 Bluetooth Speaker',
        'specs': 'Rugged Exterior Portable High-Volume Shock-Absorbing Speaker',
        'price': 'In stock',
        'image_file': 'koleer_h68.png',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Zagg Slim Wired Desktop Keyboard',
        'specs': 'Universal Typing Interface, Low-Profile keys, USB-C/USB-A Native',
        'price': 'In stock',
        'image_file': 'zagg_keyboard.png',
    },
    {
        'category': 'Protection & Cases',
        'title': 'Mutural iPad Smart Folio Stand Case',
        'specs': 'Tri-Fold Magnetic Shell, Auto Wake/Sleep Feature, Multi-Angle Fit',
        'price': 'Flat £15.00',
        'image_file': 'mutural_ipad_case.png',
    },
    {
        'category': 'Tech Accessories',
        'title': 'SanDisk Ultra Dual Drive USB-C Flash',
        'specs': 'High-Speed Flash Drive to Transfer Data Between Phones & PCs',
        'price': 'In stock',
        'image_file': 'sandisk_dual_drive.png',
    },
    {
        'category': 'Protection & Cases',
        'title': 'Maxx Clear Anti-Shock Smartphone Case',
        'specs': 'Impact-Resistant Hard TPU Protective Backcovers (iOS & Android)',
        'price': 'Flat £10.00',
        'image_file': 'clear_antishock_case.png',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Budi Super Fast PD Charging Cable',
        'specs': 'High-Durability Heavy Braided Structural Wire (Type-C / Lightning)',
        'price': 'Flat £7.00',
        'image_file': 'budi_charging_cable.png',
    },
    {
        'category': 'Counter Accessories',
        'title': 'RAW Organic Hemp Slim Rolling Papers',
        'specs': 'Unrefined 100% Natural Organic Flax Rolling Sheets Display Pack',
        'price': 'In stock',
        'image_file': 'raw_papers.png',
    },
    {
        'category': 'Protection & Cases',
        'title': 'Anti Burst Phone Case',
        'specs': 'Shockproof Clear TPU, Reinforced Corners, Scratch Resistant, Available for various iPhone & Samsung Models',
        'price': 'In stock',
        'image_file': 'Anti Burst phone case.jpg',
    },
    {
        'category': 'Laptops',
        'title': 'Apple MacBook Air',
        'specs': '13-Inch Retina Display, Apple M-Series Chip, 8GB RAM, 256GB SSD, Silver',
        'price': 'In stock',
        'image_file': 'Apple MacBook Air silver transparent background.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Apple Watch Series 3',
        'specs': 'Space Gray Aluminum Case, Sport Band, Fitness Tracking, Heart Rate Monitor',
        'price': 'In stock',
        'image_file': 'Apple Watch 38mm.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Apple Watch Series 4',
        'specs': 'Silver Aluminum Case, Sport Band, GPS, Retina Display',
        'price': 'In stock',
        'image_file': 'apple watch 42mm.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Authentic Apple AirPods',
        'specs': 'Wireless Charging Case, Active Noise Cancellation, Bluetooth 5.0, Sweat Resistant',
        'price': 'In stock',
        'image_file': 'Authentic Apple Air Pods.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Core Charger Cable',
        'specs': 'Heavy Duty Braided Lightning to USB-C Cable, Fast Charging Compatible',
        'price': 'In stock',
        'image_file': 'Core charger cable.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Core Dual Wall Charger',
        'specs': 'Dual Port USB-C & USB-A Fast Wall Charger, 20W PD Output',
        'price': 'In stock',
        'image_file': 'Core dual wall charger.jpg',
    },
    {
        'category': 'Protection & Cases',
        'title': 'Defence Folio Phone Case',
        'specs': 'Premium Synthetic Leather, Card Slots & Cash Pocket, Magnetic Closure, Stand Feature',
        'price': 'In stock',
        'image_file': 'Defence folio phone case.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Dual Lens Vehicle Black Box DVR',
        'specs': '1080P Full HD Dashboard Camera, Wide Angle Dual Lens, G-Sensor, Night Vision',
        'price': 'In stock',
        'image_file': 'Dual Lense Vechile black box DVR.jpg',
    },
    {
        'category': 'E-Liquids',
        'title': 'Elfliq Nic Salt 10ml',
        'specs': '10ml Bottle, 10mg/20mg Nicotine Strength, Authentic Elf Bar Flavors',
        'price': 'In stock',
        'image_file': 'Elfliq 10ml bottle white background.jpg',
        'flavours': ['Watermelon', 'Blue Razz Lemonade', 'Kiwi Passion Fruit Guava', 'Blueberry Sour Raspberry', 'Pink Lemonade', 'Spearmint', 'Apple Peach'],
    },
    {
        'category': 'Tech Accessories',
        'title': 'Havit Wireless Headphones',
        'specs': 'Over-Ear Bluetooth Headset, 40mm Drivers, 30 Hours Playtime, Foldable Design',
        'price': 'In stock',
        'image_file': 'Havit headphones.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'High-Speed HDMI Cable',
        'specs': 'Gold-Plated Connectors, Support 4K Ultra HD at 60Hz, Double Shielded',
        'price': 'In stock',
        'image_file': 'HDMI cable.jpg',
    },
    {
        'category': 'Smartphones',
        'title': 'Huawei P30',
        'specs': '128GB Storage, Leica Triple Camera, Breathing Crystal Color, Factory Unlocked',
        'price': 'In stock',
        'image_file': 'Huawei P30 breathing crystal white background.jpg',
        'storages': ['128 GB'],
        'colors': ['Aurora / Breathing Crystal (Light Blue/Silver Gradient)'],
    },
    {
        'category': 'Tech Accessories',
        'title': 'Kakusiga Car Rear View Mirror Phone Mount',
        'specs': '360-Degree Rotating Car Mirror Mount Holder for Smartphones',
        'price': 'In stock',
        'image_file': 'Kakuisga Car Rear view mirror.jpg',
    },
    {
        'category': 'Protection & Cases',
        'title': 'Leather Wallet Flip Phone Case',
        'specs': 'Genuine Leather Texture, Card Slots, Kickstand View, Drop Protection',
        'price': 'In stock',
        'image_file': 'Leather wallet flip phone case white background.jpg',
    },
    {
        'category': 'Laptops',
        'title': 'Lenovo ThinkPad Laptop',
        'specs': 'Intel Core i5, 8GB RAM, 256GB SSD, Windows 10/11 Pro, Business Ready',
        'price': 'In stock',
        'image_file': 'Lenovo ThinkPad business laptop white background.jpg',
    },
    {
        'category': 'Protection & Cases',
        'title': 'Liquid Silicone Phone Case',
        'specs': 'Soft Microfiber Lining, Anti-Scratch & Grip Cover, Sleek Finish',
        'price': 'In stock',
        'image_file': 'Liquid silicone phone case mockup png.jpg',
    },
    {
        'category': 'E-Liquids',
        'title': 'Maryliq Nic Salt 10ml',
        'specs': '10ml E-Liquid by Lost Mary, 20mg Nicotine Strength, Rich Flavor Options',
        'price': 'In stock',
        'image_file': 'Maryliq 10ml bottle png.jpg',
        'flavours': ['Triple Mango', 'Watermelon Ice', 'Double Apple', 'Peach Ice', 'Blackcurrant Apple', 'Lemon Lime', 'Blueberry Sour Raspberry'],
    },
    {
        'category': 'Tech Accessories',
        'title': 'Maxmate Storage Charger',
        'specs': 'Compact Travel Power Bank & Charger, Integrated Storage Case',
        'price': 'In stock',
        'image_file': 'Maxmate storage charger.jpg',
    },
    {
        'category': 'E-Liquids',
        'title': 'Nasty Juice Shortfills (100ml)',
        'specs': '100ml Shortfill Bottle, 70/30 VG/PG Blend, Premium Fruity Mint Flavors',
        'price': 'In stock',
        'image_file': 'Nasty Juice 100ml shortfill bottle transparent.jpg',
        'flavours': ['Grape & Mixed Berries', 'Menthol Tobacco'],
    },
    {
        'category': 'Nicotine Pouches',
        'title': 'Pablo Nicotine Pouches',
        'specs': 'Strong Spit-Free Nicotine Pouches (All Strengths)',
        'price': 'In stock',
        'image_file': 'Pablo Ice Cold can transparent background.jpg',
        'flavours': ['Pablo Ice Cold', 'Pablo Exclusive', 'Pablo Red'],
    },
    {
        'category': 'Smartphones',
        'title': 'Samsung Galaxy A52s 5G',
        'specs': '128GB Storage, 120Hz Super AMOLED Display, Quad Camera, Unlocked',
        'price': 'In stock',
        'image_file': 'Samsung Galaxy A52s white background transparent.jpg',
        'storages': ['128 GB'],
        'colors': ['Awesome White'],
    },
    {
        'category': 'Smartphones',
        'title': 'Samsung Galaxy A71',
        'specs': '128GB Storage, 6.7-Inch Infinity-O Display, Quad Camera, Prism Crush Silver',
        'price': 'In stock',
        'image_file': 'Samsung Galaxy A71 silver white background.jpg',
        'storages': ['128 GB'],
        'colors': ['Prism Crush Silver / Light Blue'],
    },
    {
        'category': 'Tech Accessories',
        'title': 'Samsung USB-C Cable',
        'specs': 'Original Samsung USB-C to USB-C Charging and Data Transfer Cable',
        'price': 'In stock',
        'image_file': 'Samsung USB cable.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'SGL HDMI Cable',
        'specs': 'Heavy Duty Nylon Braided 4K HDMI Cable, Gold Plated Connections',
        'price': 'In stock',
        'image_file': 'SGL Hdmi Cable.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': '2-Pin Shaver Adaptor',
        'specs': 'UK 3-Pin to EU/Shaver 2-Pin Converter Plug for Shaver & Toothbrush',
        'price': 'In stock',
        'image_file': 'Shaver adaptor.jpg',
    },
    {
        'category': 'Protection & Cases',
        'title': 'Silicone Cover Phone Case',
        'specs': 'Flexible TPU Gel, Ultra-Slim Profile, Camera Protection, Crystal Clear',
        'price': 'In stock',
        'image_file': 'Silicone cover phone case.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'TWS Wireless Earbuds',
        'specs': 'Bluetooth 5.3, Smart Touch Control, IPX5 Waterproof, Charging Case',
        'price': 'In stock',
        'image_file': 'TWS wireless earbuds.jpg',
    },
    {
        'category': 'Protection & Cases',
        'title': 'Van Dens Tempered Glass Screen Protector',
        'specs': '9H Hardness Tempered Glass, Case Friendly, High Clarity, Scratch Protection',
        'price': 'In stock',
        'image_file': 'Van - Dens tempered glass Iphone.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Van Dens Wired Headphones',
        'specs': 'In-Ear Wired Earphones, 3.5mm Jack, Built-in Mic, Bass Boosted Stereo',
        'price': 'In stock',
        'image_file': 'Van Dens wired headphones.webp',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Wired Optical Mouse',
        'specs': 'USB Plug and Play Optical Mouse, 3 Buttons, 1200 DPI Precision',
        'price': 'In stock',
        'image_file': 'Wired Mouse.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'WTK Universal Laptop Charger',
        'specs': '90W Universal Power Adapter with 8 Interchangeable Connector Tips',
        'price': 'In stock',
        'image_file': 'WTK automatic laptop charger.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'ZAGG Wired Keyboard',
        'specs': 'Full-Size Keyboard, Low Profile Scissor Keys, USB Wired Connection',
        'price': 'In stock',
        'image_file': 'ZAGG wired keyboard.jpg',
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 13',
        'specs': '128GB Storage, Starlight White, Unlocked, A15 Bionic Chip',
        'price': 'In stock',
        'image_file': 'iPhone 13 starlight white background.jpg',
        'storages': ['128 GB'],
        'colors': ['Pink'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 14',
        'specs': '128GB Storage, Midnight Black, Unlocked, Super Retina XDR Display',
        'price': 'In stock',
        'image_file': 'iPhone 14 midnight transparent background.jpg',
        'storages': ['128 GB'],
        'colors': ['Red', 'Light Pink/Purple'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 8',
        'specs': '64GB Storage, Space Gray, Touch ID Home Button, Factory Unlocked',
        'price': 'In stock',
        'image_file': 'iPhone 8 space gray white background.jpg',
        'storages': ['256 GB'],
        'colors': ['Black'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone SE',
        'specs': '64GB/128GB Storage, Compact iOS Device, Touch ID, Unlocked',
        'price': 'In stock',
        'image_file': 'iPhone SE black background transparent.png',
        'storages': ['64 GB', '128 GB'],
        'colors': ['Red', 'White', 'Black'],
    },
    {
        'category': 'Vape Kits',
        'title': 'SKE Crystal Bar 15K',
        'specs': '15,000+ Puffs, Crystal Clear Design, Mesh Coil, Rechargeable Battery',
        'price': 'In stock',
        'image_file': 'Sky Crystal Plus Vape.webp',
        'flavours': ['Strawberry Raspberry Cherry', 'Kiwi Passion Fruit Guava', 'Pineapple Ice', 'Cherry Ice', 'Mr. Blue', 'Blueberry Sour Raspberry', 'Cherry Berry', 'Lemon & Lime', 'Strawberry Burst'],
    },
    {
        'category': 'Vape Refills',
        'title': 'Hayati 6K Pods',
        'specs': '6,000 Puffs Capacity, Prefilled Mesh Coil Pods, Rich Flavor Profiles',
        'price': 'In stock',
        'image_file': 'Hayatti 6k.webp',
        'flavours': ['Blue Razz Lemonade', 'Strawberry Raspberry', 'Lemon & Lime', 'Juicy Peach'],
    },
    {
        'category': 'Vape Refills',
        'title': 'Vuse Ultra Closed Pods',
        'specs': 'High-Density Nicotine Closed Pod System, Rich Vapor Production',
        'price': 'In stock',
        'image_file': 'Vuse Ultra.jpg',
        'flavours': ['Cherry Ice', 'Dragon Pomegranate'],
    },
    {
        'category': 'Vape Refills',
        'title': 'Elfbar Elfa Prefilled Pods',
        'specs': 'Prefilled Pods for Elfa Pod Kit, Intense Flavor Profiles, Pack of 2',
        'price': 'In stock',
        'image_file': 'Elf Bar Prefilled pods.jpg',
        'flavours': ['Watermelon', 'Raspberry Cherry Ice', 'Mango'],
    },
    {
        'category': 'Vape Kits',
        'title': 'Elfbar 5000',
        'specs': '5,000 Puffs Disposable Vape Kit, Compact & Portable Design',
        'price': 'In stock',
        'image_file': 'Elfbar.jpg',
        'flavours': ['Blue Razz Lemonade', 'Strawberry Ice', 'Watermelon', 'Kiwi Passion Fruit Guava'],
    },
    {
        'category': 'Vape Kits',
        'title': 'Bloody Bar Pod Twist 20K',
        'specs': '20,000 Puffs Capacity, Unique Pod Twist Dual Flavor Switcher',
        'price': 'In stock',
        'image_file': 'Bloody Bar pod twist.jpg',
        'flavours': ['Blueberry Cherry Cranberry', 'Fresh Mint', 'Strawberry Watermelon'],
    },
    {
        'category': 'Vape Refills',
        'title': 'Lost Mary NERA 15K Pods',
        'specs': '15,000 Puffs Capacity Replacement Pods, Intelligent Smart Display Panel',
        'price': 'In stock',
        'image_file': 'Lost mary 15k.jpg',
        'flavours': ['Strawberry Ice', 'Kiwi Passion Fruit Guava', 'Fizzy Pineapple', 'Raspberry Watermelon', 'Pineapple Ice', 'Summer Grape', 'Dubai Chocolate', 'Strawberry Watermelon', 'Golden Mango', 'Sour Pineapple', 'Triple Mango', 'Juicy Peach', 'Mint', 'Cherry Sour Raspberry', 'Blueberry Raspberry', 'Cherry Ice', 'Raspberry Peach', 'Menthol', 'Miami Mint', 'Fruit Punch', 'Blue Razz Ice', 'Grape', 'Berry Mix', 'Banana Ice', 'Lemon Lime', 'Watermelon Ice', 'Sparkling Cherry', 'Pineapple Apple Pear', 'Strawberry Raspberry'],
    },
    {
        'category': 'Vape Kits',
        'title': 'Lost Mary BM6000 / 6K Pods',
        'specs': '6,000 Puffs Rechargeable Device with Click-In E-Liquid Bottle System',
        'price': 'In stock',
        'image_file': 'Lost Mary BM6000.jpg',
        'flavours': ['Strawberry Raspberry Cherry Ice', 'Cherry Ice', 'Smooth Tobacco', 'Triple Melon', 'Strawberry Watermelon', 'Pink Lemonade', 'Pineapple Ice', 'Blue Razz Lemonade', 'Blueberry', 'Blueberry Sour Raspberry', 'Cola', 'Strawberry Ice', 'Lemon Lime', 'Fresh Mint', 'Menthol', 'Miami Mint', 'Triple Mango', 'Watermelon Ice', 'Double Apple', 'Cherry Peach Lemonade', 'Juicy Peach', 'Banana Ice', 'Apple Pear', 'Fizzy Cherry', 'Grape', 'Strawberry Kiwi'],
    },
    {
        'category': 'E-Liquids',
        'title': 'Juice Bar Shortfills (100ml)',
        'specs': '100ml Shortfill E-Liquid, Premium High-VG Cloud Chaser Formula',
        'price': 'In stock',
        'image_file': 'Tasty Juice.jpg',
        'flavours': ['Banana Ice', 'Pineapple Peach Mango'],
    },
    {
        'category': 'Vape Refills',
        'title': 'VEEV One Pods',
        'specs': 'Premium VEEV One Closed Pod System, Rich & Satisfying Draw, Pack of 2',
        'price': 'In stock',
        'image_file': 'Veev one pods.jpg',
        'flavours': ['Classic Tobacco', 'Velvet Valley'],
    },
    {
        'category': 'E-Liquids',
        'title': 'Brand-Specific Nic Salts (10ml)',
        'specs': '10ml Premium Nicotine Salts from Top Brands (Dinner Lady, Mary Liq, Nasty, Hayati)',
        'price': 'In stock',
        'image_file': 'Maryliq 10ml bottle png.jpg',
        'flavours': ['Strawberry Ice', 'Strawberry Banana', 'Blackberry Ice', 'Fresh Mint', 'Pink Lemonade'],
    },
    {
        'category': 'Vape Kits',
        'title': 'OXVA Slimstick Vape Kit',
        'specs': 'Ultra Portable Slim Pod System, High Performance Mesh Coil, Auto-Draw',
        'price': 'In stock',
        'image_file': 'Slimstick Oxva.webp',
    },
    {
        'category': 'Vape Kits',
        'title': 'Vaporesso Xros 5 Pod Kit',
        'specs': 'Premium Vaporesso Pod System, Corex Heating Technology, 1000mAh Battery',
        'price': 'In stock',
        'image_file': 'Vaporesso Xros 5.jpg',
    },
    {
        'category': 'Vape Kits',
        'title': 'Voopoo Drag Vape Kit',
        'specs': 'Advanced Voopoo Drag Series Pod Mod, Intelligent Gene Chip, Dynamic Airflow',
        'price': 'In stock',
        'image_file': 'Voopoo drag.webp',
    },
    {
        'category': 'Vape Kits',
        'title': 'IQOS Iluma I One Kit',
        'specs': 'Next-Gen Induction Heating System, Single-Piece Device, 20 Consecutive Uses',
        'price': 'In stock',
        'image_file': 'Iluama I one.jpg',
    },
    {
        'category': 'Counter Accessories',
        'title': 'D&K Herb Crusher',
        'specs': 'Premium Metal Magnetic Herb Grinder, Sharp Diamond Teeth, 4-Piece Setup',
        'price': 'In stock',
        'image_file': 'D and K herb crusher.jpg',
    },
    {
        'category': 'Counter Accessories',
        'title': 'D&K Metal Pipe',
        'specs': 'Durable Pocket-Sized Metal Smoking Pipe, Easy to Clean, Heat Resistant',
        'price': 'In stock',
        'image_file': 'D and K metal pipe.jpg',
    },
    {
        'category': 'Counter Accessories',
        'title': 'Small Green Rizla Papers',
        'specs': 'Rizla Green Standard Size Rolling Papers, Medium Weight, Pack of 50',
        'price': 'In stock',
        'image_file': 'Small green rizla paper.png',
    },
    {
        'category': 'Counter Accessories',
        'title': 'Small Orange Rizla Papers',
        'specs': 'Rizla Orange Standard Size Rolling Papers, Slow Burning, Pack of 50',
        'price': 'In stock',
        'image_file': 'Small orange rizla paper.jpg',
    },
    {
        'category': 'Counter Accessories',
        'title': 'Thin Blue Rizla Papers',
        'specs': 'Rizla Blue King Size Slim Rolling Papers, Ultra Thin, Pack of 32',
        'price': 'In stock',
        'image_file': 'Thin Blue Rizla paper.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Apple Watch Series 2',
        'specs': 'Aluminum Case, Sport Band, GPS, Heart Rate Sensor',
        'price': 'In stock',
        'image_file': 'Iwatch 2.jpg',
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 16',
        'specs': '128GB Storage Tier, Apple Dual Camera System, Action Button',
        'price': 'In stock',
        'image_file': 'iPhone 16.jpg',
        'storages': ['128 GB'],
        'colors': ['Black', 'Pink', 'White'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 15 Plus',
        'specs': '128GB Storage, High-Density Battery, Unlocked Super Retina XDR Display',
        'price': 'In stock',
        'image_file': 'Iphone 15 plus.jpg',
        'storages': ['128 GB'],
        'colors': ['Black'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 15',
        'specs': '128GB Storage, Dynamic Island Display, Unlocked iOS Smartphone',
        'price': 'In stock',
        'image_file': 'iPhone 15.jpg',
        'storages': ['128 GB'],
        'colors': ['Black', 'White/Silver'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 14 Pro',
        'specs': '128GB Storage, Dynamic Island Screen, Pro-Grade Camera Module',
        'price': 'In stock',
        'image_file': 'Iphone 14 pro.jpg',
        'storages': ['128 GB'],
        'colors': ['Purple'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 13 Pro Max',
        'specs': '128GB Storage, ProMotion High Refresh Display, Factory Unlocked',
        'price': 'In stock',
        'image_file': 'iPhone 13 Pro Max.jpg',
        'storages': ['128 GB'],
        'colors': ['Graphite/Black'],
    },
    {
        'category': 'Smartphones',
        'title': 'Apple iPhone 11 Pro',
        'specs': 'Triple Camera Array, Super Retina XDR Display, Premium iOS Smartphone',
        'price': 'In stock',
        'image_file': 'iPhone 11 Pro.jpg',
        'colors': ['Gold'],
    },
    {
        'category': 'Tablets',
        'title': 'Samsung Galaxy Tab A11',
        'specs': 'Premium Android Tablet, Long-Lasting Battery, HD Display',
        'price': 'In stock',
        'image_file': 'Galaxy Tab A11.webp',
    },
    {
        'category': 'Gaming',
        'title': 'KM6 4-in-1 Gaming Set',
        'specs': 'Includes LED Keyboard, Gaming Mouse, Headset, and Mousepad',
        'price': 'In stock',
        'image_file': 'KM6 4 in one gaming set.jpg',
    },
    {
        'category': 'Laptops',
        'title': 'Apple MacBook Air (2022)',
        'specs': 'M2 Chip, Liquid Retina Display, 8GB RAM, 256GB SSD',
        'price': 'In stock',
        'image_file': 'Macbook air 2022.jpg',
    },
    {
        'category': 'Laptops',
        'title': 'Apple MacBook Pro 13-Inch',
        'specs': 'Retina Display, Intel Core / Apple M-Series Chip, Unlocked',
        'price': 'In stock',
        'image_file': 'Macbook pro 13 inch.jpg',
    },
    {
        'category': 'Vape Kits',
        'title': 'SKE Crystal 600 Pro Disposable Vape',
        'specs': 'Up to 600 Puffs, 2ml Prefilled E-Liquid, 2% Nicotine (20mg)',
        'price': 'In stock',
        'image_file': 'SKE Crystal 600 Pro.jpg',
        'flavours': ['Blueberry Sour Raspberry', 'Watermelon Ice', 'Lemon & Lime', 'Fizzy Cherry', 'Pink Lemonade', 'Menthol'],
    },
    {
        'category': 'Vape Kits',
        'title': 'OXVA NeXLiM Pod Kit',
        'specs': '40W Max Output, 1500mAh Battery, 0.85-inch Color Screen, Dual Mesh',
        'price': 'In stock',
        'image_file': 'OXVA Nexlim.jpg',
    },
    {
        'category': 'Vape Kits',
        'title': 'Pyne Pod Click 6K Starter Kit',
        'specs': 'Prefabricated Pod & E-Liquid Bottle System, Rechargeable Type-C',
        'price': 'In stock',
        'image_file': 'Pyne pod click.jpg',
    },
    {
        'category': 'Tablets',
        'title': 'Apple iPad mini 4',
        'specs': '7.9-inch Retina Display, A8 Chip, Touch ID, Wi-Fi / Cellular, Unlocked',
        'price': 'In stock',
        'image_file': 'iPad mini 4.jpg',
    },
    {
        'category': 'E-Liquids',
        'title': 'Fizzy Juice E-Liquid (120ml Shortfill)',
        'specs': '120ml Bottle, 70VG/30PG Ratio, Low Mint Cooling Effect, Nic Shot Ready',
        'price': 'In stock',
        'image_file': 'Fizzy Juice Strawberry.jpg',
        'flavours': ['Fizzy Strawberry', 'Fizzy Grape', 'Fizzy Wild Berries'],
    },
    {
        'category': 'E-Liquids',
        'title': 'Ramillion Nic Salts (10ml)',
        'specs': '10ml Bottles, 10mg / 20mg Nicotine Strengths, Balanced 50VG/50PG Ratio',
        'price': 'In stock',
        'image_file': 'Ramillion nic salts.jpg',
        'flavours': ['Pink Lemonade', 'Strawberry Ice', 'Peach Ice'],
    },
    {
        'category': 'Nicotine Pouches',
        'title': 'Skruf Superwhite Nicotine Pouches',
        'specs': 'Superslim Format, Premium All-White Portions, Long-Lasting Nicotine Release',
        'price': 'In stock',
        'image_file': 'Skruf nicotine pouches.jpg',
        'flavours': ['Frozen Mint Xtra', 'Fresh Mint', 'Blackberry'],
    },
    {
        'category': 'Counter Accessories',
        'title': 'Elements Ultra Thin Rice Rolling Papers',
        'specs': 'King Size Ultra-Thin Rice Papers, Sugar Gum, 33 Leaves per Pack',
        'price': 'In stock',
        'image_file': 'Elements Rice Papers.jpg',
    },
    {
        'category': 'Vape Refills',
        'title': 'Innokin Prism T20 Replacement Coils (5-Pack)',
        'specs': '1.5 ohm Resistance (12W - 14W), Compatible with Prism T20 Tank, 5 Coils per Pack',
        'price': 'In stock',
        'image_file': 'Innokin T20 Coils.jpg',
    },
    {
        'category': 'Vape Kits',
        'title': 'Aspire PockeX AIO Starter Kit',
        'specs': 'All-in-One Pocket Kit, 1500mAh Internal Battery, 2ml Tank, Top Airflow Sizing',
        'price': 'In stock',
        'image_file': 'Aspire PockeX Kit.jpg',
    },
    {
        'category': 'SIM Cards',
        'title': 'EE Pay As You Go SIM Card',
        'specs': '5G-Ready Multi-Fit (Nano/Micro/Standard) SIM Card, Simple Activation, Pay-As-You-Go',
        'price': 'In stock',
        'image_file': 'EE SIM Card.png',
    },
    {
        'category': 'Vape Kits',
        'title': 'Geekvape Aegis Solo Vape Kit',
        'specs': 'Dustproof, Shockproof, Waterproof, 100W Max Wattage, Single 18650 Battery Mod',
        'price': 'In stock',
        'image_file': 'Geekvape Aegis Kit.jpg',
    },
    {
        'category': 'SIM Cards',
        'title': 'giffgaff Pay As You Go SIM Card',
        'specs': 'Multi-fit SIM Card, Runs on O2 Network, No Contract Required, 5G Ready',
        'price': 'In stock',
        'image_file': 'Giffgaff SIM Card.jpg',
    },
    {
        'category': 'SIM Cards',
        'title': 'Lebara Pay As You Go SIM Card',
        'specs': 'Cheap International Minutes, Runs on Vodafone Network, Multi-fit Nano/Micro SIM',
        'price': 'In stock',
        'image_file': 'Lebara SIM Card.webp',
    },
    {
        'category': 'SIM Cards',
        'title': 'Lycamobile Pay As You Go SIM Card',
        'specs': 'Low-Cost International Calls, Easy Top-Up, Multi-fit SIM Card, 5G Enabled',
        'price': 'In stock',
        'image_file': 'Lycamobile SIM Card.jpg',
    },
    {
        'category': 'Vape Refills',
        'title': 'SMOK TFV16 Sub-Ohm Tank',
        'specs': '9ml Liquid Capacity, Dual Mesh Coils, Top Rotary Refill System, Large Airflow Ports',
        'price': 'In stock',
        'image_file': 'SMOK TFV16 Tank.jpg',
    },
    {
        'category': 'Vape Kits',
        'title': 'Vaporesso GTX One Pod Kit',
        'specs': '2000mAh Battery Mod, Adjustable 40W Output, MTL Vaping Optimized, Type-C Charging',
        'price': 'In stock',
        'image_file': 'Vaporesso GTX One Kit.jpg',
    },
    {
        'category': 'Vape Refills',
        'title': 'Vaporesso GTX Pod 26 (2-Pack)',
        'specs': '5.5ml Capacity Replacement Pods, SSS Leak-Resistant Technology, Magnetic Connection',
        'price': 'In stock',
        'image_file': 'Vaporesso GTX Pod 26.jpg',
    },
    {
        'category': 'SIM Cards',
        'title': 'Vodafone Pay As You Go SIM Card',
        'specs': 'Standard Vodafone Pay-As-You-Go SIM, 5G Network Support, Multi-fit Sizing',
        'price': 'In stock',
        'image_file': 'Vodafone SIM Card.webp',
    },
    {
        'category': 'Vape Kits',
        'title': 'Voopoo Drag Nano 2 Pod Kit',
        'specs': 'Compact Metal Chassis Mod, 800mAh Battery, 3 Adjustable Power Levels, Top-Fill Pod',
        'price': 'In stock',
        'image_file': 'Voopoo Drag Nano 2 Kit.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Efest Lush Q2 Intelligent Battery Charger',
        'specs': 'Dual-Slot Charger, LED Indicators, Auto Cut-off, Charges 18650, 20700, 21700 Vaping Batteries',
        'price': 'In stock',
        'image_file': 'Efest Lush Q2 Charger.jpg',
    },
    {
        'category': 'Vape Kits',
        'title': 'Vuse Go Disposable Vape',
        'specs': 'Up to 800 Puffs, 2ml Prefilled E-Liquid, 2% Nicotine (20mg), Compact Metal Design',
        'price': 'In stock',
        'image_file': 'Vuse Go.jpg',
        'flavours': ['Creamy Tobacco', 'Mint Ice', 'Berry Blend', 'Watermelon Ice', 'Mango Ice', 'Strawberry Ice'],
    },
    {
        'category': 'Vape Refills',
        'title': 'Vuse ePod Replacement Pods',
        'specs': 'Prefilled Closed Pods for Vuse ePod 2 Device, 1.9ml Capacity, Pack of 2',
        'price': 'In stock',
        'image_file': 'Vuse epod.jpg',
        'flavours': ['Golden Tobacco', 'Chilled Mint', 'Very Berry', 'Cucumber Mix', 'Watermelon Ice'],
    },
    {
        'category': 'E-Liquids',
        'title': 'Royale CBD E-Liquid (1000mg)',
        'specs': '10ml Premium CBD E-Liquid, Organic Hemp Extract, 0% THC, Rich Flavors',
        'price': 'In stock',
        'image_file': 'CBD Royale.jpg',
        'flavours': ['Mixed Berry', 'Mango Ice', 'Lemon Haze', 'Strawberry', 'Peppermint'],
    },
    {
        'category': 'E-Liquids',
        'title': 'SKE Crystal Nic Salts (10ml)',
        'specs': '10ml Bottle SKE Crystal Bar Official E-Liquid, 10mg / 20mg Strengths, Smooth 50/50 VG/PG',
        'price': 'In stock',
        'image_file': 'SKE Crystal Salts.jpg',
        'flavours': ['Lemon & Lime', 'Blueberry Sour Raspberry', 'Strawberry Burst', 'Cherry Ice', 'Pink Lemonade'],
    },
    {
        'category': 'Vape Kits',
        'title': 'Hayati Pro Max 4000',
        'specs': 'Up to 4000 Puffs Disposable Vape, 1400mAh Battery, Prefilled Mesh Coil, TPD Compliant',
        'price': 'In stock',
        'image_file': 'Hayati Pro Max 4000.jpg',
        'flavours': ['Blue Razz Gummy Bear', 'Summer Dream', 'Fresh Mint', 'Lemon & Lime', 'Cherry Cola'],
    },
    {
        'category': 'Vape Kits',
        'title': 'PIXL 6000 Big Puff Vape Kit',
        'specs': 'Up to 6000 Puffs, Rechargeable Battery, 2ml Prefilled Pod + 10ml Bottle Fed System, TPD Compliant',
        'price': 'In stock',
        'image_file': 'Pixl 6000..jpg',
        'flavours': ['Blueberry Sour Raspberry', 'Lemon & Lime', 'Strawberry Ice', 'Cherry Ice', 'Gummy Bear'],
    },
    {
        'category': 'Drinks',
        'title': 'Chilled Coca-Cola Classic',
        'specs': '330ml ice-cold canned carbonated soft drink',
        'price': 'In stock',
        'image_file': 'cola.jpg',
    },
    {
        'category': 'Drinks',
        'title': 'Chilled Still Spring Water',
        'specs': '500ml pure chilled still mineral water',
        'price': 'In stock',
        'image_file': 'water.jpg',
    },
    {
        'category': 'Drinks',
        'title': 'Chilled Red Bull Energy Drink',
        'specs': '250ml chilled energy drink for a quick mental and physical boost',
        'price': 'In stock',
        'image_file': 'Redbull.webp',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Yesplus Handheld USB Mini Fan',
        'specs': 'Portable Rechargeable Pocket Fan, 3 Speed Modes, Long-Life Battery, Micro-USB Charging',
        'price': 'In stock',
        'image_file': 'Yesplus mini fan.webp',
    },
    {
        'category': 'Tech Accessories',
        'title': '1080p Smart Home Security Camera',
        'specs': 'Wi-Fi IP Camera, Night Vision, Two-Way Audio, Motion Detection, Cloud & MicroSD Storage',
        'price': 'In stock',
        'image_file': 'Security Camera.jpg',
    },
    {
        'category': 'Vape Kits',
        'title': 'Elf Bar ELFA Pro Prefilled Pod Kit',
        'specs': 'Prefilled Pod Starter Kit, Rechargeable 500mAh Battery, Fast Type-C Charging, Includes 1x Prefilled Pod',
        'price': 'In stock',
        'image_file': 'Elfa Pro Kit.jpg',
        'flavours': ['Blue Razz Lemonade', 'Watermelon', 'Pink Lemonade', 'Kiwi Passion Fruit Guava', 'Blueberry Sour Raspberry'],
    },
    {
        'category': 'Vape Kits',
        'title': 'Elf Bar 600 Disposable Vape',
        'specs': 'Up to 600 Puffs, 2ml Prefilled Nic Salt E-Liquid, 2% Nicotine (20mg), Draw-Activated',
        'price': 'In stock',
        'image_file': 'Elf Bar 600.jpg',
        'flavours': ['Watermelon', 'Blueberry Sour Raspberry', 'Pink Lemonade', 'Strawberry Ice', 'Cola'],
    },
    {
        'category': 'E-Liquids',
        'title': 'Nasty Juice Podmate Nic Salts (10ml)',
        'specs': '10ml Bottles Optimized for Pod Kits, 10mg / 20mg Nicotine Strengths, Rich Throat Hit',
        'price': 'In stock',
        'image_file': 'Podmate Nic Salts.jpg',
        'flavours': ['Peach Lemonade', 'Red Apple', 'Grape & Berry', 'Spearmint', 'Strawberry Kiwi'],
    },
    {
        'category': 'E-Liquids',
        'title': 'Nasty Juice Shortfill - Wicked Haze (60ml)',
        'specs': '60ml Shortfill E-Liquid, Blackcurrant and Lemonade Menthol Blend, 70% VG Cloud Chasing Formula',
        'price': 'In stock',
        'image_file': 'Wicked Haze.jpg',
    },
    {
        'category': 'E-Liquids',
        'title': 'CBD Leaf E-Liquid (100ml)',
        'specs': '100ml Premium CBD Isolate E-Liquid, 1000mg Strength, 0% THC, Fruit & Menthol Blends',
        'price': 'In stock',
        'image_file': 'CBD Leaf.jpg',
        'flavours': ['Blackcurrant', 'Blue Raspberry', 'Gummy Bear', 'Menthol'],
    },
    {
        'category': 'Smartphones',
        'title': 'Honor X6a',
        'specs': '128GB Storage, 4GB RAM, 50MP Triple Camera, 5200mAh Battery, Google Play Services',
        'price': 'In stock',
        'image_file': 'Honor X6.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'Samsung Galaxy S10 Type-C Fast Charging Cable',
        'specs': 'Durable Braided USB-A to USB-C Data Sync & Power Fast Cable, 1.2 Meter',
        'price': 'In stock',
        'image_file': 'Samsung Type-C Cable.png',
    },
    {
        'category': 'Tech Accessories',
        'title': 'MTK High-Speed Portable SSD',
        'specs': '512GB / 1TB External USB 3.2 Gen 2 SSD, Ultra Compact, Shock Resistant',
        'price': 'In stock',
        'image_file': 'MTK SSD.jpg',
    },
    {
        'category': 'Tech Accessories',
        'title': 'MTK External Hard Drive (HDD)',
        'specs': '1TB / 2TB Portable Hard Drive, USB 3.0 Interface, Plug & Play Backup',
        'price': 'In stock',
        'image_file': 'MTK External Hard Drive.jpg',
    },
    {
        'category': 'Vape Kits',
        'title': 'IVG 600 Disposable Vape',
        'specs': 'Up to 600 Puffs, 2ml Prefilled E-Liquid, 20mg (2%) Nicotine, Draw-Activated Vapour',
        'price': 'In stock',
        'image_file': 'IVG 600.jpg',
        'flavours': ['Strawberry Watermelon', 'Blue Raspberry Ice', 'Classic Menthol', 'Fizzy Cherry'],
    },
    {
        'category': 'Tech Accessories',
        'title': '45W USB-C Super Fast Power Adapter',
        'specs': 'Samsung/Apple Compatible 45W PD Wall Charger Plug, Compact GaN Tech, Safe Charging',
        'price': 'In stock',
        'image_file': '45W Charger.jpg',
    },
    {
        'category': 'E-Liquids',
        'title': 'V-Juice - Tuned In Nic Salt (10ml)',
        'specs': '10ml Premium Nicotine Salt E-Liquid, Famous Cherry Menthol Blend, 50VG/50PG for Pods',
        'price': 'In stock',
        'image_file': 'Tuned In Cherry.jpg',
    },
]

# Reorder PRODUCTS: group by category in logical order, then configured first, bare last
CATEGORY_ORDER = [
    "Smartphones",
    "Tablets",
    "Laptops",
    "Gaming",
    "Vape Kits",
    "Vape Refills",
    "E-Liquids",
    "Nicotine Pouches",
    "Tech Accessories",
    "Protection & Cases",
    "Counter Accessories",
    "SIM Cards",
    "Drinks"
]

grouped_products = {cat: [] for cat in CATEGORY_ORDER}
for p in PRODUCTS:
    cat = p["category"]
    if cat not in grouped_products:
        grouped_products[cat] = []
    grouped_products[cat].append(p)

sorted_products = []
for cat in CATEGORY_ORDER:
    if cat in grouped_products:
        cat_products = grouped_products[cat]
        # sort so that items with options (colors, storages, flavours) come first, bare last
        cat_products_sorted = sorted(cat_products, key=lambda x: 0 if (x.get("colors") or x.get("storages") or x.get("flavours")) else 1)
        sorted_products.extend(cat_products_sorted)

PRODUCTS = sorted_products


def get_catalogue_page_html():
    cards_html = ""
    COLOR_HEX = {
        "Natural": "#BEB2A2",
        "Black": "#1C1C1E",
        "White": "#F5F5F7",
        "Natural/Grey": "#8E8E93",
        "Red": "#E31837",
        "Light Pink/Purple": "#E8D8F8",
        "Pink": "#FFC0CB",
        "Gold": "#F4D068",
        "Phantom Black": "#1A1A1A",
        "Prism Crush Silver / Light Blue": "linear-gradient(135deg, #E2E8F0 0%, #BAE6FD 100%)",
        "Awesome Violet / Light Purple": "#E2D3F5",
        "Awesome White": "#FAF9F6",
        "Aurora / Breathing Crystal (Light Blue/Silver Gradient)": "linear-gradient(135deg, #E0F2FE 0%, #E2E8F0 50%, #C084FC 100%)",
        "Awesome Black": "#1E1E1F",
        "Purple": "#4E365E",
        "Dark Titanium/Black": "#2E3033",
        "Graphite/Black": "#3E3E40",
        "White/Silver": "#F0F0F2"
    }

    for p in PRODUCTS:
        category = p["category"]
        title = p["title"]
        specs = p["specs"]
        price = p["price"]
        img_file = p["image_file"]
        
        # Check for flavours button
        flavours = p.get("flavours", [])
        flavours_btn = ""
        flavours_data = ""
        if flavours:
            escaped_title = title.replace("'", "\\'")
            flavours_json = "[" + ", ".join(f"'{f.replace("'", "\\'")}'" for f in flavours) + "]"
            flavours_btn = f'''
            <button class="btn btn-secondary product-cta-btn" onclick="openFlavoursModal('{escaped_title}', {flavours_json})" style="margin-top: 10px; background-color: var(--bg-alternate); border: 1px solid var(--border-color); color: var(--text-main); font-weight: 600; font-size: 0.8rem; cursor: pointer; transition: background-color 0.2s ease, transform 0.15s ease;">
                <i class="fa-solid fa-droplet"></i> View Flavours
            </button>
            '''
            flavours_data = ", ".join(flavours).lower()

        # Check for colors or storages options button
        colors = p.get("colors", [])
        storages = p.get("storages", [])
        options_btn = ""
        colors_data = ""
        storages_data = ""
        if colors or storages:
            escaped_title = title.replace("'", "\\'")
            colors_json = "[" + ", ".join(f"'{c.replace("'", "\\'")}'" for c in colors) + "]"
            storages_json = "[" + ", ".join(f"'{s.replace("'", "\\'")}'" for s in storages) + "]"
            options_btn = f'''
            <button class="btn btn-secondary product-cta-btn" onclick="openOptionsModal('{escaped_title}', {colors_json}, {storages_json})" style="margin-top: 10px; background-color: var(--bg-alternate); border: 1px solid var(--border-color); color: var(--text-main); font-weight: 600; font-size: 0.8rem; cursor: pointer; transition: background-color 0.2s ease, transform 0.15s ease;">
                <i class="fa-solid fa-sliders"></i> View Colors and Storage
            </button>
            '''
            colors_data = ", ".join(colors).lower()
            storages_data = ", ".join(storages).lower()

        if price == "In stock":
            price_html = '<span class="contact-price">In stock</span>'
        else:
            price_html = f'<span class="base-price">{price}</span>'
            
        cards_html += f'''
            <div class="product-card" data-category="{category}" data-title="{title.lower()}" data-specs="{specs.lower()}" data-flavours="{flavours_data}" data-colors="{colors_data}" data-storages="{storages_data}">
                <div class="product-image-wrapper">
                    <img src="Fast acsess images/{img_file}" alt="{title}" class="product-image" loading="lazy">
                    <span class="product-category-badge">{category}</span>
                </div>
                <div class="product-details">
                    <h4 class="product-title">{title}</h4>
                    <p class="product-specs">{specs}</p>
                    
                    {options_btn}
                    
                    <div class="product-price-row">
                        {price_html}
                    </div>
                    
                    {flavours_btn}
                </div>
            </div>
        '''
    html = '''
    <!-- Search Section -->
    <section class="search-section">
        <div class="container">
            <div class="section-header text-center reveal" style="margin-bottom: 20px;">
                <span class="section-subtitle">Catalog</span>
                <h2>In-Store Products</h2>
                <p class="subheading">Search and browse our stock of smartphones, tablets, vapes, nicotine pouches, and accessories.</p>
                <div class="accent-divider"></div>
            </div>
        </div>
    </section>

    <!-- Catalogue Layout Container -->
    <section class="catalogue-showcase-section" style="padding-top: 0;">
        <div class="container catalogue-layout reveal">
            <!-- Left Side: Sidebar Filter Navigation -->
            <aside class="catalogue-sidebar">
                <h3 class="sidebar-title">Categories</h3>
                <div class="product-filter-bar">
                    <button class="filter-btn active" onclick="setCategory(\'All\', this)"><i class="fa-solid fa-tags"></i> All Products</button>
                    <button class="filter-btn" onclick="setCategory(\'Smartphones\', this)"><i class="fa-solid fa-mobile-screen"></i> Smartphones</button>
                    <button class="filter-btn" onclick="setCategory(\'Tablets\', this)"><i class="fa-solid fa-tablet-screen-button"></i> Tablets</button>
                    <button class="filter-btn" onclick="setCategory(\'Laptops\', this)"><i class="fa-solid fa-laptop"></i> Laptops</button>
                    <button class="filter-btn" onclick="setCategory(\'Vape Kits\', this)"><i class="fa-solid fa-box"></i> Vape Kits</button>
                    <button class="filter-btn" onclick="setCategory(\'Vape Refills\', this)"><i class="fa-solid fa-circle-nodes"></i> Vape Refills</button>
                    <button class="filter-btn" onclick="setCategory(\'Nicotine Pouches\', this)"><i class="fa-solid fa-cubes"></i> Nicotine Pouches</button>
                    <button class="filter-btn" onclick="setCategory(\'E-Liquids\', this)"><i class="fa-solid fa-droplet"></i> E-Liquids</button>
                    <button class="filter-btn" onclick="setCategory(\'Tech Accessories\', this)"><i class="fa-solid fa-plug"></i> Tech Accessories</button>
                    <button class="filter-btn" onclick="setCategory(\'Protection & Cases\', this)"><i class="fa-solid fa-shield"></i> Protection and Cases</button>
                    <button class="filter-btn" onclick="setCategory(\'Gaming\', this)"><i class="fa-solid fa-gamepad"></i> Gaming</button>
                    <button class="filter-btn" onclick="setCategory(\'Drinks\', this)"><i class="fa-solid fa-bottle-water"></i> Drinks</button>
                    <button class="filter-btn" onclick="setCategory(\'Counter Accessories\', this)"><i class="fa-solid fa-cash-register"></i> Counter Accessories</button>
                </div>
            </aside>

            <!-- Right Side: Search and Product Grid -->
            <div class="catalogue-main">
                <div class="search-box-wrapper" style="margin-bottom: 30px;">
                    <i class="fa-solid fa-magnifying-glass search-icon"></i>
                    <input type="text" id="catalogueSearch" placeholder="Search products by name, brand, specifications, or flavours..." oninput="filterCatalogue()">
                </div>
                <div class="showcase-grid" id="catalogue-grid">
    ''' + cards_html + '''
                </div>
            </div>
        </div>
    </section>

    <!-- Not sure call CTA Banner -->
    <section class="service-cta text-center reveal" style="padding: 40px 0; background: var(--bg-alternate); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); margin-top: 50px;">
        <div class="container">
            <h2 style="font-size: 1.6rem; margin-bottom: 10px;">Not sure if we stock your desired item?</h2>
            <p style="margin-bottom: 20px; color: var(--text-muted); font-size: 0.95rem;">Give us a call and our counter staff will check our live stock for you immediately.</p>
            <a href="tel:07466540111" class="btn btn-primary" style="font-size: 0.95rem; padding: 10px 24px;"><i class="fa-solid fa-phone"></i> Call Fast Access</a>
        </div>
    </section>

    <script>
        let currentCategory = \'All\';
        
        function setCategory(category, btnEl) {
            currentCategory = category;
            // Toggle active class on filter buttons
            document.querySelectorAll(\'.product-filter-bar .filter-btn\').forEach(btn => {
                btn.classList.remove(\'active\');
            });
            btnEl.classList.add(\'active\');
            filterCatalogue();
        }
        
        function filterCatalogue() {
            const searchVal = document.getElementById(\'catalogueSearch\').value.toLowerCase().trim();
            const cards = document.querySelectorAll(\'#catalogue-grid .product-card\');
            
            cards.forEach(card => {
                const cardCat = card.getAttribute(\'data-category\');
                const cardTitle = card.getAttribute(\'data-title\');
                const cardSpecs = card.getAttribute(\'data-specs\');
                const cardFlavours = card.getAttribute('data-flavours') || '';
                const cardColors = card.getAttribute('data-colors') || '';
                const cardStorages = card.getAttribute('data-storages') || '';
                
                const matchCategory = (currentCategory === 'All' || cardCat === currentCategory);
                const matchSearch = (!searchVal || cardTitle.includes(searchVal) || cardSpecs.includes(searchVal) || cardFlavours.includes(searchVal) || cardColors.includes(searchVal) || cardStorages.includes(searchVal));if (matchCategory && matchSearch) {
                    card.style.display = \'flex\';
                } else {
                    card.style.display = \'none\';
                }
            });
        }
        
        // Handle pre-selected category via query params on load
        window.addEventListener(\'DOMContentLoaded\', () => {
            const params = new URLSearchParams(window.location.search);
            const catParam = params.get(\'category\');
            if (catParam) {
                // Find matching button text
                const buttons = Array.from(document.querySelectorAll(\'.product-filter-bar .filter-btn\'));
                const btn = buttons.find(b => b.textContent.trim().toLowerCase() === catParam.toLowerCase() || 
                                              (catParam.toLowerCase() === \'smartphones\' && b.textContent.trim().toLowerCase() === \'smartphones\'));
                if (btn) {
                    setCategory(btn.textContent.trim(), btn);
                } else {
                    filterCatalogue();
                }
            } else {
                filterCatalogue();
            }
        });
    </script>
    '''
    return html


def get_product_showcase_html():
    html = '''
    <!-- Product Showcase Grid Section -->
    <section class="product-showcase-section" id="products-showcase">
        <div class="container">
            <div class="section-header text-center reveal">
                <span class="section-subtitle">Catalog</span>
                <h2>In-Store Products</h2>
                <p class="subheading">Browse our live stock of smartphones, laptops, vapes, and tech accessories. Visit us in-store to purchase.</p>
                <div class="accent-divider"></div>
            </div>
            
            <div class="product-filter-bar reveal">
                <button class="filter-btn active" onclick="filterShowcase('All')">All Products</button>
                <button class="filter-btn" onclick="filterShowcase('Counter Accessories')">Counter Accessories</button>
                <button class="filter-btn" onclick="filterShowcase('Drinks')">Drinks</button>
                <button class="filter-btn" onclick="filterShowcase('SIM Cards')">SIM Cards</button>
                <button class="filter-btn" onclick="filterShowcase('E-Liquids')">E-Liquids</button>
                <button class="filter-btn" onclick="filterShowcase('Gaming')">Gaming</button>
                <button class="filter-btn" onclick="filterShowcase('Laptops')">Laptops</button>
                <button class="filter-btn" onclick="filterShowcase('Nicotine Pouches')">Nicotine Pouches</button>
                <button class="filter-btn" onclick="filterShowcase('Protection & Cases')">Protection & Cases</button>
                <button class="filter-btn" onclick="filterShowcase('Smartphones')">Smartphones</button>
                <button class="filter-btn" onclick="filterShowcase('Tablets')">Tablets</button>
                <button class="filter-btn" onclick="filterShowcase('Tech Accessories')">Tech Accessories</button>
                <button class="filter-btn" onclick="filterShowcase('Vape Kits')">Vape Kits</button>
                <button class="filter-btn" onclick="filterShowcase('Vape Refills')">Vape Refills</button>
            </div>
            
            <div class="showcase-grid grid-cols-1 md:grid-cols-3 xl:grid-cols-4">
    '''
    for p in PRODUCTS:
        category = p["category"]
        title = p["title"]
        specs = p["specs"]
        price = p["price"]
        img_file = p["image_file"]
        
        # Check for flavours button
        flavours = p.get("flavours", [])
        flavours_btn = ""
        if flavours:
            escaped_title = title.replace("'", "\\'")
            # Format as a valid JS array of single-quoted strings to prevent HTML conflicts
            flavours_json = "[" + ", ".join(f"'{f.replace("'", "\\'")}'" for f in flavours) + "]"
            # Create a clean clickable button
            flavours_btn = f'''
            <button class="btn btn-secondary product-cta-btn" onclick="openFlavoursModal('{escaped_title}', {flavours_json})" style="margin-top: 10px; background-color: var(--bg-alternate); border: 1px solid var(--border-color); color: var(--text-main); font-weight: 600; font-size: 0.8rem; cursor: pointer; transition: background-color 0.2s ease, transform 0.15s ease;">
                <i class="fa-solid fa-list"></i> View Flavours
            </button>
            '''
            
        if price == "In stock":
            price_html = '<span class="contact-price">In stock</span>'
        else:
            price_html = f'<span class="base-price">{price}</span>'
            
        html += f'''
            <div class="product-card reveal" data-category="{category}">
                <div class="product-image-wrapper">
                    <img src="Fast acsess images/{img_file}" alt="{title}" class="product-image" loading="lazy">
                    <span class="product-category-badge">{category}</span>
                </div>
                <div class="product-details">
                    <h4 class="product-title">{title}</h4>
                    <p class="product-specs">{specs}</p>
                    <div class="product-price-row">
                        {price_html}
                    </div>
                    {flavours_btn}
                </div>
            </div>
        '''
        
    html += '''
            </div>
        </div>
    </section>
    '''
    return html

REVIEWS = [
    {
        "author": "Raphael Mariñas",
        "text": "I had a blast experience, and also they are so friendly and fantastic service, everything you need Electronic and vapes also computer etc. Is right here. If you're regular customer, you will know how exclusive you are give them full star cause for their effort of working your devices and remarkables price. If i can give them 1 million stars i will 🤣🤩",
        "rating": "5/5"
    },
    {
        "author": "Tahera",
        "text": "We had a great experience at this internet cafe. The staff were incredibly helpful, understanding, and went out of their way to assist us. They were honest and trustworthy, which made our visit even more pleasant. We highly recommend this place for anyone looking for reliable and friendly service",
        "rating": "5/5"
    },
    {
        "author": "Danny Steenkamp",
        "text": "Very polite, friendly service. Wanted a battery changed on my p30 pro. The battery ordered had less charge than my original. The honest statement means I'll be back",
        "rating": "5/5"
    },
    {
        "author": "Gemma Bridgman",
        "text": "Five stars for speed of service, honesty & integrity. Unfortunately I cannot comment on quality of service since my laptop cannot be repaired (the cost of repair isn't worth it for the laptop) but at least I know. I'll go back to Praem in future.",
        "rating": "5/5"
    },
    {
        "author": "Grim Show",
        "text": "Experienced smooth and easy collaboration with Mack while he was helping fixing my Mac. Prompt and efficient communication. Would recommend to anyone who wants to have their repair done quick and effective",
        "rating": "5/5"
    },
    {
        "author": "Vaildina Fernandes",
        "text": "Kind people. Always ready to help. Afordable and cheapest shop, with latest cellphones, internet services, printouts, also for passport photos. Must visit if you have document related work. Thanks!",
        "rating": "5/5"
    },
    {
        "author": "Jemima Kiranda",
        "text": "Really amazing service customer care was amazing especially by Mack he was so kind and briefed me on how to look after the alternations he made to my phone. I definitely recommend him 100% - Jemimah",
        "rating": "5/5"
    },
    {
        "author": "nikhil nikalai",
        "text": "Great customer service, I came here for Indian passport photo their price is very reasonable also very helpfull when I was applying for a visa.",
        "rating": "5/5"
    },
    {
        "author": "Jashanpreet Kaur",
        "text": "Best customer service, especially mack he's very friendly, very good price and all the digital products available easily accessible in high street. 👍👍👍",
        "rating": "5/5"
    },
    {
        "author": "Katie Shacklady",
        "text": "Had an amazing experience, brought it my MacBook asking for a used screen they had none available so replaced my new one at the same price as I needed it ASAP, can not thank them enough - would recommended to anyone in need of a fix !",
        "rating": "5/5"
    },
    {
        "author": "megan",
        "text": "Very friendly and welcoming staff. Great services and products available at good prices",
        "rating": "5/5"
    },
    {
        "author": "Severn Gems",
        "text": "This shop has a huge range of e-cigarettes with great deals on them. Amazing customer service! A good range of mobile phone accessories here too.",
        "rating": "5/5"
    },
    {
        "author": "Sultan Said",
        "text": "Amazing pair of lads. Came in and gave nothing but transparency and honesty when it came to fixing my phone. Appreciate such professionalism especially when many places aren't capable of performing professional jobs.",
        "rating": "5/5"
    },
    {
        "author": "Rochelle Mccammon",
        "text": "Very nice people. Clean shop, service with a smile... always 😊 Mac, brilliant! Will definitely come back as he's such a big help",
        "rating": "5/5"
    },
    {
        "author": "Dionne phipps",
        "text": "Good services and prices are cheap and affordable,Orem and Mack is good in services with phones,, iPods, computers etc. Overall they provided excellent services and are very helpful every time I go there. Thanks so much Dionne",
        "rating": "5/5"
    },
    {
        "author": "Shay Gaul",
        "text": "I came here for vape and Mack has given me a very nice vape machine and some juice, he is very experienced and well spoken. Highly recommend places especially in Hounslow area",
        "rating": "5/5"
    },
    {
        "author": "Annabelle Abreu",
        "text": "Amazing Customer Service, especially from Mack, He was such a gentleman and very informative - Great time management 10/10 service , would recommend to a friend 👍",
        "rating": "5/5"
    },
    {
        "author": "RAMU DANDA",
        "text": "Great customer service very well behaved and soft spoken, my mobile was not turning on they have done something and turned it on and didn't charge me anything as they said it's a common problem, I'm very pleased and they are very honest, highly recommended",
        "rating": "5/5"
    },
    {
        "author": "Rakesh Bollam",
        "text": "This is just not a print shop, they are helping you on anything they knew it, very helpful always polite and smile on their face, specially Mack and Sai. Hounslow is blessed to have this shop. Best of luck",
        "rating": "5/5"
    },
    {
        "author": "Lauren B",
        "text": "Always come in to buy elf bars they're the only shop to have my favourite flavours. Happy to always be served by Mike :) thanks from Lauren Burr",
        "rating": "5/5"
    },
    {
        "author": "John Ryan",
        "text": "Love having this shop in our neighbourhood! The guy is super friendly and always ready to help whether it's fixing a cracked screen, setting up a new phone, or finding the right accessories. Prices are fair, service is quick, and you can really tell they care about their customers. So nice to have a reliable local spot for all our mobile needs — highly recommend checking them out!",
        "rating": "5/5"
    },
    {
        "author": "John Blake",
        "text": "Hands down the best vape store in the area. The customer service is top notch. They always have the latest vapes and their flavours in stock. Both of the brothers are super friendly and always willing to help you find the best and right mod or juices. Also the prices are amazing and also have the best atmosphere. Highly recommend this store",
        "rating": "5/5"
    },
    {
        "author": "Diana Sima",
        "text": "Super helpful and genuinely kind. He checked my phone, explained everything clearly, and gave me an honest estimate of its value even though I didn't end up buying anything. Took the time to help without any pressure at all. Rare to find someone this professional and fair. Highly recommend.",
        "rating": "5/5"
    }
]

reviews_slides_html = ""
reviews_dots_html = ""
for idx, r in enumerate(REVIEWS):
    active_class = " active" if idx == 0 else ""
    escaped_text = r["text"].replace('"', '\\"')
    reviews_slides_html += f'''
                    <div class="review-slide{active_class}">
                        <p class="review-text">"{escaped_text}"</p>
                        <div class="review-author">
                            <span>{r["author"]}</span>
                            <span class="stars"><i class="fa-solid fa-star"></i> {r["rating"]}</span>
                        </div>
                    </div>'''
    reviews_dots_html += f'<span class="dot{active_class}" onclick="currentSlide({idx})"></span>'

index_content = get_header("Fast Access Print, Vape and Repair", "Hounslow's primary printing, cyber cafe, vape shop, and expert device repair store. Serving High Street for 25 years. Document printing from £1. Genuine parts.", is_home=True) + '''
    <!-- Hero Section -->
    <section class="hero" style="background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.95)), url('printing-service.jpg');">
        <div class="container hero-grid">
            <div class="hero-content reveal">
                <span class="eyebrow"><i class="fa-solid fa-shop"></i> ESTABLISHED 25 YEARS | HOUNSLOW HIGH STREET</span>
                <h1>
                    <span class="hero-title-line-1">Print, repair, connect.</span>
                    <span class="hero-title-line-2">On the High Street since 2001.</span>
                </h1>
                <p class="hero-tagline">Hounslow's trusted digital hub since 2001 — professional A4–A5 document printing from £1, government-compliant passport photos, high-speed internet cafe access, and expert phone and laptop repairs using 100% genuine parts.</p>
                <div class="hero-btns">
                    <a href="documentprinting" class="btn btn-primary"><i class="fa-solid fa-print"></i> Document printing &mdash; from &pound;1</a>
                    <a href="tel:07466540111" class="btn btn-outline"><i class="fa-solid fa-phone"></i> Call Fast Access</a>
                </div>
                <div class="hero-trust-strip">
                    <div class="trust-item">
                        <i class="fa-solid fa-print"></i>
                        <span>Instant Print and Copy</span>
                    </div>
                    <div class="trust-divider"></div>
                    <div class="trust-item">
                        <i class="fa-solid fa-camera"></i>
                        <span>Compliant Passport Photos</span>
                    </div>
                    <div class="trust-divider"></div>
                    <div class="trust-item">
                        <i class="fa-solid fa-shield-halved"></i>
                        <span>100% Genuine Parts</span>
                    </div>
                    <div class="trust-divider"></div>
                    <div class="trust-item">
                        <i class="fa-solid fa-cloud-arrow-up"></i>
                        <span>Vapes and E-Liquids</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="services" id="services">
        <div class="container">
            <div class="section-header text-center reveal">
                <h2>Our Services and Products</h2>
                <p class="subheading">Professional printing, biometric photos, internet terminal access, and tech repair services.</p>
                <div class="accent-divider"></div>
            </div>
            
            <!-- Printing & Cafe Section -->
            <h3 class="services-category-title reveal"><i class="fa-solid fa-print"></i> Professional Print and Cafe Services</h3>
            <div class="services-grid-2 reveal" style="margin-bottom: 50px;">
                <!-- Document Printing -->
                <a href="documentprinting" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('printing-service.jpg');">
                        <div class="card-content">
                            <span class="service-badge"><i class="fa-solid fa-fire"></i> Primary Service</span>
                            <h3>Document Printing &amp; Duplication</h3>
                            <p>High-quality A4 and A5 black &amp; white or color prints. First page £1.00.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                        </div>
                    </div>
                </a>
                <!-- Internet Cafe -->
                <a href="internetcafe" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('internet-cafe.jpg');">
                        <div class="card-content">
                            <h3>High-Speed Internet Cafe</h3>
                            <p>Computer terminal access, high-resolution scanning, and emailing services.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                    </div>
                </a>
            </div>

            <!-- Vape & E-Liquids Showcase Section -->
            <h3 class="services-category-title reveal"><i class="fa-solid fa-cloud-arrow-up"></i> Premium Vapes &amp; E-Liquids</h3>
            <div class="vapes-home-showcase reveal" style="margin-bottom: 50px; background: var(--bg-alternate); border: 1px solid var(--border-color); border-radius: 12px; overflow: hidden;">
                <div style="display: grid; grid-template-columns: 1fr 1.2fr; min-height: 380px;">
                    <a href="catalogue.html?category=Vape+Kits" style="background-color: #ffffff; display: flex; align-items: center; justify-content: center; padding: 30px; min-height: 250px; border-right: 1px solid var(--border-color); text-decoration: none;">
                        <img src="Fast acsess images/Geekvape Aegis Kit.jpg" alt="Premium Vapes &amp; E-Liquids" style="max-width: 100%; max-height: 320px; object-fit: contain; transition: transform 0.3s ease;" class="vape-hover-img">
                    </a>
                    <div style="padding: 40px; display: flex; flex-direction: column; justify-content: center;">
                        <span class="service-badge" style="width: fit-content; margin-bottom: 12px;"><i class="fa-solid fa-star"></i> In Stock Now</span>
                        <h4 style="font-size: 1.8rem; margin-bottom: 15px; font-weight: 800; font-family: var(--font-heading); color: var(--text-main);">Disposables, Pods &amp; E-Liquids</h4>
                        <p style="color: var(--text-muted); margin-bottom: 25px; line-height: 1.7; font-size: 1rem;">
                            We carry Hounslow's most complete range of premium disposable vapes, closed pod kits, coils, e-liquids, and nicotine pouches. 
                            Stocking authentic brands: <strong>Lost Mary</strong>, <strong>Elf Bar</strong>, <strong>SKE Crystal</strong>, <strong>Hayati Pro Max</strong>, <strong>IVG</strong>, <strong>Velo</strong>, <strong>Nordic Spirit</strong>, and <strong>ZYN</strong>.
                        </p>
                        <div class="vape-btns">
                            <a href="catalogue.html?category=Vape+Kits" class="btn btn-primary"><i class="fa-solid fa-basket-shopping"></i> Browse Vapes</a>
                            <a href="contact.html?product=Vape+Stock+Enquiry" class="btn btn-outline"><i class="fa-solid fa-envelope"></i> Stock Enquiry</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <style>
                .vape-btns {
                    display: flex;
                    gap: 15px;
                    margin-top: 15px;
                }
                .vape-hover-img:hover {
                    transform: scale(1.05);
                }
                @media (max-width: 768px) {
                    .vapes-home-showcase > div {
                        grid-template-columns: 1fr !important;
                    }
                    .vapes-home-showcase > div > a {
                        border-right: none !important;
                        border-bottom: 1px solid var(--border-color);
                        height: 250px;
                        padding: 20px !important;
                    }
                    .vapes-home-showcase > div > div:last-child {
                        padding: 24px !important;
                    }
                    .vape-btns {
                        flex-direction: column;
                        width: 100%;
                    }
                    .vape-btns .btn {
                        width: 100%;
                        text-align: center;
                        justify-content: center;
                    }
                }
            </style>

            <!-- Phone Repair Subsection -->
            <h3 class="services-category-title reveal"><i class="fa-solid fa-mobile-screen"></i> Phone Repair Services</h3>
            <div class="services-grid reveal" style="margin-bottom: 50px;">
                <!-- Phone Screen Repair -->
                <a href="screenrepair" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('cracked-screen.jpg');">
                        <div class="card-content">
                            <h3>Phone Screen Repair</h3>
                            <p>Smashed displays, unresponsive digitizers &amp; bleeding LEDs replaced with genuine parts.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                        </div>
                    </div>
                </a>
                
                <!-- Phone Battery Replacement -->
                <a href="batteryreplacement" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('battery-repair.jpg');">
                        <div class="card-content">
                            <h3>Phone Battery Replacement</h3>
                            <p>Fast drain or swollen batteries swapped out for brand new genuine cells.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                        </div>
                    </div>
                </a>
                
                <!-- Phone Charging Port -->
                <a href="chargingport" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('charging-port.jpg');">
                        <div class="card-content">
                            <h3>Charging Port Repair</h3>
                            <p>Loose connection or dead charging port sockets fixed.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                        </div>
                    </div>
                </a>
                
                <!-- Phone Unlocking -->
                <a href="phoneunlocking" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('unlock-phone.jpg');">
                        <div class="card-content">
                            <h3>Phone Unlocking</h3>
                            <p>Remove network restrictions and use any SIM card worldwide.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                        </div>
                    </div>
                </a>
            </div>

            <!-- Laptop Repair Subsection -->
            <h3 class="services-category-title reveal"><i class="fa-solid fa-laptop"></i> Laptop &amp; Computer Repairs</h3>
            <div class="services-grid reveal">
                <!-- Laptop Screen Repair -->
                <a href="laptopscreen" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('laptop-broken-screen.jpg');">
                        <div class="card-content">
                            <h3>Laptop Screen Repair</h3>
                            <p>Smashed laptop panels &amp; bleeding LED displays replaced.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                        </div>
                    </div>
                </a>
                
                <!-- Performance & Upgrades -->
                <a href="slowperformance" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('laptop-slow-computer.jpg');">
                        <div class="card-content">
                            <h3>Performance Tuneups</h3>
                            <p>Speed up slow bootups, clean cache files, and apply thermal paste.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                        </div>
                    </div>
                </a>
                
                <!-- Liquid Spill Recovery -->
                <a href="liquidspill" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('laptop-water-damage.jpg');">
                        <div class="card-content">
                            <h3>Liquid Spill Recovery</h3>
                            <p>Decontaminate corrosion in logic boards and repair trace lines.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                        </div>
                    </div>
                </a>

                <!-- SSD & RAM Upgrade -->
                <a href="ramstorage" class="service-card-link">
                    <div class="service-card" style="background-image: linear-gradient(rgba(17, 17, 17, 0.45), rgba(17, 17, 17, 0.75)), url('laptop-ram-upgrade.jpg');">
                        <div class="card-content">
                            <h3>SSD and RAM Upgrades</h3>
                            <p>Restores performance and upgrades storage capacities safely.</p>
                            <span class="learn-more">Learn More &rarr;</span>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <!-- Country Marquee -->
    <section class="country-marquee-section">
        <div class="container">
            <div class="section-header text-center reveal" style="margin-bottom: 20px;">
                <span class="section-subtitle">Global Coverage</span>
                <h2>Biometric Passport Photos For All Countries</h2>
                <div class="accent-divider"></div>
            </div>
            <div class="marquee-wrapper reveal">
                <div class="marquee-content">
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/gb.png" width="20" alt="UK Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> United Kingdom (HMPO)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/us.png" width="20" alt="US Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> United States (Visa and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/eu.png" width="20" alt="EU Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Schengen Area / EU Visa</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/in.png" width="20" alt="India Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> India (OCI and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ca.png" width="20" alt="Canada Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Canada (Visa and ID)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/au.png" width="20" alt="Australia Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Australia</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/pk.png" width="20" alt="Pakistan Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Pakistan (NICOP and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ng.png" width="20" alt="Nigeria Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Nigeria</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/bd.png" width="20" alt="Bangladesh Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Bangladesh</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/cn.png" width="20" alt="China Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> China</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/jm.png" width="20" alt="Jamaica Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Jamaica</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/za.png" width="20" alt="South Africa Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> South Africa</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/gh.png" width="20" alt="Ghana Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Ghana</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ph.png" width="20" alt="Philippines Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Philippines</div>
                    <!-- Repeat for seamless scrolling -->
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/gb.png" width="20" alt="UK Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> United Kingdom (HMPO)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/us.png" width="20" alt="US Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> United States (Visa and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/eu.png" width="20" alt="EU Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Schengen Area / EU Visa</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/in.png" width="20" alt="India Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> India (OCI and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ca.png" width="20" alt="Canada Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Canada (Visa and ID)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/au.png" width="20" alt="Australia Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Australia</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/pk.png" width="20" alt="Pakistan Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Pakistan (NICOP and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ng.png" width="20" alt="Nigeria Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Nigeria</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/bd.png" width="20" alt="Bangladesh Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Bangladesh</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/cn.png" width="20" alt="China Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> China</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/jm.png" width="20" alt="Jamaica Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Jamaica</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/za.png" width="20" alt="South Africa Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> South Africa</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/gh.png" width="20" alt="Ghana Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Ghana</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ph.png" width="20" alt="Philippines Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Philippines</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Passport Photo Feature Section -->
    <section class="passport-photo-home-section" style="padding: 60px 0; background: var(--bg-card); border-top: none; border-bottom: 1px solid var(--border-color);">
        <div class="container details-grid">
            <div class="details-text reveal">
                <span class="section-subtitle" style="display: block; margin-bottom: 8px;">Capture &amp; Print</span>
                <h2 style="font-size: 2.2rem; margin-bottom: 15px;">Biometric Passport Photos</h2>
                <p style="margin-bottom: 20px; font-size: 1.05rem; line-height: 1.7;">Get professional, government-compliant passport, visa, and ID photos captured instantly in our Hounslow store. We support specifications for all countries including UK HMPO, US, EU, Canada, India, and China. Ready in 5 minutes with a 100% compliance guarantee.</p>
                <div class="symptoms-box" style="margin-bottom: 25px;">
                    <ul class="symptoms-list">
                        <li><i class="fa-solid fa-circle-check"></i> <strong>HMPO Digital Codes:</strong> Get UK digital passport photo codes instantly.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>Guaranteed Biometrics:</strong> Taken using professional lighting and backdrops.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>Instant Turnaround:</strong> Capture, validation, and printing in under 5 minutes.</li>
                    </ul>
                </div>
                <a href="passportphotos" class="btn btn-primary"><i class="fa-solid fa-camera"></i> View Specifications</a>
            </div>
            <div class="details-image reveal">
                <img src="passport-photo.jpg" alt="Biometric photo setup" class="in-process-img">
            </div>
        </div>
    </section>

    <!-- Booking Form Section -->
    <section class="booking-section" id="book-now">
        <div class="container booking-grid">
            <div class="booking-info reveal">
                <span class="section-subtitle">Enquiries</span>
                <h2>Request a Service or Print Submission</h2>
                <p>Submit your document printing requests (first page is £1.00), passport photo enquiries, cyber cafe terminal bookings, or tech repair consultations. Fill in the form and we'll get back to you immediately.</p>
                
                <div class="contact-bullets">
                    <div class="bullet-item">
                        <i class="fa-solid fa-circle-check"></i>
                        <div>
                            <strong>Document Printing and Copying</strong>
                            <p>Upload/email files to fastinternetaccess@gmail.com for instant pickup (first page is £1.00).</p>
                        </div>
                    </div>
                    <div class="bullet-item">
                        <i class="fa-solid fa-circle-check"></i>
                        <div>
                            <strong>Government Compliant Passport Photos</strong>
                            <p>High-quality lighting setup compliant with international guidelines.</p>
                        </div>
                    </div>
                    <div class="bullet-item">
                        <i class="fa-solid fa-circle-check"></i>
                        <div>
                            <strong>100% Genuine Parts Policy</strong>
                            <p>We use 100% certified genuine components for all repairs.</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="booking-form-wrapper reveal">
                <form class="native-booking-form" onsubmit="return handleBookingSubmit(event)">
                    <div class="form-group">
                        <label for="clientName">Your Name</label>
                        <input type="text" id="clientName" required placeholder="e.g., Sahil Ahmadi">
                    </div>
                    <div class="form-group">
                        <label for="clientPhone">Phone Number</label>
                        <input type="tel" id="clientPhone" required placeholder="e.g., 07123 456789">
                    </div>
                    <div class="form-group-grid">
                        <div class="form-group">
                            <label for="deviceModel">Device model or printing details</label>
                            <input type="text" id="deviceModel" placeholder="e.g., iPhone 11, or A4 PDF Print">
                        </div>
                        <div class="form-group">
                            <label for="serviceType">Required Option</label>
                            <select id="serviceType" required>
                                <option value="" disabled selected>Select option...</option>
                                <option value="printing">Document Printing and Copying (First page £1.00)</option>
                                <option value="passport">Passport Photos (All Countries)</option>
                                <option value="cafe">Internet Cafe Terminal Access</option>
                                <option value="consultation">Free Tech Consultation</option>
                                <option value="screen">Phone Screen Repair</option>
                                <option value="battery">Phone Battery Replacement</option>
                                <option value="water">Phone Water Damage Repair</option>
                                <option value="port">Phone Charging Port Repair</option>
                                <option value="unlocking">Phone Unlocking</option>
                                <option value="laptop-screen">Laptop Screen Repair</option>
                                <option value="laptop-perf">Laptop Performance Tuneup</option>
                                <option value="laptop-virus">Laptop Virus &amp; Malware</option>
                                <option value="laptop-data">Laptop Data Recovery</option>
                                <option value="laptop-ram">Laptop SSD and RAM Upgrade</option>
                                <option value="laptop-keys">Laptop Keyboard and Ports</option>
                                <option value="laptop-spill">Laptop Liquid Spill Recovery</option>
                                <option value="laptop-power">Laptop Power and Battery</option>
                                <option value="vape">Vape / Pouches Stock Enquiry</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Preferred Action</label>
                        <div class="radio-group">
                            <label class="radio-label">
                                <input type="radio" name="deliveryOption" value="dropoff" checked>
                                <span>Visit Shop In Person</span>
                            </label>
                            <label class="radio-label">
                                <input type="radio" name="deliveryOption" value="phone">
                                <span>Get Advice Call / Quote</span>
                            </label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="issueDetails">Describe what you need printed or repaired</label>
                        <textarea id="issueDetails" rows="4" placeholder="e.g., I need 10 A4 pages printed black & white..."></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary w-100"><i class="fa-solid fa-paper-plane"></i> Send Enquiry</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Why Us Section -->
    <section class="why-us">
        <div class="container">
            <div class="section-header text-center reveal">
                <h2>Why Choose Fast Access?</h2>
                <div class="accent-divider"></div>
            </div>
            
            <div class="why-us-grid reveal">
                <div class="why-card">
                    <div class="why-icon"><i class="fa-solid fa-clock-rotate-left"></i></div>
                    <h3>25 Years of Service</h3>
                    <p>Established on Hounslow High Street in 2001. We have provided trusted digital services for 25 years.</p>
                </div>
                <div class="why-card">
                    <div class="why-icon"><i class="fa-solid fa-shield-halved"></i></div>
                    <h3>Everything Genuine</h3>
                    <p>No cheap knock-offs. We use 100% genuine components for device repairs and authentic materials for our prints.</p>
                </div>
                <div class="why-card">
                    <div class="why-icon"><i class="fa-solid fa-print"></i></div>
                    <h3>Professional Printing Hub</h3>
                    <p>Equipped with high-speed machinery for A4 and A5 prints, plus laminating &amp; biometric photography.</p>
                </div>
            </div>
        </div>
    </section>
    

    
    <!-- Catalogue Showcase Section -->
    <section class="phones-teaser">
        <div class="container phones-teaser-grid">
            <div class="phones-teaser-content reveal">
                <span class="section-subtitle">Our Store Stock</span>
                <h2>Vapes, Tech Products and More</h2>
                <p>We stock a massive, handpicked inventory of the latest smart devices, premium disposable vape kits, closed pod refills, nicotine pouches, and essential tech accessories. Visit us in-store at 80 High St, Hounslow to view our full stock.</p>
                <a href="catalogue" class="btn btn-primary">Browse Full Catalogue &rarr;</a>
            </div>
            <div class="phone-anchors-grid reveal">
                <!-- Representative 1: Vapes & Pods -->
                <div class="phone-item-card">
                    <img loading="lazy" src="Fast acsess images/blog_big_puff_vapes.webp" alt="Premium Vapes &amp; Pods">
                    <span>Vapes &amp; Pods</span>
                </div>
                <!-- Representative 2: Smartphones -->
                <div class="phone-item-card">
                    <img loading="lazy" src="Fast acsess images/blog_premium_upgrades.webp" alt="Smartphones">
                    <span>Smartphones</span>
                </div>
                <!-- Representative 3: Nicotine Pouches -->
                <div class="phone-item-card">
                    <img loading="lazy" src="Fast acsess images/blog_nicotine_pouches.webp" alt="Nicotine Pouches">
                    <span>Nicotine Pouches</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Reviews Section -->
    <section class="reviews">
        <div class="container">
            <div class="section-header text-center reveal">
                <span class="section-subtitle">Testimonials</span>
                <h2>What Our Customers Say</h2>
                <p class="subheading">Read reviews from real customers who visit our Hounslow store.</p>
                <div class="accent-divider"></div>
            </div>
            
            <div class="reviews-slider-container reveal">
                <div class="reviews-wrapper" id="reviewsWrapper">
''' + reviews_slides_html + '''
                </div>
                
                <div class="slider-dots" id="sliderDots">
''' + reviews_dots_html + '''
                </div>
            </div>
        </div>
    </section>

    <!-- Final CTA -->
    <section class="final-cta text-center reveal" style="background-image: linear-gradient(rgba(17, 17, 17, 0.75), rgba(17, 17, 17, 0.85)), url('printing-service.jpg');">
        <div class="container">
            <h2>Need Quick Printing, Internet Access or Device Repairs?</h2>
            <p>Visit us at 80 High St, Hounslow, TW3 1NH, or call us for pricing and stock information.</p>
            <a href="tel:07466540111" class="btn btn-primary btn-large"><i class="fa-solid fa-phone"></i> Call Fast Access</a>
        </div>
    </section>
''' + get_footer()

with open(os.path.join(dest_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)
print("index.html written.")


# ----------------- Write catalogue.html -----------------
catalogue_content = get_header("Product Catalogue", "Browse our full in-store stock of smartphones, vapes, nicotine pouches, and accessories.") + get_catalogue_page_html() + get_footer()
with open(os.path.join(dest_dir, "catalogue.html"), "w", encoding="utf-8") as f:
    f.write(catalogue_content)
print("catalogue.html written.")

# ----------------- Write vapes-pouches.html (Redirect) -----------------
vapes_redirect = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=catalogue.html?category=Vape+Kits">
    <script type="text/javascript">
        window.location.href = "catalogue.html?category=Vape+Kits";
    </script>
    <title>Redirecting...</title>
</head>
<body>
    <p>If you are not redirected, <a href="catalogue.html?category=Vape+Kits">click here</a>.</p>
</body>
</html>"""

with open(os.path.join(dest_dir, "vapespouches.html"), "w", encoding="utf-8") as f:
    f.write(vapes_redirect)
print("vapes-pouches.html written (redirect).")


# ----------------- Write phones-in-store.html (Redirect) -----------------
phones_redirect = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=catalogue.html?category=Smartphones">
    <script type="text/javascript">
        window.location.href = "catalogue.html?category=Smartphones";
    </script>
    <title>Redirecting...</title>
</head>
<body>
    <p>If you are not redirected, <a href="catalogue.html?category=Smartphones">click here</a>.</p>
</body>
</html>"""

with open(os.path.join(dest_dir, "phonesinstore.html"), "w", encoding="utf-8") as f:
    f.write(phones_redirect)
print("phones-in-store.html written (redirect).")

# ----------------- Write contact.html -----------------
contact_content = get_header("Contact Us", "Visit our store at 80 High St, Hounslow, or request a printing, internet cafe, or device repair appointment online.") + '''
    <!-- Page Hero -->
    <section class="page-hero text-center reveal">
        <div class="container">
            <h1>Contact Us</h1>
            <p>Drop off your device, print documents, use our cyber cafe, or get biometric passport photos at our Hounslow High Street shop.</p>
        </div>
    </section>

    <!-- Info & Booking Section -->
    <section class="contact-details-section">
        <div class="container contact-grid-page">
            <div class="contact-left-info reveal">
                <h2>Fast Access &amp; Repairs</h2>
                <p>Hounslow's premium digital services and tech repair shop. Serving the community with integrity for 25 years.</p>
                <p class="phone-large" style="margin-top: 15px;"><i class="fa-solid fa-phone"></i> <a href="tel:07466540111">07466 540111</a></p>
                <p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 25px;">
                    <i class="fa-solid fa-envelope" style="color: var(--primary); margin-right: 8px;"></i>
                    <a href="mailto:fastinternetaccess@gmail.com" style="color: var(--primary); text-decoration: none; font-weight: 600;">fastinternetaccess@gmail.com</a>
                </p>
                
                <div class="hours-box">
                    <h3><i class="fa-solid fa-clock"></i> Shop Hours</h3>
                    <table class="contact-hours-table">
                        <tbody>
                            <tr><td>Monday</td><td>9:00 am &ndash; 8:00 pm</td></tr>
                            <tr><td>Tuesday</td><td>9:00 am &ndash; 8:00 pm</td></tr>
                            <tr><td>Wednesday</td><td>9:00 am &ndash; 8:00 pm</td></tr>
                            <tr><td>Thursday</td><td>9:00 am &ndash; 8:00 pm</td></tr>
                            <tr><td>Friday</td><td>9:00 am &ndash; 8:00 pm</td></tr>
                            <tr><td>Saturday</td><td>9:00 am &ndash; 8:00 pm</td></tr>
                            <tr><td>Sunday</td><td>10:00 am &ndash; 7:00 pm</td></tr>
                        </tbody>
                    </table>
                </div>
                
                <!-- Google Maps Embed -->
                <div class="contact-map-wrapper">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2484.3412586737525!2d-0.3664057238525049!3d51.469324012217646!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48760cdbf6c8f9db%3A0x8d5c4ffb7b12d7c5!2s80%20High%20St%2C%20Hounslow%20TW3%201NH!5e0!3m2!1sen!2suk!4v1718389750000!5m2!1sen!2suk" width="100%" height="280" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
                </div>
            </div>
            
            <div class="booking-form-wrapper reveal">
                <h3>Request Repair / Printing Stock check</h3>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 20px;">Fill in your details and we will get back to you shortly.</p>
                <form class="native-booking-form" onsubmit="return handleBookingSubmit(event)">
                    <div class="form-group">
                        <label for="contactName">Your Name</label>
                        <input type="text" id="contactName" required placeholder="Name">
                    </div>
                    <div class="form-group">
                        <label for="contactPhone">Phone Number</label>
                        <input type="tel" id="contactPhone" required placeholder="Phone">
                    </div>
                    <div class="form-group">
                        <label for="contactService">Options / Service</label>
                        <select id="contactService" required>
                            <option value="" disabled selected>Select service...</option>
                            <option value="printing">Document Printing and Copying (First page £1.00)</option>
                            <option value="passport">Passport Photos (All Countries)</option>
                            <option value="cafe">Internet Cafe Terminal Access</option>
                            <option value="consultation">Free Consultation</option>
                            <option value="screen">Phone Screen Repair</option>
                            <option value="battery">Phone Battery Replacement</option>
                            <option value="water">Phone Water Damage Repair</option>
                            <option value="port">Phone Charging Port Repair</option>
                            <option value="unlocking">Phone Unlocking</option>
                            <option value="laptop-screen">Laptop Screen Repair</option>
                            <option value="laptop-perf">Laptop Performance Tuneup</option>
                            <option value="laptop-virus">Laptop Virus &amp; Malware</option>
                            <option value="laptop-data">Laptop Data Recovery</option>
                            <option value="laptop-ram">Laptop SSD and RAM Upgrade</option>
                            <option value="laptop-keys">Laptop Keyboard and Ports</option>
                            <option value="laptop-spill">Laptop Liquid Spill Recovery</option>
                            <option value="laptop-power">Laptop Power and Battery</option>
                            <option value="vapes">Vapes / Pouches Enquiry</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Preferred Action</label>
                        <div class="radio-group">
                            <label class="radio-label">
                                <input type="radio" name="contactDelivery" value="dropoff" checked>
                                <span>Drop-Off Shop Visit</span>
                            </label>
                            <label class="radio-label">
                                <input type="radio" name="contactDelivery" value="call">
                                <span>Free advice call consultation</span>
                            </label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="contactDetails">Provide file names to print or describe issue</label>
                        <textarea id="contactDetails" rows="4" placeholder="Describe details..."></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary w-100"><i class="fa-solid fa-calendar-check"></i> Submit Request</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Storefront Exterior Section -->
    <section class="contact-images-section">
        <div class="container text-center reveal">
            <div class="contact-image-container">
                <img src="exterior.webp" alt="Fast Access Shop Front Exterior" onclick="openLightbox('exterior.webp', 'Storefront Exterior - 80 High St, Hounslow')">
                <p class="contact-image-caption">Our storefront exterior at 80 High St, Hounslow, TW3 1NH</p>
            </div>
        </div>
    </section>
''' + get_footer()

with open(os.path.join(dest_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_content)
print("contact.html written.")


# ----------------- Write Document Printing Page -----------------
printing_content = get_header("Document Printing and Copying", "High-speed A4 and A5 document printing, duplicating, lamination, and photocopying in Hounslow. First page £1.00.") + '''
    <!-- Page Hero -->
    <section class="service-hero" style="background-image: linear-gradient(rgba(17, 17, 17, 0.65), rgba(17, 17, 17, 0.85)), url('printing-service.jpg');">
        <div class="container text-center reveal">
            <h1>Document Printing and Copying</h1>
            <p>Professional document printing and duplication services. A4 and A5 sizing. Lamination available.</p>
            <a href="mailto:fastinternetaccess@gmail.com" class="btn btn-primary"><i class="fa-solid fa-envelope"></i> Email Files to Print</a>
        </div>
    </section>

    <!-- Printing Details -->
    <section class="service-details">
        <div class="container details-grid">
            <div class="details-text reveal">
                <h2>Fast, High-Quality Prints and Copying</h2>
                <p>We provide instant, professional printing and copying services directly from your email or USB stick. Whether you need a single page copied, an official application printed, or promotional leaflets, we support multiple formats and page sizes with crystal-clear output.</p>
                
                <div class="symptoms-box">
                    <h3>Our Printing Offerings</h3>
                    <ul class="symptoms-list">
                        <li><i class="fa-solid fa-circle-check"></i> <strong>A4 Sizing:</strong> Standard document printing, CVs, flight tickets, and applications.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>A5 Sizing:</strong> Flyers, booklets, invoices, and menus.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>Lamination:</strong> Protect your A4 and A5 prints from moisture, dust, and tearing.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>First Page is £1.00:</strong> Standard document printing starts at £1.00 for the first page, subsequent pages are charged at standard rates.</li>
                    </ul>
                </div>
            </div>
            <div class="details-image reveal">
                <img src="printing-service.jpg" alt="Document printing press" class="in-process-img">
            </div>
        </div>
    </section>

    <!-- Pricing Section -->
    <section class="pricing-section">
        <div class="container">
            <div class="section-header text-center reveal">
                <span class="section-subtitle">Affordable rates</span>
                <h2>Our Printing and Scanning Prices</h2>
                <div class="accent-divider"></div>
            </div>
            
            <div class="pricing-grid reveal">
                <!-- Card 1: Print from Email -->
                <div class="pricing-card">
                    <h3><i class="fa-solid fa-envelope"></i> Print From Email</h3>
                    <p class="price-note">First page is standard £1.00 processing. Subsequent pages are priced as below:</p>
                    <div class="pricing-table-wrapper">
                        <table class="pricing-table">
                            <thead>
                                <tr>
                                    <th>Size and Option</th>
                                    <th>Price Per Side</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>A4 Black and White (B/W)</td>
                                    <td class="price-highlight">£0.20</td>
                                </tr>
                                <tr>
                                    <td>A3 Black and White (B/W)</td>
                                    <td class="price-highlight">£1.00</td>
                                </tr>
                                <tr>
                                    <td>A4 Colour</td>
                                    <td class="price-highlight">£1.00</td>
                                </tr>
                                <tr>
                                    <td>A3 Colour</td>
                                    <td class="price-highlight">£3.00</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <!-- Card 2: Scanning Services -->
                <div class="pricing-card">
                    <h3><i class="fa-solid fa-scanner"></i> Scanning Services</h3>
                    <p class="price-note">High-resolution digitizing of your physical documents to email or USB:</p>
                    <div class="pricing-table-wrapper">
                        <table class="pricing-table">
                            <thead>
                                <tr>
                                    <th>Size</th>
                                    <th>Price Per Side</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>A4 Document Scan</td>
                                    <td class="price-highlight">£0.50</td>
                                </tr>
                                <tr>
                                    <td>A3 Document Scan</td>
                                    <td class="price-highlight">£1.00</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Process Section -->
    <section class="process-section">
        <div class="container">
            <div class="section-header text-center reveal">
                <span class="section-subtitle">How it works</span>
                <h2>Our Printing and Copying Process</h2>
                <div class="accent-divider"></div>
            </div>
            
            <div class="process-grid reveal">
                <div class="process-step">
                    <div class="process-number">01</div>
                    <div class="process-icon"><i class="fa-solid fa-envelope-open-text"></i></div>
                    <h3>Submit Your Files</h3>
                    <p>Email your documents directly to <strong>fastinternetaccess@gmail.com</strong> or bring them on a USB flash drive to our Hounslow store.</p>
                </div>
                
                <div class="process-step">
                    <div class="process-number">02</div>
                    <div class="process-icon"><i class="fa-solid fa-sliders"></i></div>
                    <h3>Choose Sizing and Options</h3>
                    <p>Select A4 or A5 paper sizing, choose color or black &amp; white, and select finishing options like protective lamination.</p>
                </div>
                
                <div class="process-step">
                    <div class="process-number">03</div>
                    <div class="process-icon"><i class="fa-solid fa-print"></i></div>
                    <h3>Instant Production</h3>
                    <p>We output your documents instantly on our professional high-speed presses. (First page is £1.00, subsequent sides are charged at standard rates).</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Printing Standards Section -->
    <section class="compliance-badges-section">
        <div class="container">
            <div class="section-header text-center reveal" style="margin-bottom: 40px;">
                <span class="section-subtitle">Quality Standards</span>
                <h2>Why Print With Us?</h2>
                <div class="accent-divider"></div>
            </div>
            <div class="badges-grid-3 reveal">
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-scroll"></i></div>
                    <h3>Premium Quality Paper</h3>
                    <p>We print standard orders on high-opacity, thick premium white paper for a professional look and feel.</p>
                </div>
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-arrows-to-dot"></i></div>
                    <h3>Laser Precision Sizing</h3>
                    <p>Perfect registration and scaling for A4 and A5 dimensions, ensuring no cut-off margins.</p>
                </div>
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-clock-rotate-left"></i></div>
                    <h3>Same-Day Collection</h3>
                    <p>Walk in or send files ahead. We produce and laminate your documents in minutes while you wait.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="service-cta text-center reveal">
        <div class="container">
            <h2>Ready to Print Your Documents?</h2>
            <p>Send your PDF, Word doc, or images to <a href="mailto:fastinternetaccess@gmail.com" style="color: var(--primary); font-weight: 600;">fastinternetaccess@gmail.com</a> and we will prepare it for collection. (First page is £1.00).</p>
            <a href="mailto:fastinternetaccess@gmail.com" class="btn btn-primary"><i class="fa-solid fa-paper-plane"></i> Email fastinternetaccess@gmail.com</a>
        </div>
    </section>
''' + get_footer()

with open(os.path.join(dest_dir, "documentprinting.html"), "w", encoding="utf-8") as f:
    f.write(printing_content)
print("document-printing.html written.")


# ----------------- Write Passport Photos Page -----------------
passport_content = get_header("Passport Photos", "Government-compliant visa and passport photos for all countries captured instantly in Hounslow. Biometric standard guaranteed.") + '''
    <!-- Page Hero -->
    <section class="service-hero" style="background-image: linear-gradient(rgba(17, 17, 17, 0.35), rgba(17, 17, 17, 0.55)), url('passport-photo.jpg');">
        <div class="container text-center reveal">
            <h1>Biometric Passport Photos</h1>
            <p>100% government-compliant passport, visa, and ID photo capture for all countries. Ready in 5 minutes.</p>
            <a href="tel:07466540111" class="btn btn-primary"><i class="fa-solid fa-phone"></i> Call Fast Access</a>
        </div>
    </section>

    <!-- Photo Details -->
    <section class="service-details">
        <div class="container details-grid">
            <div class="details-text reveal">
                <h2>Guaranteed Biometric Approval</h2>
                <p>Avoid passport application rejections with our professional ID photo capture service. We use specialized lighting, proper backdrops, and advanced biometric compliance checks to verify your photos against official government requirements (including UK, US, EU, Canada, India, and China). We print them instantly on high-quality photographic paper or send them to you digitally.</p>
                
                <div class="symptoms-box" style="margin-bottom: 20px;">
                    <h3>Our Photo Specifications</h3>
                    <ul class="symptoms-list">
                        <li><i class="fa-solid fa-circle-check"></i> <strong>All Countries Supported:</strong> UK Passport, US Visa, Schengen Visa, India OCI, Canada Visa, and more.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>Government Compliant:</strong> Guaranteed to pass biometric verification checks.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>Digital Codes:</strong> UK digital passport photo codes provided.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>Instant Turnaround:</strong> Capture, verification, and high-quality printing done in under 5 minutes.</li>
                    </ul>
                </div>
            </div>
            <div class="details-image reveal">
                <img src="passport-photo.jpg" alt="Biometric photo setup" class="in-process-img">
            </div>
        </div>
    </section>

    <!-- Country Marquee -->
    <section class="country-marquee-section">
        <div class="container">
            <div class="section-header text-center reveal" style="margin-bottom: 20px;">
                <span class="section-subtitle">Global Coverage</span>
                <h2>Supported Passport and Visa Countries</h2>
                <div class="accent-divider"></div>
            </div>
            <div class="marquee-wrapper reveal">
                <div class="marquee-content">
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/gb.png" width="20" alt="UK Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> United Kingdom (HMPO)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/us.png" width="20" alt="US Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> United States (Visa and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/eu.png" width="20" alt="EU Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Schengen Area / EU Visa</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/in.png" width="20" alt="India Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> India (OCI and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ca.png" width="20" alt="Canada Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Canada (Visa and ID)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/au.png" width="20" alt="Australia Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Australia</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/pk.png" width="20" alt="Pakistan Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Pakistan (NICOP and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ng.png" width="20" alt="Nigeria Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Nigeria</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/bd.png" width="20" alt="Bangladesh Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Bangladesh</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/cn.png" width="20" alt="China Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> China</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/jm.png" width="20" alt="Jamaica Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Jamaica</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/za.png" width="20" alt="South Africa Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> South Africa</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/gh.png" width="20" alt="Ghana Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Ghana</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ph.png" width="20" alt="Philippines Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Philippines</div>
                    <!-- Repeat for seamless scrolling -->
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/gb.png" width="20" alt="UK Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> United Kingdom (HMPO)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/us.png" width="20" alt="US Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> United States (Visa and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/eu.png" width="20" alt="EU Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Schengen Area / EU Visa</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/in.png" width="20" alt="India Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> India (OCI and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ca.png" width="20" alt="Canada Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Canada (Visa and ID)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/au.png" width="20" alt="Australia Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Australia</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/pk.png" width="20" alt="Pakistan Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Pakistan (NICOP and Passport)</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ng.png" width="20" alt="Nigeria Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Nigeria</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/bd.png" width="20" alt="Bangladesh Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Bangladesh</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/cn.png" width="20" alt="China Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> China</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/jm.png" width="20" alt="Jamaica Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Jamaica</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/za.png" width="20" alt="South Africa Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> South Africa</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/gh.png" width="20" alt="Ghana Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Ghana</div>
                    <div class="marquee-item"><img src="https://flagcdn.com/w40/ph.png" width="20" alt="Philippines Flag" loading="lazy" style="vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.15); margin-right: 8px;"> Philippines</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Process Section -->
    <section class="process-section">
        <div class="container">
            <div class="section-header text-center reveal">
                <span class="section-subtitle">How it works</span>
                <h2>Our Passport and Visa Photo Process</h2>
                <div class="accent-divider"></div>
            </div>
            
            <div class="process-grid reveal">
                <div class="process-step">
                    <div class="process-number">01</div>
                    <div class="process-icon"><i class="fa-solid fa-camera"></i></div>
                    <h3>Studio Setup and Capture</h3>
                    <p>We set up country-specific backdrops and softbox studio lighting to eliminate shadows and capture your photo in seconds.</p>
                </div>
                
                <div class="process-step">
                    <div class="process-number">02</div>
                    <div class="process-icon"><i class="fa-solid fa-face-smile"></i></div>
                    <h3>Biometric Check</h3>
                    <p>Our digital verification system validates your photo against official UK (HMPO), US, EU, OCI, or Canada specifications.</p>
                </div>
                
                <div class="process-step">
                    <div class="process-number">03</div>
                    <div class="process-icon"><i class="fa-solid fa-id-card-clip"></i></div>
                    <h3>Instant Print or Code</h3>
                    <p>Get high-grade glossy prints in 5 minutes, or receive digital passport codes for instant online submissions.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Compliance Badges Section -->
    <section class="compliance-badges-section">
        <div class="container">
            <div class="section-header text-center reveal" style="margin-bottom: 40px;">
                <span class="section-subtitle">Official Standards</span>
                <h2>Guaranteed Acceptance and Security</h2>
                <div class="accent-divider"></div>
            </div>
            <div class="badges-grid-3 reveal">
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-stamp"></i></div>
                    <h3>HMPO Compliant</h3>
                    <p>Strict adherence to UK Home Office guidelines to guarantee digital and printed codes pass first time.</p>
                </div>
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-plane"></i></div>
                    <h3>ICAO Standard</h3>
                    <p>Meets all International Civil Aviation Organization specifications for biometric face geometry and sizing.</p>
                </div>
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-circle-check"></i></div>
                    <h3>100% Approval Guarantee</h3>
                    <p>In the unlikely event of a rejection, we will re-take and reprint your photo completely free of charge.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="service-cta text-center reveal">
        <div class="container">
            <h2>Need Passport Photos Today?</h2>
            <p>Visit us at 80 High St, Hounslow. No appointment required. Walk in and get your photos in 5 minutes.</p>
            <a href="tel:07466540111" class="btn btn-primary"><i class="fa-solid fa-phone"></i> Call Fast Access</a>
        </div>
    </section>
''' + get_footer()

with open(os.path.join(dest_dir, "passportphotos.html"), "w", encoding="utf-8") as f:
    f.write(passport_content)
print("passport-photos.html written.")


# ----------------- Write Internet Cafe Page -----------------
cafe_content = get_header("Internet Cafe", "High-speed cyber cafe internet access terminals, document scanning, emailing, and copying services in Hounslow. Established 25 years.") + '''
    <!-- Page Hero -->
    <section class="service-hero" style="background-image: linear-gradient(rgba(17, 17, 17, 0.65), rgba(17, 17, 17, 0.85)), url('internet-cafe.jpg');">
        <div class="container text-center reveal">
            <h1>High-Speed Internet Cafe</h1>
            <p>Computer terminal access, high-speed browsing, document scanning, copying, and emailing services in Hounslow.</p>
            <a href="tel:07466540111" class="btn btn-primary"><i class="fa-solid fa-phone"></i> Call Shop</a>
        </div>
    </section>

    <!-- Cafe Details -->
    <section class="service-details">
        <div class="container details-grid">
            <div class="details-text reveal">
                <h2>Your High Street Internet Hub</h2>
                <p>Need computer terminal access to check your emails, complete applications, print flight tickets, or browse the web? We offer modern computer terminals equipped with high-speed internet and connected directly to our professional printing presses. Our helpful staff are on hand to assist with scanning and emailing documents.</p>
                
                <div class="symptoms-box">
                    <h3>Available Internet Services</h3>
                    <ul class="symptoms-list">
                        <li><i class="fa-solid fa-circle-check"></i> <strong>PC Terminals:</strong> Modern workstations with secure browsing environment.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>Document Scanning:</strong> High-resolution scanning to email or USB.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>Emailing and Filing:</strong> Complete visa applications, print tax forms, and send files.</li>
                        <li><i class="fa-solid fa-circle-check"></i> <strong>Photocopying:</strong> Instant black &amp; white or color copies.</li>
                    </ul>
                </div>
            </div>
            <div class="details-image reveal">
                <img src="internet-cafe.jpg" alt="Internet Cafe Workstations" class="in-process-img" loading="lazy" width="800" height="600">
            </div>
        </div>
    </section>

    <!-- Pricing Section -->
    <section class="pricing-section">
        <div class="container">
            <div class="section-header text-center reveal">
                <span class="section-subtitle">Affordable rates</span>
                <h2>Computer Usage &amp; Copying Prices</h2>
                <div class="accent-divider"></div>
            </div>
            
            <div class="pricing-grid reveal">
                <!-- Card 1: Computer Terminal Usage -->
                <div class="pricing-card">
                    <h3><i class="fa-solid fa-desktop"></i> Computer Usage Tiers</h3>
                    <p class="price-note">High-speed browsing, secure logins, and document handling terminals:</p>
                    <div class="pricing-table-wrapper">
                        <table class="pricing-table">
                            <thead>
                                <tr>
                                    <th>Duration</th>
                                    <th>Price / Rate</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>0 Min to 15 Min</td>
                                    <td class="price-highlight">Inquire In-Store</td>
                                </tr>
                                <tr>
                                    <td>15 Min to 30 Min</td>
                                    <td class="price-highlight">Inquire In-Store</td>
                                </tr>
                                <tr>
                                    <td>30 Min to 1 Hour</td>
                                    <td class="price-highlight">Inquire In-Store</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <!-- Card 2: Copying & Scanning Services -->
                <div class="pricing-card">
                    <h3><i class="fa-solid fa-copy"></i> Copy and Scan Services</h3>
                    <p class="price-note">Instant document copying and scanning from physical sheets:</p>
                    <div class="pricing-table-wrapper">
                        <table class="pricing-table">
                            <thead>
                                <tr>
                                    <th>Service</th>
                                    <th>Price Per Side</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Colour Copy</td>
                                    <td class="price-highlight">£1.00</td>
                                </tr>
                                <tr>
                                    <td>Black and White Copy</td>
                                    <td class="price-highlight">£0.20</td>
                                </tr>
                                <tr>
                                    <td>Document Scan</td>
                                    <td class="price-highlight">£0.50</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Process Section -->
    <section class="process-section">
        <div class="container">
            <div class="section-header text-center reveal">
                <span class="section-subtitle">How it works</span>
                <h2>Using Our Internet Cafe</h2>
                <div class="accent-divider"></div>
            </div>
            
            <div class="process-grid reveal">
                <div class="process-step">
                    <div class="process-number">01</div>
                    <div class="process-icon"><i class="fa-solid fa-desktop"></i></div>
                    <h3>Secure Workstations</h3>
                    <p>Walk in and log into a clean, high-speed PC station in a secure browsing environment with standard USB ports.</p>
                </div>
                
                <div class="process-step">
                    <div class="process-number">02</div>
                    <div class="process-icon"><i class="fa-solid fa-envelope"></i></div>
                    <h3>Complete Your Work</h3>
                    <p>Browse, check emails, scan physical documents to PDF, or compile online visa and utility applications.</p>
                </div>
                
                <div class="process-step">
                    <div class="process-number">03</div>
                    <div class="process-icon"><i class="fa-solid fa-upload"></i></div>
                    <h3>Direct Print Output</h3>
                    <p>Send documents directly from your terminal to our high-resolution network printers. (Prints start from £1.00).</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Cyber Cafe Security Section -->
    <section class="compliance-badges-section">
        <div class="container">
            <div class="section-header text-center reveal" style="margin-bottom: 40px;">
                <span class="section-subtitle">Terminal Safety</span>
                <h2>Secure Browsing and Data Privacy</h2>
                <div class="accent-divider"></div>
            </div>
            <div class="badges-grid reveal">
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-user-shield"></i></div>
                    <h3>Automated Session Wipe</h3>
                    <p>For your security, all user profiles, cookies, browsing history, and downloads are wiped clean upon logout.</p>
                </div>
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-lock"></i></div>
                    <h3>Encrypted Connections</h3>
                    <p>All network traffic runs through secure firewalls to protect sensitive logins and credit card details.</p>
                </div>
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-desktop"></i></div>
                    <h3>High-Performance PCs</h3>
                    <p>Modern Windows workstations equipped with standard USB ports and direct high-speed internet links.</p>
                </div>
                <div class="compliance-card">
                    <div class="compliance-icon"><i class="fa-solid fa-print"></i></div>
                    <h3>Direct Print Routing</h3>
                    <p>Print CVs, tickets, or visa applications securely from your terminal straight to our high-resolution presses.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="service-cta text-center reveal">
        <div class="container">
            <h2>Need Web Access or Document Assistance?</h2>
            <p>Visit us at 80 High St, Hounslow. Walk in, grab a terminal, and print or scan whatever you need. (Prints start from £1.00).</p>
            <a href="tel:07466540111" class="btn btn-primary"><i class="fa-solid fa-phone"></i> Call Fast Access</a>
        </div>
    </section>
''' + get_footer()

with open(os.path.join(dest_dir, "internetcafe.html"), "w", encoding="utf-8") as f:
    f.write(cafe_content)
print("internet-cafe.html written.")


# ----------------- Write Blog Page -----------------
blog_content = get_header("Blog and Advice", "Read professional advice, printing guidelines, passport photo rules, and device maintenance guides from Hounslow's local digital hub.") + '''
    <!-- Page Hero -->
    <section class="page-hero text-center reveal">
        <div class="container">
            <h1>Blog and Advice Hub</h1>
            <p>Expert articles and local guides from our 25 years of digital and print services in Hounslow.</p>
        </div>
    </section>

    <!-- Blog Posts Section -->
    <section class="phones-section">
        <div class="container">
            <div style="text-align: center; margin-bottom: 40px;" class="reveal">
                <div class="accent-divider" style="margin: 0 auto;"></div>
            </div>

            <div class="blog-grid reveal">
                <!-- Post 1 -->
                <div class="blog-card">
                    <img src="Fast acsess images/blog_printing_hounslow.webp" alt="Document Printing Hounslow" class="blog-card-img" loading="lazy">
                    <div class="blog-card-content">
                        <div class="blog-card-meta">July 3, 2026 | Printing and Copying</div>
                        <h3>The Ultimate Guide to Last-Minute Document Printing in Hounslow</h3>
                        <p>Need urgent printing? Learn how to email your documents to fastinternetacess@gmail.com and print them instantly with zero wait times.</p>
                        <a href="blogprintinghounslow" class="btn btn-outline" style="align-self: flex-start; padding: 6px 16px; font-size: 0.85rem;">Read Post &rarr;</a>
                    </div>
                </div>
                <!-- Post 2 -->
                <div class="blog-card">
                    <img src="Fast acsess images/blog_formatting.webp" alt="Format Large Documents" class="blog-card-img" loading="lazy">
                    <div class="blog-card-content">
                        <div class="blog-card-meta">July 2, 2026 | Formatting and Scaling</div>
                        <h3>How to Format Large Documents for A3 and A4 Printing</h3>
                        <p>An easy-to-follow guide explaining aspect ratios and resolution requirements when scaling documents between A4 and A3 size formats.</p>
                        <a href="blogformatting" class="btn btn-outline" style="align-self: flex-start; padding: 6px 16px; font-size: 0.85rem;">Read Post &rarr;</a>
                    </div>
                </div>
                <!-- Post 3 -->
                <div class="blog-card">
                    <img src="Fast acsess images/blog_workstations.webp" alt="Quick Workstations" class="blog-card-img" loading="lazy">
                    <div class="blog-card-content">
                        <div class="blog-card-meta">July 1, 2026 | Workstation Rentals</div>
                        <h3>Desktop on Demand: Maximizing Quick Workstations for Remote Workers</h3>
                        <p>Distraction-free high-speed internet stations and terminals for gig workers, remote employees, or tourists needing immediate PC access.</p>
                        <a href="blogworkstations" class="btn btn-outline" style="align-self: flex-start; padding: 6px 16px; font-size: 0.85rem;">Read Post &rarr;</a>
                    </div>
                </div>
                <!-- Post 4 -->
                <div class="blog-card">
                    <img src="Fast acsess images/blog_big_puff_vapes.webp" alt="Big Puff Vapes" class="blog-card-img" loading="lazy">
                    <div class="blog-card-content">
                        <div class="blog-card-meta">June 30, 2026 | Vape Technology</div>
                        <h3>10K vs. 30K Puffs: Choosing the Right Big-Puff Vape for Your Budget</h3>
                        <p>Cost efficiency breakdown of changing vape technologies. Compare popular Dojo Blast, IVG Pro 10K, and Crown Bar 30K modular setups.</p>
                        <a href="blogbigpuffvapes" class="btn btn-outline" style="align-self: flex-start; padding: 6px 16px; font-size: 0.85rem;">Read Post &rarr;</a>
                    </div>
                </div>
                <!-- Post 5 -->
                <div class="blog-card">
                    <img src="Fast acsess images/blog_closed_pod_systems.webp" alt="Closed Pod Systems" class="blog-card-img" loading="lazy">
                    <div class="blog-card-content">
                        <div class="blog-card-meta">June 29, 2026 | Closed Pod Systems</div>
                        <h3>The Rise of Closed-Pod Systems: Reusable Batteries in the Market</h3>
                        <p>Environmental and long-term cost benefits of modular closed-pod setups. Featuring Vuse Ultra and Z-Land customizable pods.</p>
                        <a href="blogclosedpodsystems" class="btn btn-outline" style="align-self: flex-start; padding: 6px 16px; font-size: 0.85rem;">Read Post &rarr;</a>
                    </div>
                </div>
                <!-- Post 6 -->
                <div class="blog-card">
                    <img src="Fast acsess images/blog_nic_salts.webp" alt="10ml Nic Salts" class="blog-card-img" loading="lazy">
                    <div class="blog-card-content">
                        <div class="blog-card-meta">June 28, 2026 | E-Liquids</div>
                        <h3>A Flavor Breakdown of the Best 10ml Nic Salts: Finding Your Vape</h3>
                        <p>Refillable pod e-liquid guide. Check out our Mix &amp; Match deal (e.g. Bar Juice 5000 priced at £2.99 each or 4 for £10.00) and profiles.</p>
                        <a href="blognicsalts" class="btn btn-outline" style="align-self: flex-start; padding: 6px 16px; font-size: 0.85rem;">Read Post &rarr;</a>
                    </div>
                </div>
                <!-- Post 7 -->
                <div class="blog-card">
                    <img src="Fast acsess images/blog_nicotine_pouches.webp" alt="Nicotine Pouches Guide" class="blog-card-img" loading="lazy">
                    <div class="blog-card-content">
                        <div class="blog-card-meta">June 27, 2026 | Nicotine Pouches</div>
                        <h3>Nicotine Pouches: Smoke-Free Guide to ZYN, VELO, and Nordic Spirit</h3>
                        <p>Transition to white spit-free pouches. Tips on selecting strength, brands (Nordic Spirit, VELO, Pablo), and flavor profiles.</p>
                        <a href="blognicotinepouches" class="btn btn-outline" style="align-self: flex-start; padding: 6px 16px; font-size: 0.85rem;">Read Post &rarr;</a>
                    </div>
                </div>
                <!-- Post 8 -->
                <div class="blog-card">
                    <img src="Fast acsess images/blog_premium_upgrades.webp" alt="Premium Mobile Upgrades" class="blog-card-img" loading="lazy">
                    <div class="blog-card-content">
                        <div class="blog-card-meta">June 26, 2026 | Smartphone Upgrades</div>
                        <h3>Premium Mobile Upgrades: Is It Time to Step Up to the iPhone 16 Pro Max?</h3>
                        <p>Write-up comparing flagships. Check out in-stock iPhone 16 Pro Max 256GB, standard iPhone 16, and Samsung S22 Ultra models.</p>
                        <a href="blogpremiumupgrades" class="btn btn-outline" style="align-self: flex-start; padding: 6px 16px; font-size: 0.85rem;">Read Post &rarr;</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
''' + get_footer()

with open(os.path.join(dest_dir, "blog.html"), "w", encoding="utf-8") as f:
    f.write(blog_content)
print("blog.html written.")


# ----------------- Write Individual Blog Posts -----------------

# 1. blogprintinghounslow.html
blog1_content = get_header("Last-Minute Document Printing", "Email documents directly to fastinternetacess@gmail.com and print them instantly in Hounslow with zero wait times.") + '''
    <article class="blog-post-container reveal">
        <header class="blog-post-header">
            <span class="section-subtitle">Printing and Copying</span>
            <h1>The Ultimate Guide to Last-Minute Document Printing in Hounslow</h1>
            <div class="blog-post-meta">Published July 3, 2026 by Fast Access Print Hub</div>
        </header>
        
        <img src="Fast acsess images/blog_printing_hounslow.webp" alt="Hounslow Document Printing" style="width: 100%; border-radius: 8px; margin-bottom: 40px; box-shadow: var(--shadow);" loading="lazy">
        
        <div class="blog-post-content">
            <p>Need urgent printing? Whether you\'re a remote worker, local professional, student, or traveler needing a boarding pass printed, Fast Access is Hounslow\'s trusted local print shop. We ensure document printing is fast, reliable, and convenient.</p>
            
            <h2>Print Straight From Your Inbox</h2>
            <p>To eliminate wait times, you can submit your PDFs, shipping labels, tickets, or visa documentation directly from your phone. Simply email your files to:</p>
            <ul>
                <li><strong>fastinternetacess@gmail.com</strong></li>
                <li><strong>fastinternetaccess21@gmail.com</strong></li>
            </ul>
            <p>Once sent, our staff receives them in real-time. Walk in, confirm your email address at the counter, and we will print your documents immediately.</p>
            
            <h2>Transparent Pricing Structure</h2>
            <p>We believe in straightforward, competitive rates at the register:</p>
            <ul>
                <li><strong>First Page (Sent via Email):</strong> £1.00</li>
                <li><strong>A4 Black and White (per side):</strong> £0.20</li>
                <li><strong>A4 Colour (per side):</strong> £1.00</li>
            </ul>
            <p>Note: We maintain a <strong>minimum card payment of £3.00</strong> in-store, so we recommend printing multiple copies or bundling services to meet this threshold.</p>
            
            <div class="blog-cta" style="margin-top: 40px; padding: 25px; background: var(--bg-alternate); border-radius: 6px; border: 1px dashed var(--border-color); text-align: center;">
                <h3 style="margin-bottom: 10px; color: var(--text-main); font-size: 1.15rem;">Ready to Print?</h3>
                <p style="margin-bottom: 15px; font-size: 0.9rem; color: var(--text-muted);">Email files to <strong>fastinternetacess@gmail.com</strong> and walk in today. Min card payment £3.00.</p>
                <a href="mailto:fastinternetacess@gmail.com" class="btn btn-primary" style="padding: 8px 20px; font-size: 0.85rem;"><i class="fa-solid fa-envelope"></i> Email Files Now</a>
            </div>
        </div>
    </article>
''' + get_footer()

with open(os.path.join(dest_dir, "blogprintinghounslow.html"), "w", encoding="utf-8") as f:
    f.write(blog1_content)
print("blogprintinghounslow.html written.")


# 2. blog-formatting.html
blog2_content = get_header("Formatting A3 and A4 Documents", "Aspect ratios and resolution requirements when scaling documents between A4 and A3 size formats.") + '''
    <article class="blog-post-container reveal">
        <header class="blog-post-header">
            <span class="section-subtitle">Formatting &amp; Sizing</span>
            <h1>How to Format Large Documents for A3 and A4 Printing</h1>
            <div class="blog-post-meta">Published July 2, 2026 by Design and Print Team</div>
        </header>
        
        <img src="Fast acsess images/blog_formatting.webp" alt="Formatting and scaling sizes" style="width: 100%; border-radius: 8px; margin-bottom: 40px; box-shadow: var(--shadow);" loading="lazy">
        
        <div class="blog-post-content">
            <p>Upscaling a low-resolution file to a larger layout leads to blurry, pixelated results. To get premium, crystal-clear physical prints, it is essential to format aspect ratios and resolution targets correctly. Here is our expert guide on formatting document files for standard A4 and large A3 printing.</p>
            
            <h2>Understanding Sizing and Ratios</h2>
            <p>Both A4 and A3 paper formats follow the ISO 216 standard, utilizing a 1:√2 aspect ratio (1.414). This means an A4 sheet (210 x 297 mm) can scale up to an A3 sheet (297 x 420 mm) without cropping your margins. To preserve clarity, keep your source file resolution at <strong>300 DPI (Dots Per Inch)</strong> and save files as <strong>PDFs</strong> to lock vector fonts and margins.</p>
            
            <h2>A3 vs A4 Pricing Tiers</h2>
            <p>Upgrading to high-quality color prints or larger A3 layouts is highly affordable and provides maximum visual impact for posters, presentations, and portfolios:</p>
            <ul>
                <li><strong>A4 Black and White:</strong> £0.20 per side</li>
                <li><strong>A4 Colour:</strong> £1.00 per side (premium visual enhancement)</li>
                <li><strong>A3 Black and White:</strong> £1.00 per side</li>
                <li><strong>A3 Colour:</strong> £3.00 per side (ideal for CAD drawings, blueprints, and posters)</li>
            </ul>
            
            <div class="blog-cta" style="margin-top: 40px; padding: 25px; background: var(--bg-alternate); border-radius: 6px; border: 1px dashed var(--border-color); text-align: center;">
                <h3 style="margin-bottom: 10px; color: var(--text-main); font-size: 1.15rem;">Need CAD or Poster Prints?</h3>
                <p style="margin-bottom: 15px; font-size: 0.9rem; color: var(--text-muted);">We offer professional A3 and A4 colour printing. Walk in with your PDF or email it to us.</p>
                <a href="mailto:fastinternetacess@gmail.com" class="btn btn-primary" style="padding: 8px 20px; font-size: 0.85rem;"><i class="fa-solid fa-envelope"></i> Email Files</a>
            </div>
        </div>
    </article>
''' + get_footer()

with open(os.path.join(dest_dir, "blogformatting.html"), "w", encoding="utf-8") as f:
    f.write(blog2_content)
print("blog-formatting.html written.")


# 3. blog-workstations.html
blog3_content = get_header("Quick Workstations for Remote Workers", "High-speed internet terminals and workspace rentals for gig workers and remote employees in Hounslow.") + '''
    <article class="blog-post-container reveal">
        <header class="blog-post-header">
            <span class="section-subtitle">Workstation Rentals</span>
            <h1>Desktop on Demand: Maximizing Quick Workstations for Remote Workers</h1>
            <div class="blog-post-meta">Published July 1, 2026 by Cafe Operations</div>
        </header>
        
        <img src="Fast acsess images/blog_workstations.webp" alt="Computer Workstations" style="width: 100%; border-radius: 8px; margin-bottom: 40px; box-shadow: var(--shadow);" loading="lazy">
        
        <div class="blog-post-content">
            <p>If you are a remote employee, freelancer, tourist, or gig worker needing temporary computer access, Fast Access offers dedicated workstations. Secure, high-speed Windows PC terminals let you quickly edit a document, fill out a visa application, check email, or print important documents.</p>
            
            <h2>Dedicated Computer Usage Charges</h2>
            <p>We provide affordable, tiered rates for all workstation access:</p>
            <ul>
                <li><strong>0 to 15 Minutes:</strong> £0.50</li>
                <li><strong>15 to 30 Minutes:</strong> £1.00</li>
                <li><strong>30 Minutes to 1 Hour:</strong> £1.50</li>
            </ul>
            
            <h2>Workstation Policies</h2>
            <p>To ensure a clean, quiet, and professional workspace environment for all remote workers, we enforce a strict <strong>no-eating policy</strong> around our hardware terminals. Keeping food and liquids away from the workstations protects the keyboards, mice, and computer hardware.</p>
            
            <div class="blog-cta" style="margin-top: 40px; padding: 25px; background: var(--bg-alternate); border-radius: 6px; border: 1px dashed var(--border-color); text-align: center;">
                <h3 style="margin-bottom: 10px; color: var(--text-main); font-size: 1.15rem;">Need Desktop Access?</h3>
                <p style="margin-bottom: 15px; font-size: 0.9rem; color: var(--text-muted);">Walk in and grab an open workstation. High-speed internet and printing are fully integrated.</p>
                <a href="tel:07466540111" class="btn btn-primary" style="padding: 8px 20px; font-size: 0.85rem;"><i class="fa-solid fa-desktop"></i> Call for Details</a>
            </div>
        </div>
    </article>
''' + get_footer()

with open(os.path.join(dest_dir, "blogworkstations.html"), "w", encoding="utf-8") as f:
    f.write(blog3_content)
print("blog-workstations.html written.")


# 4. blog-big-puff-vapes.html
blog4_content = get_header("10K vs 30K Puffs Vape Budget", "A cost-efficiency breakdown of changing vape technologies and modular setups.") + '''
    <article class="blog-post-container reveal">
        <header class="blog-post-header">
            <span class="section-subtitle">Vape Technology</span>
            <h1>10K vs. 30K Puffs: Choosing the Right Big-Puff Vape for Your Budget</h1>
            <div class="blog-post-meta">Published June 30, 2026 by Vape Tech Experts</div>
        </header>
        
        <img src="Fast acsess images/blog_big_puff_vapes.webp" alt="Big Puff Vapes" style="width: 100%; border-radius: 8px; margin-bottom: 40px; box-shadow: var(--shadow);" loading="lazy">
        
        <div class="blog-post-content">
            <p>Big-puff vapes offer massive longevity improvements over standard disposables. However, with systems ranging from 10,000 puffs up to 30,000 puffs, choosing the right modular system for your budget requires understanding the core differences. Here is a breakdown of the cost and technology.</p>
            
            <h2>Vape Capacity and Technology Breakdown</h2>
            <ul>
                <li><strong>10K-Puff Series (Dojo Blast 10K &amp; IVG Pro 10K):</strong> Compact, pocket-friendly pod systems. These setups utilize 10ml modular pod refill systems. They offer a great entry point for budget-conscious vapers looking for durability without the bulk.</li>
                <li><strong>30K-Puff Hypermax Series (Crown Bar Al Fakher 30K &amp; Lost Mary 30K):</strong> Ultra-high-capacity modular kits. Utilizing advanced coil heating, rechargeable bases, and multi-pod designs, these provide maximum longevity and are highly cost-efficient in the long run.</li>
            </ul>
            
            <h2>Which is Better for You?</h2>
            <p>If you prefer a smaller device with easy pod replacements, the Dojo Blast or IVG Pro series is perfect. For heavy users seeking maximum savings and a powerhouse setup, the Crown Bar Al Fakher 30K or Lost Mary 30K systems are unmatched.</p>
            
            <div class="blog-cta" style="margin-top: 40px; padding: 25px; background: var(--bg-alternate); border-radius: 6px; border: 1px dashed var(--border-color); text-align: center;">
                <h3 style="margin-bottom: 10px; color: var(--text-main); font-size: 1.15rem;">Explore Our Vape Range</h3>
                <p style="margin-bottom: 15px; font-size: 0.9rem; color: var(--text-muted);">We stock Dojo Blast 10K, IVG Pro 10K, and Crown Bar Al Fakher 30K in-store today.</p>
                <a href="catalogue.html?category=vape%20kits" class="btn btn-primary" style="padding: 8px 20px; font-size: 0.85rem;"><i class="fa-solid fa-list"></i> View Vape Catalogue</a>
            </div>
        </div>
    </article>
''' + get_footer()

with open(os.path.join(dest_dir, "blogbigpuffvapes.html"), "w", encoding="utf-8") as f:
    f.write(blog4_content)
print("blog-big-puff-vapes.html written.")


# 5. blog-closed-pod-systems.html
blog5_content = get_header("Rise of Closed Pod Systems", "Environmental and long-term cost benefits of closed-pod setups and reusable vape batteries.") + '''
    <article class="blog-post-container reveal">
        <header class="blog-post-header">
            <span class="section-subtitle">Closed Pod Systems</span>
            <h1>The Rise of Closed-Pod Systems: Reusable Batteries in the Market</h1>
            <div class="blog-post-meta">Published June 29, 2026 by Eco Vape Team</div>
        </header>
        
        <img src="Fast acsess images/blog_closed_pod_systems.webp" alt="Closed Pod Systems" style="width: 100%; border-radius: 8px; margin-bottom: 40px; box-shadow: var(--shadow);" loading="lazy">
        
        <div class="blog-post-content">
            <p>Vape users are moving away from single-use disposables in favor of reusable closed-pod systems. By using a permanent rechargeable battery base paired with disposable flavour cartridges, users save money and reduce plastic waste. Here is why reusable systems are dominating the shelves.</p>
            
            <h2>Economics of Reusable Battery Systems</h2>
            <p>Instead of throwing away a battery with every pod, closed systems let you reuse the core base. They offer advanced charging options and long-term cost savings since you only buy replacement pods:</p>
            <ul>
                <li><strong>Vuse Ultra System:</strong> A high-performance kit featuring fast wireless charging, clearview display readouts, and signature flavours like Cherry Ice.</li>
                <li><strong>Z-Land Modular Pod System:</strong> An incredibly customisable system that lets you mix and match flavor bases like Mango and Banana.</li>
            </ul>
            
            <div class="blog-cta" style="margin-top: 40px; padding: 25px; background: var(--bg-alternate); border-radius: 6px; border: 1px dashed var(--border-color); text-align: center;">
                <h3 style="margin-bottom: 10px; color: var(--text-main); font-size: 1.15rem;">Browse Closed-Pod Hardware</h3>
                <p style="margin-bottom: 15px; font-size: 0.9rem; color: var(--text-muted);">We carry Z-Land and Vuse Ultra starter kits and replacement pods at our counter.</p>
                <a href="catalogue.html?category=vape%20refills" class="btn btn-primary" style="padding: 8px 20px; font-size: 0.85rem;"><i class="fa-solid fa-list"></i> View Replacement Pods</a>
            </div>
        </div>
    </article>
''' + get_footer()

with open(os.path.join(dest_dir, "blogclosedpodsystems.html"), "w", encoding="utf-8") as f:
    f.write(blog5_content)
print("blog-closed-pod-systems.html written.")


# 6. blog-nic-salts.html
blog6_content = get_header("Best 10ml Nic Salts Flavor Breakdown", "Refillable pod e-liquid guide featuring our Mix and Match multi-buy promotions.") + '''
    <article class="blog-post-container reveal">
        <header class="blog-post-header">
            <span class="section-subtitle">E-Liquids</span>
            <h1>A Flavor Breakdown of the Best 10ml Nic Salts: Finding Your Vape</h1>
            <div class="blog-post-meta">Published June 28, 2026 by Flavour Reviewer</div>
        </header>
        
        <img src="Fast acsess images/blog_nic_salts.webp" alt="10ml Nic Salts" style="width: 100%; border-radius: 8px; margin-bottom: 40px; box-shadow: var(--shadow);" loading="lazy">
        
        <div class="blog-post-content">
            <p>Nicotine salts deliver a smoother throat hit and faster nicotine absorption than standard freebase e-liquids. If you use a refillable pod kit, selecting the right nic salt is the key to an optimal vaping experience. Here is a review of our top e-liquid flavours.</p>
            
            <h2>Premium Flavor Profiles</h2>
            <ul>
                <li><strong>Strawberry Sour Raspberry:</strong> A delicious balance of sweet strawberries and tangy, sour raspberries.</li>
                <li><strong>Pink Bubba / Blue Bubba:</strong> A nostalgic, sweet bubblegum candy base.</li>
                <li><strong>Lemon and Lime:</strong> A crisp, citrusy, and refreshing all-day vape.</li>
                <li><strong>Red Apple Ice:</strong> Crisp red apple flavour with a cool, icy finish.</li>
            </ul>
            
            <h2>Maximize Savings: Mix &amp; Match Deals</h2>
            <p>We offer fantastic multi-buy promotions at our retail counter to help you stock up on e-liquids. Check out our **Bar Juice 5000 priced at £2.99 each or 4 for £10.00** promotion to lock in massive discounts.</p>
            
            <div class="blog-cta" style="margin-top: 40px; padding: 25px; background: var(--bg-alternate); border-radius: 6px; border: 1px dashed var(--border-color); text-align: center;">
                <h3 style="margin-bottom: 10px; color: var(--text-main); font-size: 1.15rem;">Stock Up and Save</h3>
                <p style="margin-bottom: 15px; font-size: 0.9rem; color: var(--text-muted);">Mix &amp; Match Bar Juice 5000 and other 10ml salts: 4 for £10.00 in-store today.</p>
                <a href="catalogue.html?category=e-liquids" class="btn btn-primary" style="padding: 8px 20px; font-size: 0.85rem;"><i class="fa-solid fa-basket-shopping"></i> View E-Liquids</a>
            </div>
        </div>
    </article>
''' + get_footer()

with open(os.path.join(dest_dir, "blognicsalts.html"), "w", encoding="utf-8") as f:
    f.write(blog6_content)
print("blog-nic-salts.html written.")


# 7. blog-nicotine-pouches.html
blog7_content = get_header("Nicotine Pouches Smoke-Free Guide", "Learn how to select strength, brands, and flavours for Nordic Spirit, VELO, and Pablo pouches.") + '''
    <article class="blog-post-container reveal">
        <header class="blog-post-header">
            <span class="section-subtitle">Nicotine Pouches</span>
            <h1>Nicotine Pouches: Smoke-Free Guide to ZYN, VELO, and Nordic Spirit</h1>
            <div class="blog-post-meta">Published June 27, 2026 by Health and Tech Team</div>
        </header>
        
        <img src="Fast acsess images/blog_nicotine_pouches.webp" alt="Nicotine Pouches Guide" style="width: 100%; border-radius: 8px; margin-bottom: 40px; box-shadow: var(--shadow);" loading="lazy">
        
        <div class="blog-post-content">
            <p>For adult users looking for a 100% tobacco-free, smoke-free, and spit-free nicotine alternative, white nicotine pouches have become the leading choice. They are discreet, easy to use, and available in multiple strength levels. Here is our comprehensive guide.</p>
            
            <h2>How Nicotine Pouches Work</h2>
            <p>You simply place a single pouch under your upper lip. It releases nicotine and flavor gradually over 30 to 60 minutes. Because they contain no tobacco leaf, they won\'t stain your teeth and require no spitting.</p>
            
            <h2>Choosing the Right Brand &amp; Strength</h2>
            <ul>
                <li><strong>Nordic Spirit (Mild to Strong):</strong> Smooth, refreshing options like <em>Spearmint</em>, <em>Sweet Mint</em>, and <em>Wild Berry / Elderflower</em>.</li>
                <li><strong>VELO (Standard to Strong):</strong> Popular fruity and cooling options like <em>Spicy Papaya</em>, <em>Mango Flame</em>, and <em>Ruby Berry / Blush Berry</em>.</li>
                <li><strong>Pablo (Extreme Strength):</strong> Highly potent lines designed for experienced users, including <em>Pablo Ice Cold</em>, <em>Pablo Exclusive</em>, and <em>Pablo Red</em>.</li>
            </ul>
            
            <div class="blog-cta" style="margin-top: 40px; padding: 25px; background: var(--bg-alternate); border-radius: 6px; border: 1px dashed var(--border-color); text-align: center;">
                <h3 style="margin-bottom: 10px; color: var(--text-main); font-size: 1.15rem;">Check Out Our Pouch Stock</h3>
                <p style="margin-bottom: 15px; font-size: 0.9rem; color: var(--text-muted);">We carry ZYN, VELO, Nordic Spirit, and Pablo in all strengths. View flavours in-store.</p>
                <a href="catalogue.html?category=nicotine%20pouches" class="btn btn-primary" style="padding: 8px 20px; font-size: 0.85rem;"><i class="fa-solid fa-list"></i> View Pouches Catalogue</a>
            </div>
        </div>
    </article>
''' + get_footer()

with open(os.path.join(dest_dir, "blognicotinepouches.html"), "w", encoding="utf-8") as f:
    f.write(blog7_content)
print("blog-nicotine-pouches.html written.")


# 8. blog-premium-upgrades.html
blog8_content = get_header("Premium Mobile Phone Upgrades", "A detailed flagship comparison between iPhone 16 Pro Max, iPhone 16, and Samsung Galaxy models.") + '''
    <article class="blog-post-container reveal">
        <header class="blog-post-header">
            <span class="section-subtitle">Smartphone Upgrades</span>
            <h1>Premium Mobile Upgrades: Is It Time to Step Up to the iPhone 16 Pro Max?</h1>
            <div class="blog-post-meta">Published June 26, 2026 by Mobile Hardware Experts</div>
        </header>
        
        <img src="Fast acsess images/blog_premium_upgrades.webp" alt="Flagship iPhone Upgrades" style="width: 100%; border-radius: 8px; margin-bottom: 40px; box-shadow: var(--shadow);" loading="lazy">
        
        <div class="blog-post-content">
            <p>Upgrading your phone connects you to better cameras, faster processing speeds, and superior battery life. If you\'re carrying a model that\'s a few generations old, flagship devices represent a massive leap forward. Here is why stepping up to a premium model is worth it.</p>
            
            <h2>Highlighting Our In-Store Flagship Inventory</h2>
            <ul>
                <li><strong>Apple iPhone 16 Pro Max (256GB):</strong> Features a premium Titanium Frame, the flagship A18 Pro chip, and advanced cameras. Available in Natural Titanium and Black.</li>
                <li><strong>Apple iPhone 16 (128GB):</strong> Represents the perfect balance of price and performance, featuring the new Action Button and dual camera. Available in Black, Pink, and White.</li>
                <li><strong>Samsung Galaxy S22 Ultra (256GB / 512GB):</strong> The ultimate power-user device, featuring a pro-grade quad camera setup and a built-in S-Pen. Available in Phantom Black.</li>
            </ul>
            
            <h2>Simple In-Store Purchases</h2>
            <p>Skip the carrier shipping delays and visit Fast Access to upgrade today. We accept cash and card payments (minimum card payment £3.00 applies).</p>
            
            <div class="blog-cta" style="margin-top: 40px; padding: 25px; background: var(--bg-alternate); border-radius: 6px; border: 1px dashed var(--border-color); text-align: center;">
                <h3 style="margin-bottom: 10px; color: var(--text-main); font-size: 1.15rem;">Want to Purchase?</h3>
                <p style="margin-bottom: 15px; font-size: 0.9rem; color: var(--text-muted);">Visit us at 80 High St, Hounslow to inspect these models. Min card payment £3.00.</p>
                <a href="catalogue.html?category=smartphones" class="btn btn-primary" style="padding: 8px 20px; font-size: 0.85rem;"><i class="fa-solid fa-mobile-screen-button"></i> View Smartphones</a>
            </div>
        </div>
    </article>
''' + get_footer()

with open(os.path.join(dest_dir, "blogpremiumupgrades.html"), "w", encoding="utf-8") as f:
    f.write(blog8_content)
print("blog-premium-upgrades.html written.")


# 14 service/repair page generation calls
# 1. SCREEN REPAIR PAGE
build_service_page(
    filename="screenrepair.html",
    service_name="Phone Screen Repair",
    one_liner="Smashed display or unresponsive touch screen? We fit quality replacement panels.",
    body_copy="Smashed phone screens shouldn't mean buying a new device. We fit premium replacement displays for iPhone, Samsung Galaxy, Google Pixel, and more. Our parts restore original touch responsiveness, brightness, and color accuracy. Most repairs are completed within 1 hour.",
    symptoms=[
        "Cracked, shattered, or physically damaged front glass panel",
        "Screen flickering, colored vertical lines, or black stripes",
        "Black screen display while the phone still vibrates/sounds",
        "Unresponsive touch screen zones or ghost-touch behaviors"
    ],
    images=[
        "Screen broken screen repair page image 1.jpg",
        "Screen being repaired image 2.jpg",
        "Screen fixed image 3.jpg"
    ],
    is_laptop=False,
    hero_image="cracked-screen.jpg"
)

# 2. BATTERY REPLACEMENT PAGE
build_service_page(
    filename="batteryreplacement.html",
    service_name="Phone Battery Replacement",
    one_liner="Phone draining in hours or shutting down at 20%? Get a brand new cell.",
    body_copy="Over time, lithium-ion phone batteries naturally degrade and lose capacity. Swapping your depleted cell with a brand new, safety-tested battery restores original usage hours and prevents sudden shutdowns. Most battery replacements take under 45 minutes.",
    symptoms=[
        "Battery drains extremely fast during basic usage",
        "Phone turns off suddenly at 10% to 30% battery level",
        "Battery percentage jumps up and down erratically",
        "Device back casing looks slightly bulged (swollen battery hazard)"
    ],
    images=[
        "Battery dead image 1.jpg",
        "Battery replacment page 2.jpg",
        "Battery fixed 100 percent.jpg"
    ],
    is_laptop=False,
    hero_image="battery-repair.jpg"
)

# 3. WATER DAMAGE PAGE
build_service_page(
    filename="waterdamage.html",
    service_name="Phone Water Damage Repair",
    one_liner="Dropped in water? Don't try charging it — bring it straight to our shop.",
    body_copy="Liquid contact triggers rapid corrosion inside your phone. We open the device, extract the main circuit board, and treat it in a specialized chemical ultrasonic bath to remove moisture and minerals. We then diagnose individual components to bring the device back to life.",
    symptoms=[
        "Device dropped in water, sink, toilet, or liquid drink",
        "Corrosion spots visible inside ports or SIM tray slot",
        "Unresponsive buttons, screen flicker, or no power after wetness",
        "Muffled sound from speakers or failure to register microphone input"
    ],
    images=[
        "Water damage phone water damage image 1.jpg",
        "Water damage being repaired.jpg",
        "Water damage repaired.jpg"
    ],
    is_laptop=False,
    hero_image="water-damage.jpg"
)

# 4. CHARGING PORT PAGE
build_service_page(
    filename="chargingport.html",
    service_name="Phone Charging Port Repair",
    one_liner="Loose charger cables, slow charging, or completely dead USB-C / Lightning ports.",
    body_copy="A worn-out charging port makes recharging your device frustrating or impossible. We clean packed lint from loose ports or replace the entire charging jack assembly to restore full power connection and fast charging speeds.",
    symptoms=[
        "Charging cable feels loose and easily falls out of the port",
        "Device only charges when the cable is wiggled or held at an angle",
        "Phone completely fails to charge or register connection when plugged in",
        "Extremely slow charging times compared to normal speeds"
    ],
    images=[
        "Charger port broken image 1.webp",
        "Charger port being fixed.jpg",
        "Charger port fixed.webp"
    ],
    is_laptop=False,
    hero_image="charging-port.jpg"
)

# 5. PHONE UNLOCKING PAGE
build_service_page(
    filename="phoneunlocking.html",
    service_name="Phone Unlocking",
    one_liner="Unlock your phone from any carrier and enjoy complete network freedom.",
    body_copy="Locked handsets limit you to a single mobile provider. We perform factory-standard network unlocking so you can insert any SIM card from any carrier worldwide. Perfect for switching network rates or using local SIMs while traveling abroad.",
    symptoms=[
        "'SIM Not Supported' or network lock error message on screen",
        "Pre-owned handset locked to a specific network carrier",
        "Travelling overseas and wanting to use cheaper local network SIMs",
        "Switching mobile providers but wanting to keep your current device"
    ],
    images=[
        "Phone sim not supported image 1 unlock.png",
        "Phone being unblocked.jpg",
        "Use the provider you want image 3.jpg"
    ],
    is_laptop=False,
    hero_image="unlock-phone.jpg"
)

# 6. TABLET & GENERAL REPAIRS PAGE
build_service_page(
    filename="laptoptablet.html",
    service_name="Tablet and General Repairs",
    one_liner="From iPad screen swaps to logic board issues — we repair tablets and miscellaneous tech.",
    body_copy="We apply the same high-quality technical standards to tablets, iPads, MacBooks, and Windows laptops. Whether you need a smashed screen replaced, a keyboard fixed, or performance tune-ups, our workshop is fully equipped for larger devices.",
    symptoms=[
        "Smashed iPad or tablet screen glass, or bleeding LCD displays",
        "Tablet battery draining extremely quickly or getting hot",
        "Keyboard keys stuck, missing, or registering double inputs",
        "Charging connection issues or loose socket jacks on tablets"
    ],
    images=[
        "Tablet wont turn on.webp",
        "Laptop broken image 1.jpg",
        "Laptop and tablet fixed.jpg"
    ],
    is_laptop=False,
    hero_image="laptop-broken-screen.jpg"
)


# ----------------- Write Laptop Sub-pages -----------------
# 7. LAPTOP SCREEN REPAIR PAGE
build_service_page(
    filename="laptopscreen.html",
    service_name="Laptop Screen Repair",
    one_liner="Cracked, flickering or dead laptop screen? We replace displays for all models.",
    body_copy="Smashed screens shouldn't mean replacing your entire laptop. We fit premium replacement LED panels for MacBooks, Dell, HP, Lenovo, and ASUS. Most screen replacements are completed within 1-2 hours.",
    symptoms=[
        "Smashed or cracked outer glass panel or inner LCD display",
        "Flickering display, strange horizontal/vertical lines, or black spots",
        "No display at all while laptop power light is on and fan spins",
        "Dim backlight where the screen image is barely visible"
    ],
    images=[
        "laptop-screen-broken.jpg",
        "laptop-screen-repairing.jpg",
        "laptop-screen-fixed.jpg"
    ],
    is_laptop=True,
    hero_image="laptop-broken-screen.jpg"
)

# 8. LAPTOP SLOW PC TUNEUP PAGE
build_service_page(
    filename="slowperformance.html",
    service_name="Laptop Performance Tuneup",
    one_liner="Speed up your slow laptop with professional tuning and internal dust cleanup.",
    body_copy="Over time, computers collect dust, dry out thermal paste, and accumulate registry bloat. We clean inside, apply premium thermal compound, and streamline your operating system to restore speed.",
    symptoms=[
        "Laptop takes several minutes to start up or shut down",
        "Constant loading cursor and frozen application windows",
        "Fan runs constantly at maximum speed and laptop feels hot",
        "Low performance during basic tasks like web browsing or video calls"
    ],
    images=[
        "laptop-slow-before.jpg",
        "laptop-performance-repairing.jpg",
        "laptop-performance-fixed.jpg"
    ],
    is_laptop=True,
    hero_image="laptop-slow-computer.jpg"
)

# 9. LAPTOP VIRUS & MALWARE PAGE
build_service_page(
    filename="virusmalware.html",
    service_name="Laptop Virus and Malware Removal",
    one_liner="Complete virus warning removal, system cleanup, and security reinforcement.",
    body_copy="Pop-ups, lock screens, or sudden slowdowns are signs of malware infection. We wipe viruses, remove spyware, and install active firewalls to protect your identity and private data.",
    symptoms=[
        "Suspicious browser pop-ups, fake antivirus alerts, or redirecting search pages",
        "Device is locked by ransomware demanding payment to access files",
        "Unexplained high network usage and password change warnings",
        "System settings or desktop background changed without permission"
    ],
    images=[
        "laptop-virus-before.jpg",
        "laptop-virus-repairing.jpg",
        "laptop-virus-fixed.jpg"
    ],
    is_laptop=True,
    hero_image="laptop-virus-removal.jpg"
)

# 10. LAPTOP DATA RECOVERY PAGE
build_service_page(
    filename="datarecovery.html",
    service_name="Laptop Data Recovery",
    one_liner="Recover lost files, precious photos, and critical documents from failed drives.",
    body_copy="If your computer won't boot or showing disk errors, do not write new files. We extract data from failed SSDs, corrupt HDDs, and formatted USBs safely.",
    symptoms=[
        "Laptop boots directly into recovery mode or shows 'No Bootable Device'",
        "Internal drive making clicking or grinding noises",
        "Accidental deletion of important directories, folders, or document formats",
        "USB drive or memory card shows as unformatted or raw partition"
    ],
    images=[
        "laptop-data-before.jpg",
        "laptop-data-repairing.jpg",
        "laptop-data-fixed.jpg"
    ],
    is_laptop=True,
    hero_image="laptop-data-recovery.jpg"
)

# 11. LAPTOP RAM & STORAGE UPGRADE PAGE
build_service_page(
    filename="ramstorage.html",
    service_name="Laptop RAM & SSD Upgrade",
    one_liner="Upgrade your drive to a superfast SSD and boost multitasking with extra RAM.",
    body_copy="Low storage warning or slow bootup? Swapping a mechanical HDD for an SSD speeds up performance by up to 10x. We duplicate your data exactly to the new drive.",
    symptoms=[
        "Constant 'Low Disk Space' warning notifications on screen",
        "Applications crashing or freezing when opening multiple browser tabs",
        "Slow system response due to low random-access memory (RAM) capacity",
        "Standard hard drive (HDD) running at 100% active time in task manager"
    ],
    images=[
        "laptop-ram-before.jpg",
        "laptop-ram-repairing.jpg",
        "laptop-ram-fixed.jpg"
    ],
    is_laptop=True,
    hero_image="laptop-ram-upgrade.jpg"
)

# 12. LAPTOP KEYBOARD & PORTS PAGE
build_service_page(
    filename="keyboardports.html",
    service_name="Laptop Keyboard and Ports Repair",
    one_liner="Sticky keys, loose USB ports, or unresponsive trackpads — repaired.",
    body_copy="Damaged keyboards or loose power connections are highly frustrating. We replace keyboard assemblies and solder fresh USB/charging ports.",
    symptoms=[
        "Individual keyboard keys stick, double-register, or completely fail",
        "USB, HDMI, or audio jacks feel loose and disconnect on movement",
        "Trackpad is unresponsive, erratic, or physically stuck (swollen battery sign)",
        "Laptop keyboard lights up but none of the inputs register on screen"
    ],
    images=[
        "laptop-keyboard-before.jpg",
        "laptop-keyboard-repairing.jpg",
        "laptop-keyboard-fixed.jpg"
    ],
    is_laptop=True,
    hero_image="laptop-keyboard-repair.jpg"
)

# 13. LAPTOP LIQUID SPILL RECOVERY PAGE
build_service_page(
    filename="liquidspill.html",
    service_name="Laptop Liquid Spill Recovery",
    one_liner="Spilled liquid on your laptop? Turn it off immediately and bring it to us.",
    body_copy="Time is critical. We disassemble your laptop, dry components, decontaminate corrosion in ultrasonic baths, and solder corroded board components.",
    symptoms=[
        "Water, coffee, tea, beer, or sugary drinks spilled on keyboard",
        "Laptop turned off immediately after liquid contact and refuses to turn on",
        "Keyboard keys feel sticky or trackpad behaves erratically after spill",
        "Corrosion spots or liquid droplets visible in venting ports"
    ],
    images=[
        "laptop-water-before.jpg",
        "laptop-water-repairing.jpg",
        "laptop-water-fixed.jpg"
    ],
    is_laptop=True,
    hero_image="laptop-water-damage.jpg"
)

# 14. LAPTOP POWER & BATTERY PAGE
build_service_page(
    filename="powercharging.html",
    service_name="Laptop Power and Battery Repair",
    one_liner="Battery draining quickly or laptop failing to turn on? We replace cells fast.",
    body_copy="Swollen batteries are fire hazards and warp trackpads. We swap MacBook and Windows laptop batteries with premium safety-tested cells.",
    symptoms=[
        "Laptop runs only when plugged into the charger plug",
        "Battery percentage drains rapidly during basic operations",
        "Battery health shows 'Service Recommended' or 'Replace Soon'",
        "Laptop trackpad or bottom cover is physically bulging or warped"
    ],
    images=[
        "laptop-power-before.jpg",
        "laptop-power-repairing.jpg",
        "laptop-power-fixed.jpg"
    ],
    is_laptop=True,
    hero_image="laptop-repair-hero.jpg"
)


# ----------------- Write vapes-pouches.html -----------------
vapes_content = get_header("Vapes and Pouches", "Premium disposable vapes and nicotine pouch brands in stock. Visit us in store.") + '''
    <!-- Page Hero -->
    <section class="page-hero text-center reveal">
        <div class="container">
            <h1>Vapes and Nicotine Pouches</h1>
            <p>Authorized stockists for major disposable vape and nicotine pouch brands in London.</p>
        </div>
    </section>

    <!-- Product Grid Section -->
    <section class="phones-section">
        <div class="container">
            <p class="intro-paragraph text-center">We stock a wide selection of premium disposable vapes and nicotine pouches in varied flavors and nicotine strengths. Please note that nicotine products are only available for purchase in-store by customers aged 18 and over.</p>
            
            <div class="section-header text-center reveal">
                <h2>Nicotine Pouches</h2>
                <div class="accent-divider"></div>
            </div>
            
            <div class="phones-grid reveal" style="margin-bottom: 60px; margin-top: 30px;">
                <!-- Nordic Spirit -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Nordic Reuse.webp" alt="Nordic Spirit Nicotine Pouches">
                    <h3>Nordic Spirit</h3>
                    <span class="avail-badge">In Stock</span>
                </div>
                <!-- VELO -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Velo reuse.jpg" alt="VELO Nicotine Pouches">
                    <h3>VELO</h3>
                    <span class="avail-badge">In Stock</span>
                </div>
                <!-- Pablo -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Pablo reuse.jpg" alt="Pablo Nicotine Pouches">
                    <h3>Pablo</h3>
                    <span class="avail-badge">In Stock</span>
                </div>
                <!-- ZYN -->
                <div class="phone-product-card">
                    <img loading="lazy" src="ZYN Pouches Reuse.webp" alt="ZYN Nicotine Pouches">
                    <h3>ZYN</h3>
                    <span class="avail-badge">In Stock</span>
                </div>
            </div>

            <div class="section-header text-center reveal">
                <h2>Disposable Vapes</h2>
                <div class="accent-divider"></div>
            </div>

            <div class="phones-grid reveal" style="margin-top: 30px;">
                <!-- Lost Mary -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Lost Mary reuse.jpg" alt="Lost Mary Vapes">
                    <h3>Lost Mary</h3>
                    <span class="avail-badge">In Stock</span>
                </div>
                <!-- IVG -->
                <div class="phone-product-card">
                    <img loading="lazy" src="IVG Reuse 1.jpg" alt="IVG Vapes">
                    <h3>IVG</h3>
                    <span class="avail-badge">In Stock</span>
                </div>
                <!-- Elf Bar -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Elf reuse.jpg" alt="Elf Bar Vapes">
                    <h3>Elf Bar</h3>
                    <span class="avail-badge">In Stock</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Final CTA -->
    <section class="final-cta text-center reveal" style="background-image: linear-gradient(rgba(17, 17, 17, 0.75), rgba(17, 17, 17, 0.85)), url('laptop-circuit-board.jpg');">
        <div class="container">
            <h2>Looking for specific flavours or strengths?</h2>
            <p>Visit our store at 7-11 St John's Hill, London, or call us directly to check current stock levels.</p>
            <a href="tel:07438125133" class="btn btn-primary btn-large"><i class="fa-solid fa-phone"></i> Call 07438 125133</a>
        </div>
    </section>
''' + get_footer()

with open(os.path.join(dest_dir, "vapespouches.html"), "w", encoding="utf-8") as f:
    f.write(vapes_content)
print("vapes-pouches.html written.")


# ----------------- Write phones-in-store.html -----------------
phones_content = get_header("Phones In Store", "Quality pre-owned and new handsets in stock. iPhone, Samsung, and Google Pixel models.") + '''
    <!-- Page Hero -->
    <section class="page-hero text-center reveal">
        <div class="container">
            <h1>Phones In Store</h1>
            <p>Quality pre-owned and new handsets in stock in London.</p>
        </div>
    </section>

    <!-- Product Grid Section -->
    <section class="phones-section">
        <div class="container">
            <p class="intro-paragraph text-center">We carry a stock of fully-tested second-hand handsets and brand new phones. Each pre-owned device goes through our rigorous quality diagnostics and comes with store guarantees. Check out our current range below.</p>
            
            <div class="phones-grid reveal" style="margin-top: 30px;">
                <!-- iPhone 17 Pro Max -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Iphone 17 pro max.webp" alt="iPhone 17 Pro Max">
                    <h3>iPhone 17 Pro Max</h3>
                    <span class="avail-badge">Available In Store</span>
                </div>
                <!-- iPhone 17 -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Iphone 17.webp" alt="iPhone 17">
                    <h3>iPhone 17</h3>
                    <span class="avail-badge">Available In Store</span>
                </div>
                <!-- Samsung S26 Ultra -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Samsung s26 ultra.webp" alt="Samsung Galaxy S26 Ultra">
                    <h3>Samsung Galaxy S26 Ultra</h3>
                    <span class="avail-badge">Available In Store</span>
                </div>
                <!-- Samsung Galaxy Z Flip 6 -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Samsung Flip 6.webp" alt="Samsung Galaxy Z Flip 6">
                    <h3>Samsung Galaxy Z Flip 6</h3>
                    <span class="avail-badge">Available In Store</span>
                </div>
                <!-- Google Pixel 10a -->
                <div class="phone-product-card">
                    <img loading="lazy" src="Google Pixel 10a.webp" alt="Google Pixel 10a">
                    <h3>Google Pixel 10a</h3>
                    <span class="avail-badge">Available In Store</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Final CTA -->
    <section class="final-cta text-center reveal" style="background-image: linear-gradient(rgba(17, 17, 17, 0.75), rgba(17, 17, 17, 0.85)), url('laptop-technician.jpg');">
        <div class="container">
            <h2>Want to trade-in your phone or check availability?</h2>
            <p>Give us a call to confirm pricing, specs, and stock levels before visiting.</p>
            <a href="tel:07438125133" class="btn btn-primary btn-large"><i class="fa-solid fa-phone"></i> Call 07438 125133</a>
        </div>
    </section>
''' + get_footer()

with open(os.path.join(dest_dir, "phonesinstore.html"), "w", encoding="utf-8") as f:
    f.write(phones_content)
print("phones-in-store.html written.")