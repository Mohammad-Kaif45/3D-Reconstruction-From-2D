import requests
import os
import time

class Image3DConverter:
    def __init__(self, api_key, mock_mode=False):
        self.api_key = api_key
        self.api_url = 'https://api.stability.ai/v2beta/3d/stable-fast-3d'
        self.mock_mode = mock_mode

    def convert_image(self, image_path):
        if self.mock_mode:
            return self._mock_conversion(image_path)
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
        }

        try:
            with open(image_path, 'rb') as image_file:
                files = {'image': image_file}
                print("Sending request to Stability AI API...")
                response = requests.post(
                    self.api_url,
                    headers=headers,
                    files=files,
                    timeout=60  # Increased timeout for 3D processing
                )

            if response.status_code == 200:
                print("✅ 3D conversion successful!")
                return response.content
            elif response.status_code == 402:
                error_msg = "API credits exhausted. Please purchase more credits at https://platform.stability.ai/account/credits"
                print(f"❌ {error_msg}")
                raise Exception(error_msg)
            elif response.status_code == 401:
                error_msg = "Invalid API key. Please check your Stability AI API key."
                print(f"❌ {error_msg}")
                raise Exception(error_msg)
            else:
                error_msg = f"API request failed with status {response.status_code}: {response.text}"
                print(f"❌ {error_msg}")
                raise Exception(error_msg)
                
        except requests.exceptions.Timeout:
            error_msg = "Request timed out. 3D conversion takes time, please try again."
            print(f"❌ {error_msg}")
            raise Exception(error_msg)
        except requests.exceptions.RequestException as e:
            error_msg = f"Network error: {str(e)}"
            print(f"❌ {error_msg}")
            raise Exception(error_msg)
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            print(f"❌ {error_msg}")
            raise Exception(error_msg)

    def _mock_conversion(self, image_path):
        """Mock conversion for testing purposes - creates a simple GLB file"""
        print("🔄 Using mock 3D conversion for testing...")
        
        # Create a simple GLB file content (minimal valid GLB)
        # This is a basic GLB structure - in real use, you'd get this from the API
        mock_glb_content = self._create_mock_glb()
        
        print("✅ Mock 3D conversion completed!")
        return mock_glb_content
    
    def _create_mock_glb(self):
        """Create a minimal valid GLB file for testing"""
        # This is a very basic GLB structure - just for testing
        import struct
        
        # GLB header (12 bytes)
        magic = b'glTF'
        version = struct.pack('<I', 2)
        length = struct.pack('<I', 44)  # Total file length
        
        # JSON chunk
        json_data = b'{"asset":{"version":"2.0"},"scene":0,"scenes":[{"nodes":[]}],"nodes":[],"meshes":[]}'
        json_length = struct.pack('<I', len(json_data))
        json_type = struct.pack('<I', 0x4E4F534A)  # JSON chunk type
        
        # Binary chunk (empty for this mock)
        binary_length = struct.pack('<I', 0)
        binary_type = struct.pack('<I', 0x004E4942)  # Binary chunk type
        
        # Combine all parts
        glb_content = magic + version + length + json_length + json_type + json_data + binary_length + binary_type
        
        return glb_content


# Example usage
def main():
    # For testing, use mock mode
    api_key = 'sk-rulTxMpOvei39xMEdaKABdZS95i0LlN2TpD7YJrODZxwkn9q'
    converter = Image3DConverter(api_key, mock_mode=True)  # Enable mock mode for testing
    
    # Test with a sample image
    image_path = r'media/uploads/45.jpg'  # Use an existing image
    
    if os.path.exists(image_path):
        try:
            result = converter.convert_image(image_path)
            
            if result:
                # Save the resulting 3D model
                output_path = r'media/models/test_model.glb'
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                with open(output_path, 'wb') as output_file:
                    output_file.write(result)
                print("✅ Mock conversion successful. 3D model saved to:", output_path)
            else:
                print("❌ Conversion failed")
        except Exception as e:
            print(f"❌ Error during conversion: {e}")
    else:
        print(f"❌ Test image not found: {image_path}")

if __name__ == '__main__':
    main()
