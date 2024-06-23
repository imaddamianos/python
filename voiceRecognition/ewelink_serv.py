

from ewelink import EWeLinkApi, EWeLinkConnectionError

async def main():
    # Define your eWeLink credentials
    ewelink_email = 'imad-damianos@hotmail.com'
    ewelink_password = 'im11ad11'
    
    try:
        # Create an instance of the EWeLinkApi with your credentials
        api = EWeLinkApi(email=ewelink_email, password=ewelink_password)
        
        # Login to eWeLink
        await api.login()
        
        # Print user information
        print("User Info:", api.user_info)
        
        # Get all devices associated with the account
        devices = await api.get_devices()
        print("Devices:", devices)
        
        # Example of controlling a device
        device_id = 'your_device_id_here'
        device = devices.get(device_id)
        
        if device:
            # Check device state
            print("Device State:", device.state)
            
            # Toggle device state (turn on if it's off, turn off if it's on)
            await device.toggle()
            
            # Refresh device info
            await device.refresh()
            print("Updated Device State:", device.state)
        else:
            print(f"Device with ID '{device_id}' not found.")
    
    except EWeLinkConnectionError as e:
        print("Connection Error:", e)
    
    except Exception as e:
        print("An error occurred:", e)

