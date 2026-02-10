import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_game():
    print("Testing /api/start...")
    try:
        r = requests.post(f"{BASE_URL}/api/start")
        print(f"Status: {r.status_code}")
        data = r.json()
        print(f"Keys: {data.keys()}")
        print(f"Choices: {data.get('choices')}")
        
        if not data.get('choices'):
            print("ERROR: No choices in start!")
        else:
            print("Success: Start has choices.")

        # Test choice 0 (Open door -> 2a)
        print("\nTesting /api/choice (index 0)...")
        r = requests.post(f"{BASE_URL}/api/choice", json={'choice_index': 0})
        print(f"Status: {r.status_code}")
        data = r.json()
        print(f"Message: {data.get('message')}")
        print(f"Choices: {data.get('choices')}")

        if not data.get('choices'):
            print("ERROR: No choices in 2a!")
        else:
            print("Success: 2a has choices.")

    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    test_game()
