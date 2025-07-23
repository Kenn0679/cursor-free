#!/usr/bin/env python3
"""
Test script to check if the cursor_acc_info.py fixes work
"""

import sys
import os

# Add the current directory to path so we can import the modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from cursor_acc_info import display_account_info, get_token
    print("✅ Successfully imported cursor_acc_info")
    
    # Test if we can get token (this might be None if not logged in)
    token = get_token()
    if token:
        print(f"✅ Token found: {token[:20]}...")
    else:
        print("⚠️  No token found - this is normal if not logged into Cursor")
    
    # Test display_account_info - this should not crash even with API errors
    try:
        print("\n🔍 Testing display_account_info...")
        display_account_info()
        print("✅ display_account_info completed without errors")
    except Exception as e:
        print(f"❌ Error in display_account_info: {e}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n✅ Test completed")
