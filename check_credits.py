import requests
import json

def check_api_credits():
    api_key = "sk-rulTxMpOvei39xMEdaKABdZS95i0LlN2TpD7YJrODZxwkn9q"
    
    print("🔍 Checking Stability AI Account Credits...")
    print("=" * 50)
    
    headers = {
        'Authorization': f'Bearer {api_key}',
    }
    
    try:
        # Get account information
        response = requests.get(
            'https://api.stability.ai/v1/user/account',
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            account_data = response.json()
            print("✅ Account Information:")
            print(f"📧 Email: {account_data.get('email', 'N/A')}")
            print(f"🆔 User ID: {account_data.get('id', 'N/A')}")
            
            # Check organizations
            organizations = account_data.get('organizations', [])
            if organizations:
                org = organizations[0]  # Default organization
                print(f"🏢 Organization: {org.get('name', 'N/A')}")
                print(f"👤 Role: {org.get('role', 'N/A')}")
            
            # Try to get credit information
            try:
                credit_response = requests.get(
                    'https://api.stability.ai/v1/user/credits',
                    headers=headers,
                    timeout=10
                )
                
                if credit_response.status_code == 200:
                    credit_data = credit_response.json()
                    print("\n💰 Credit Information:")
                    print(f"💳 Credits Available: {credit_data.get('credits', 'N/A')}")
                    
                    # Estimate 3D conversions based on typical costs
                    credits = credit_data.get('credits', 0)
                    if isinstance(credits, (int, float)):
                        # Estimate: 1 credit per 3D conversion (this may vary)
                        estimated_conversions = int(credits)
                        print(f"🎯 Estimated 3D Conversions: {estimated_conversions}")
                        
                        if estimated_conversions > 0:
                            print(f"✅ You can generate approximately {estimated_conversions} 3D models!")
                        else:
                            print("❌ No credits available for 3D conversion")
                    else:
                        print("⚠️  Credit information format unknown")
                        
                else:
                    print(f"❌ Could not fetch credit info: {credit_response.status_code}")
                    
            except Exception as e:
                print(f"❌ Error fetching credits: {e}")
                
        else:
            print(f"❌ Could not fetch account info: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("💡 Note: Credit costs may vary based on:")
    print("   - Image complexity")
    print("   - Processing time")
    print("   - API usage patterns")
    print("   - Current pricing")
    print("=" * 50)

if __name__ == "__main__":
    check_api_credits() 