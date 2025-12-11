# Mobile Preview - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/mobile/preview  
**Scraped:** 2025-12-10 14:04:03

**Description:** Preview your mobile app on real devices using QR codes and Expo Go. Test on iOS and Android instantly.

---

Mobile Preview - AlgorithmShift Documentation | AlgorithmShiftDocumentationMobile Apps
# Mobile Preview

Test your mobile app on real iOS and Android devices instantly. Scan a QR code with Expo Go and see your app running on your phone in seconds.

### Canvas Preview

See mobile components rendered in the builder canvas using React Native Web

- • Click "App" button in canvas
- • Instant visual feedback
- • No device needed

### Device Preview

Test on real iOS/Android devices with QR code and Expo Go

- • Scan QR code
- • Test on real device
- • Native performance

## How Mobile Preview Works

### Fargate-Based Preview System

AlgorithmShift uses AWS Fargate to deploy your app as a temporary Expo development server:

1. Your app is packaged as a complete React Native/Expo project
1. Project is uploaded to S3 as a ZIP file
1. Fargate container downloads and runs Expo dev server
1. QR code is generated pointing to the Expo server
1. Scan QR code with Expo Go app on your device
1. App loads and runs natively on your phone

## Quick Start Guide
1
### Install Expo Go

Download Expo Go app on your iOS or Android device:

iOS (iPhone/iPad)

Download from App Store
[App Store Link →](https://apps.apple.com/app/expo-go/id982107779)
Android

Download from Google Play
[Google Play Link →](https://play.google.com/store/apps/details?id=host.exp.exponent)2
### Build Your Mobile App

Create or open a mobile app in AlgorithmShift:
Copy
```
// When creating app, set type to 'mobile'
{
  "name": "My Mobile App",
  "type": "mobile",  // ← Important!
  "workspace_id": "your-workspace-id"
}
```
Component drawer shows mobile components automaticallyDrag TouchableOpacity, FlatList, TextInput, etc.Configure mobile-specific properties3
### Start Mobile Preview

Click the "Mobile Preview" button in your app builder:

What happens:

1. App is packaged as React Native/Expo project
1. ZIP file uploaded to S3
1. Fargate container starts Expo dev server (~30-60 seconds)
1. QR code appears when ready

First preview takes 30-60 seconds while the container starts. Subsequent previews are faster if container stays warm.
4
### Scan QR Code

Use Expo Go to scan the QR code:

iOS

1. Open Expo Go app
1. Tap "Scan QR Code"
1. Point camera at QR code
1. App loads automatically

Android

1. Open Expo Go app
1. Tap "Scan QR Code"
1. Point camera at QR code
1. Tap to open when detected
5
### Test Your App

Your app is now running natively on your device!
Test touch interactions (tap, swipe, scroll)Try different screen orientationsTest keyboard interactions with TextInputVerify navigation between screensCheck performance on real device
## Preview Architecture
Copy
```
┌─────────────────────┐
│   AlgorithmShift    │
│   App Builder       │
└──────────┬──────────┘
           │
           │ 1. Click "Mobile Preview"
           ↓
┌─────────────────────┐
│   Backend API       │
│   - Generate RN     │
│   - Create ZIP      │
│   - Upload to S3    │
└──────────┬──────────┘
           │
           │ 2. Trigger Fargate
           ↓
┌─────────────────────┐
│   AWS Fargate       │
│   - Download ZIP    │
│   - Extract files   │
│   - npm install     │
│   - Start Expo      │
└──────────┬──────────┘
           │
           │ 3. Generate QR Code
           ↓
┌─────────────────────┐
│   Expo Dev Server   │
│   Port 19000/19001  │
└──────────┬──────────┘
           │
           │ 4. Scan QR Code
           ↓
┌─────────────────────┐
│   Your Phone        │
│   (Expo Go App)     │
│   - iOS/Android     │
└─────────────────────┘
```

## Preview Modes Comparison
FeatureCanvas PreviewDevice PreviewSpeedInstant30-60 seconds (first time)Device NeededNoYes (iOS/Android)RenderingReact Native WebNative React NativePerformanceWeb-likeTrue nativeTouch InteractionsMouse simulationReal touch gesturesKeyboardDesktop keyboardMobile keyboard typesUse CaseQuick visual checkReal device testing
## Troubleshooting

### QR Code Not Appearing

Possible causes:

- Fargate container starting (wait 30-60 seconds)
- Build error (check logs in preview modal)
- AWS resources unavailable

Solution: Wait for container to fully start. Check console logs for errors.

### App Won't Load on Device

Possible causes:

- Device not on same network (Expo requires connectivity)
- Firewall blocking Expo dev server
- Expo Go app outdated

Solution: Ensure device and server can communicate. Update Expo Go app. Try scanning again.

### "Unable to Connect to Metro" Error

This means Expo Go can't reach the development server.

Solution:

- Wait longer for server to fully start
- Check if Fargate container is running
- Rescan QR code
- Restart Expo Go app

### Components Not Rendering Correctly

Check:

- Using mobile components (not web components)
- StyleSheet properties valid for React Native
- No web-specific CSS (like display: grid)

Solution: Use mobile components from the component drawer. Check properties panel for mobile-specific props.

## Preview Limitations

### Current Limitations

- • Preview Duration:Preview expires after 30 minutes of inactivity
- • Data Sources:May show placeholder data instead of live API data
- • Authentication:May not reflect actual auth flows
- • Native Modules:Some native features (camera, maps) may not work in preview
- • Performance:Preview runs in dev mode (slower than production build)

For production testing: Download the ZIP and build locally or deploy to app stores.

## Download for Local Development

### Download Complete Project

For full control and local development, download your app as a complete React Native/Expo project:

1. Click "Download ZIP" in Mobile Preview modal
1. Extract ZIP file
1. Run npm install
1. Run npm start to start Expo
1. Scan QR code or run on simulator
Copy
```
# Extract and run locally
unzip my-mobile-app.zip
cd my-mobile-app
npm install
npm start

# Run on iOS simulator (macOS only)
npm run ios

# Run on Android emulator
npm run android
```

## Learn More
[### Mobile Components

21 native React Native components](https://www.algorithmshift.ai/docs/mobile/components)[### React Native Setup

Local development environment](https://www.algorithmshift.ai/docs/mobile/react-native)[### App Store Deployment

Deploy to iOS and Android stores](https://www.algorithmshift.ai/docs/mobile/deployment)[### Mobile App Builder

Visual mobile app development](https://www.algorithmshift.ai/docs/visual-builder/mobile-apps)
