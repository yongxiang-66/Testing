import pyautogui
import cv2
import numpy as np
import time
import os
from datetime import datetime

def main():
    """Screen recorder with improved error handling and features."""
    
    # Get actual screen resolution dynamically
    screen_width, screen_height = pyautogui.size()
    resolution = (screen_width, screen_height)
    
    # Video codec (XVID for .avi, or use 'mp4v' for .mp4)
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    
    # Create recordings folder if it doesn't exist
    recordings_folder = "recordings"
    os.makedirs(recordings_folder, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(recordings_folder, f"Recording_{timestamp}.avi")
    
    # Frame rate (30 FPS is more reasonable than 50)
    fps = 30.0
    
    # Create VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    
    # Check if VideoWriter initialized successfully
    if not out.isOpened():
        print("Error: Could not open video writer!")
        return
    
    # Preview window disabled for background recording
    # cv2.namedWindow("Live Recording", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("Live Recording", 640, 360)
    
    print(f"Recording started: {filename}")
    print(f"Resolution: {resolution[0]}x{resolution[1]} @ {fps} FPS")
    print("Press F2 to stop recording")
    print("Press F3 to pause/resume")
    
    paused = False
    frame_count = 0
    start_time = time.time()
    
    try:
        while True:
            # Take screenshot
            img = pyautogui.screenshot()
            
            # Convert PIL image to numpy array
            frame = np.array(img)
            
            # Convert RGB (PyAutoGUI) to BGR (OpenCV)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Write frame only if not paused
            if not paused:
                out.write(frame)
                frame_count += 1
            
            # Add recording indicator
            status_text = "PAUSED" if paused else "REC"
            color = (0, 255, 255) if paused else (0, 0, 255)
            cv2.circle(frame, (30, 30), 10, color, -1)
            cv2.putText(frame, status_text, (50, 40), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            
            # Display disabled for background recording
            # cv2.imshow('Live Recording', frame)
            
            # Handle keyboard input (works without window)
            key = cv2.waitKey(1) & 0xFF
            
            if key == 0x71:  # F2 key - Quit
                break
            elif key == 0x72:  # F3 key - Pause/Resume
                paused = not paused
                print("Recording paused" if paused else "Recording resumed")
    
    except KeyboardInterrupt:
        print("\nRecording interrupted by user")
    
    except Exception as e:
        print(f"Error during recording: {e}")
    
    finally:
        # Cleanup
        duration = time.time() - start_time
        out.release()
        cv2.destroyAllWindows()
        
        print(f"\nRecording stopped!")
        print(f"Frames recorded: {frame_count}")
        print(f"Duration: {duration:.2f} seconds")
        print(f"Saved to: {filename}")

if __name__ == "__main__":
    main()

