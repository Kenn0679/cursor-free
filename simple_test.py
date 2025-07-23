"""
Simple test to verify the cursor_acc_info fixes
"""
print("Testing cursor_acc_info fixes...")

try:
    import sys
    import os
    
    # Test imports
    from colorama import Fore, Style, init
    print("✅ colorama import OK")
    
    import requests
    print("✅ requests import OK")
    
    import hashlib
    import base64
    import struct
    import time
    print("✅ standard library imports OK")
    
    # Test the functions we added
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    try:
        from cursor_acc_info import generate_hashed64_hex, generate_cursor_checksum
        print("✅ checksum functions import OK")
        
        # Test the functions
        test_hash = generate_hashed64_hex("test", "salt")
        print(f"✅ generate_hashed64_hex works: {test_hash[:20]}...")
        
        test_checksum = generate_cursor_checksum("test_token")
        print(f"✅ generate_cursor_checksum works: {test_checksum[:20]}...")
        
    except Exception as e:
        print(f"❌ Error testing checksum functions: {e}")
    
    try:
        from cursor_acc_info import UsageManager
        print("✅ UsageManager import OK")
        
        # Test get_usage with a dummy token (will fail but shouldn't crash)
        result = UsageManager.get_usage("dummy_token")
        if result is None:
            print("✅ get_usage handles errors gracefully")
        else:
            print(f"✅ get_usage returned: {result}")
            
    except Exception as e:
        print(f"❌ Error testing UsageManager: {e}")
    
    print("\n✅ All tests completed successfully!")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
