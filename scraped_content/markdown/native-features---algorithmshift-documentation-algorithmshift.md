# Native Features - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/mobile/native  
**Scraped:** 2025-12-10 14:03:25

**Description:** Access device capabilities: camera, location, push notifications, biometrics, and more.

---

Native Features - AlgorithmShift Documentation | AlgorithmShiftDocumentationMobile Apps
# Native Device Features

Access device capabilities through React Native modules. Camera, location, biometrics, and more.

### Camera & Photos

- • Take photos
- • Record videos
- • Photo library access
- • Image picker

### Location Services

- • GPS location
- • Geofencing
- • Background location
- • Maps integration

### Notifications

- • Push notifications
- • Local notifications
- • Scheduled alerts
- • Badge counts

### Biometrics

- • Face ID (iOS)
- • Touch ID (iOS)
- • Fingerprint (Android)
- • Secure authentication

### Device Info

- • Battery status
- • Network info
- • Device model
- • OS version

### Sensors

- • Accelerometer
- • Gyroscope
- • Compass
- • Proximity sensor

## Camera Integration
Copy
```
import { Camera } from 'react-native-vision-camera';

// Take photo
const photo = await camera.current.takePhoto({
  qualityPrioritization: 'quality',
  flash: 'auto',
});

// Upload to AlgorithmShift storage
const formData = new FormData();
formData.append('file', {
  uri: photo.path,
  type: 'image/jpeg',
  name: 'photo.jpg'
});

const response = await fetch('/api/v1/storage/upload', {
  method: 'POST',
  body: formData
});
```

## Location Services
Copy
```
import Geolocation from '@react-native-community/geolocation';

// Get current position
Geolocation.getCurrentPosition(
  (position) => {
    const { latitude, longitude } = position.coords;
    
    // Send to API
    updateUserLocation({
      lat: latitude,
      lng: longitude,
      timestamp: position.timestamp
    });
  },
  (error) => console.error(error),
  { enableHighAccuracy: true, timeout: 20000 }
);

// Watch position changes
const watchId = Geolocation.watchPosition(
  (position) => {
    // Update UI with new position
  }
);
```
