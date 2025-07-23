#!/usr/bin/env python3
"""
Script to fix browser connection issues for OAuth
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def kill_browser_processes():
    """Kill all browser processes"""
    browsers = [
        'opera.exe',
        'chrome.exe', 
        'msedge.exe',
        'firefox.exe',
        'brave.exe'
    ]
    
    print("🔄 Closing all browser processes...")
    for browser in browsers:
        try:
            subprocess.run(['taskkill', '/f', '/im', browser], 
                         capture_output=True, check=False)
        except:
            pass
    
    print("✅ Browser processes closed")
    time.sleep(2)

def fix_browser_config():
    """Fix browser configuration"""
    print("🔧 Fixing browser configuration...")
    
    # Create config directory
    config_dir = Path.home() / "Documents" / ".cursor-free-vip"
    config_dir.mkdir(parents=True, exist_ok=True)
    
    config_file = config_dir / "config.ini"
    
    # Read current config or create new one
    config_content = """[Browser]
default_browser = chrome
chrome_path = C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe
chrome_driver_path = 
edge_path = C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe
edge_driver_path = 
firefox_path = C:\\Program Files\\Mozilla Firefox\\firefox.exe
firefox_driver_path = 
brave_path = C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe
brave_driver_path = 
opera_path = C:\\Users\\asus\\AppData\\Local\\Programs\\Opera\\opera.exe
opera_driver_path = 
operagx_path = C:\\Users\\asus\\AppData\\Local\\Programs\\Opera GX\\opera.exe
operagx_driver_path = 

[Turnstile]
handle_turnstile_time = 2
handle_turnstile_random_time = 1-3

[Timing]
min_random_time = 0.1
max_random_time = 0.8
page_load_wait = 0.1-0.8
input_wait = 0.3-0.8
submit_wait = 0.5-1.5
verification_code_input = 0.1-0.3
verification_success_wait = 2-3
verification_retry_wait = 2-3
email_check_initial_wait = 4-6
email_refresh_wait = 2-4
settings_page_load_wait = 1-2
failed_retry_time = 0.5-1
retry_interval = 8-12
max_timeout = 160

[Utils]
enabled_update_check = True
enabled_force_update = False
enabled_account_info = True

[OAuth]
show_selection_alert = False

[Language]
default_language = vi
language_cache_dir = C:\\Users\\asus\\Documents\\.cursor-free-vip\\locales

[WindowsPaths]
storage_path = C:\\Users\\asus\\AppData\\Roaming\\Cursor\\User\\globalStorage\\storage.json
sqlite_path = C:\\Users\\asus\\AppData\\Roaming\\Cursor\\User\\globalStorage\\state.vscdb
machine_id_path = C:\\Users\\asus\\AppData\\Roaming\\Cursor\\machineId

[TempMailPlus]
enabled = false
email = 
epin = 
"""
    
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    print(f"✅ Config saved to: {config_file}")

def main():
    print("🔧 Browser Fix Tool for Cursor Free VIP")
    print("=" * 50)
    
    # Step 1: Kill browser processes
    kill_browser_processes()
    
    # Step 2: Fix config
    fix_browser_config()
    
    print("\n✅ Browser fix completed!")
    print("\n📝 Recommendations:")
    print("1. Use Chrome instead of Opera GX (more stable)")
    print("2. Make sure Chrome is installed")
    print("3. Run without administrator privileges if possible")
    print("4. Close all browser windows before running OAuth")
    
    print(f"\n🚀 Now try running: python main.py")

if __name__ == "__main__":
    main()
